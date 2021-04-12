from flask import *
from model import *
from uuid import uuid4
import os,requests,re


app = Flask(__name__)
app.config.from_object("config.Config")
@app.before_first_request
def before_first_request_func():
    db.init_app(app)
    if not os.path.isfile('/orchestrator.db'):
        with app.app_context():
            db.create_all()
    # print("This function will run once")




"""Template download code"""
def find_file(filename, search_path):
    result = None
    for root, dir, files in os.walk(search_path):
        if filename in files:
            print(search_path)
            result = os.path.join(root, filename)
    return result

def fetch_site_id():
    sites = Site.query.all()
    for site in sites:
        return site.site_id

@app.route('/')
def hello_world():
    return 'Hello Flask under Apache!'

#Download the file package from the repo.
@app.route('/files', methods=["GET", "POST"])
def files():
    try:
        #FILE_PATH = 'C:\flask_wsgi\packages'
        file_name = request.args.get('file_name')
        file_to_be_returned = find_file(file_name, app.config["FILE_PATH"])
        if file_to_be_returned is not None:
            return send_file(file_to_be_returned, app.config["ATTACHMENT_FILE_TEMPLATE"], as_attachment=True)
        else:
            return 'Please check the name of file and try again.'
    except Exception as e:
        print(e)
        return 'Please try again later'



#Download the template from repo.
@app.route('/templates', methods=["GET", "POST"])
def templates():
    try:
        #TEMPLATE_PATH = 'C:\flask_wsgi\templates'
        file_name = request.args.get('template_name')
        file_to_be_returned = find_file(file_name, app.config["TEMPLATE_PATH"])
        if file_to_be_returned is not None:
            return send_file(file_to_be_returned, file_name, as_attachment=True)
        else:
            return 'Please check the template name and try again.'

    except Exception as e:
        print(e)
        return 'Please try again later'



#Get the list of all the agents present in Agent Table.
@app.route('/agents', methods=["GET"])
def get_list_of_agents():
    try:
        agents_list_result = []
        agents_list = Agent.query.all()
        if agents_list:
            for agent in agents_list:
                agents_list_result.append(agent.as_dict())
            return jsonify(agents_list_result,
                           {"message": "Agents list retrieved successfully"}), 200
        return jsonify({"message": "No agents exist"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error occurred while getting agents list"}), 500



#Get specific agent present in Agent table using agent_id
@app.route('/agents/<agent_id>', methods=["GET"])
def get_agent(agent_id):
    try:
        agent = Agent.query.filter(Agent.agent_id == agent_id).first()
        if agent is not None:
            return jsonify(agent.as_dict())
        return jsonify({"message": "No agent exists with agent_id: " + agent_id}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error occurred while getting agent with id: " + agent_id}), 500



#Register of agent along with agent_id and returning agent id.
@app.route('/agentregister', methods=["POST"])
def agent_register():
    Agent_id = str(uuid4().hex[:8])
    new_agent = Agent(
        agent_id= Agent_id,
        account_name=request.json['account_name'],
        top_level_asset_pcsn=request.json['top_level_asset_pcsn'],
        mac_address=request.json['mac_address'],
        ip_address=request.json['ip_address'],
        hostname=request.json['hostname'],
        operating_system=request.json['operating_system']
    )
    site_id = fetch_site_id()
    agent = {
    "site_id": site_id,
    "agent_id": Agent_id,
    "account_name": request.json['account_name'],
    "top_level_asset_pcsn": request.json['top_level_asset_pcsn'],
    "mac_address": request.json['mac_address'],
    "ip_address": request.json['ip_address'],
    "hostname": request.json['hostname'],
    "operating_system": request.json['operating_system']
    }
    requests.post("http://localhost:5000/workstationregister",json=agent)
    db.session.add(new_agent)
    db.session.commit()
    return jsonify(new_agent.agent_id)


#To get list of all available tasks
@app.route('/alltaskslist', methods=["GET"])
def tasks_list():
    try:
        tasks_list_result = []
        tasks_list = Task.query.all()
        if tasks_list:
            for task in tasks_list:
                tasks_list_result.append(task.as_dict())
            return jsonify(tasks_list_result,
                           {"message": "Tasks list retrieved successfully"}), 200
        return jsonify({"message": "No tasks exist"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": "Error occurred while getting tasks list"}), 500

def getFilename_fromCd(cd):
    if not cd:
        return None
    fname = re.findall("filename=(.+)",cd)
    if len(fname) == 0:
        return None
    return fname[0]

#Post function for creating new task, getting from CO and have to make site_id as Global variable.
@app.route('/addtask')
def add_task():
    site_id = fetch_site_id()
    response = requests.get("http://localhost:5000/tasksearch?site_id="+site_id)
    datas = response.json()
    for data in datas:
        if data['task_type'] == 'workstation registration':
            response = requests.get("http://localhost:5000/registerworkstation",params={"site_id":site_id})
            workstation = json.dumps(response.json())
            with open("credentials.json", "w") as file1:
                file1.write(workstation)
        elif data['task_type'] == 'deploy' or data['task_type'] == 'upgrade':
            try:
                r = requests.get("http://localhost:5000/files",params={"file_name":data['package_name']})
                filename = getFilename_fromCd(r.headers.get('content-disposition'))
                open(filename,'wb').write(r.content)
                r1 = requests.get("http://localhost:5000/templates",params={"template_name":data['template_name']})
                filename1 = getFilename_fromCd(r1.headers.get('content-disposition'))
                open(filename1,'wb').write(r1.content)
            except Exception as e:
                print(e)
        new_task = Task(
                task_id=data['task_id'],
                site_id=data['site_id'],
                agent_id=data['agent_id'],
                task_type=data['task_type'],
                product_name=data['product_name'],
                packages=data['package_name'],
                template_name=data['template_name'],
                status=data['status']
        )
        db.session.add(new_task)
        db.session.commit()
    return jsonify(new_task.as_dict())

@app.route('/updatetaskstatus',methods=["POST"])
def update_task_status():
    task_id = request.args.get('task_id')
    status = request.args.get('status')
    try:
        requests.get("http://localhost:5000/updatetaskcomplete/"+task_id)
        task = Task.query.filter(Task.task_id == task_id)
        task.update({Task.status:status})
        db.session.commit()
        return jsonify({'message':"Updated status successfully"})
    except:
        return jsonify({'message':"Unable to update the status"})

    
#Update the task from Not Initiated to In progress using Agent ID as Parameters.
@app.route('/taskslist',methods=['GET'])  
def task_list_id():
    try:
        agent_id = request.args.get('agent_id')
        task = Task.query.filter(Task.agent_id == agent_id, Task.status == 'Not Initiated' ).first()
        
        if task is not None:
            task_id = task.task_id
            temp_dict = jsonify(task.as_dict())
            Task.query.filter(Task.task_id == task_id).update({Task.status:'In progress'})
        # db.session.update({task.status: 'In Progress'})
            db.session.commit()
            return temp_dict
        return jsonify({"message": "No task exists with agent_id: " + agent_id}), 200
    except:
        return "Programming error"

@app.route('/registersite',methods=['POST'])
def register_site():
    try:
        site_id = str(uuid4().hex[:8])
        site_name = request.json['site_name']
        site_ip = request.json['site_ip']
        account_name = request.json['account_name']
        result ={"site_id": site_id,
        "site_name": site_name,
        "site_ip": site_ip,
        "account_name": account_name}
        requests.post("http://localhost:5000/siteregister",json=result)
        site = Site(site_id=site_id,site_name=site_name,site_ip=site_ip,account_name=account_name)
        db.session.add(site)
        db.session.commit()
        return jsonify({"msg": "successfully stored"})
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///orchestrator.db"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config.from_object("config.Config")
    # db.init_app(app)
    app.run(host="0.0.0.0", port="55001",debug=True)


