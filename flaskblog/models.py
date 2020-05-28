from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(db.Model, UserMixin):
    
    id = db.Column(db.String(20), primary_key=True)

    Nomenclature = db.Column(db.String(20), unique=False, nullable=True)
    Manufacturer = db.Column(db.String(20), unique=False, nullable=True)
    Agent = db.Column(db.String(20), unique=False, nullable=True)
    inventory_number = db.Column(db.String(20), unique=False, nullable=True)
    Serial_number = db.Column(db.String(20), unique=False, nullable=True)
    Installation_Date = db.Column(db.String(20), unique=False, nullable=True)
    Operation = db.Column(db.String(20), unique=False, nullable=True)
    Location = db.Column(db.String(20), unique=False, nullable=True)
    
    warrantly_period = db.Column(db.String(20), unique=False, nullable=True)
    Contact_data_of_manufacturer = db.Column(db.String(20), unique=False, nullable=True)
    
    Department = db.Column(db.String(20), unique=False, nullable=True)
    
    cause_of_fault = db.Column(db.String(20), unique=False, nullable=True)
    fault_description = db.Column(db.String(20), unique=False, nullable=True)
    Technician_name = db.Column(db.String(20), unique=False, nullable=True)
    
    start_date_of_job_order = db.Column(db.String(20), unique=False, nullable=True)
    Action_taken = db.Column(db.String(20), unique=False, nullable=True)
    predictive_maintenance_Scheduling = db.Column(db.String(20), unique=False, nullable=True)
    Price = db.Column(db.String(20), unique=False, nullable=True)
    
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return "<User: {}>".format(self.Nomenclature)
        

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
