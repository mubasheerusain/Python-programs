from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Agent(db.Model):
    agent_id = db.Column(db.String(255), primary_key=True)
    account_name = db.Column(db.String(100))
    top_level_asset_pcsn = db.Column(db.String(255))
    mac_address = db.Column(db.String(100))
    ip_address = db.Column(db.String(100))
    hostname = db.Column(db.String(100))
    operating_system = db.Column(db.String(100))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Site(db.Model):
    site_id = db.Column(db.String, primary_key=True)
    account_name = db.Column(db.String(100))
    site_ip = db.Column(db.String(255))
    site_name = db.Column(db.String(100))
    

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Task(db.Model):
    site_id = db.Column(db.String)
    task_id = db.Column(db.String(255), primary_key=True)
    agent_id = db.Column(db.String)
    task_type = db.Column(db.String(100))
    product_name = db.Column(db.String(100))
    packages = db.Column(db.String(512))
    template_name = db.Column(db.String(100))
    status = db.Column(db.String(100))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
