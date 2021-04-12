# Orchestrator ORM app

Steps to start application:

1. Clone from git
2. Open cmd, cd to the cloned project (varian-orchestrator-app)
3. Create virtual environment using following command
   
   virtualenv varian-virtual-env   
4. Activate it 
   
   varian-virtual-env\Scripts\activate
   
5. Now you are in the v.env, at start of the command prompt you can see (varian-virtual-env)
	
	(varian-virtual-env) C:\Users\..........\varian-orchestrator-app>
	
6. install dependencies using below command
	
	pip install -r requirements.txt
	
7. Use this command to run the app
	
	python main.py

8. For the first time this will create a SQLLite db inside the varian-orchestrator-app\app\orchestrator.db

9. App is up and running on port 5000
	http://127.0.0.1:5000/agents

10. All new routes can be written in main.py above this line only

    if __name__ == '__main__':

    Don't create any route after this line
