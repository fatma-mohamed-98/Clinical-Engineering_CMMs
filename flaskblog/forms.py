from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

  
    
class RegistrationForm(FlaskForm):
    
    Nomenclature = StringField('Nomenclature',validators=[ Length(min=1, max=400)])
    Manufacturer = StringField('Manufacturer',validators=[ Length(min=1, max=400)])
    Agent       = StringField('Agent',validators=[ Length(min=1, max=400)])
    inventory_number  = StringField('inventory_number',validators=[Length(min=1, max=400)])
    Serial_number  = StringField('Serial_number',validators=[ Length(min=1, max=400)])
    Installation_Date  = StringField('Installation_Date',validators=[ Length(min=1, max=400)])
    Operation  = StringField('Operation',validators=[ Length(min=1, max=400)])
    Location  = StringField('Location',validators=[ Length(min=1, max=400)])
    
    warrantly_period  = StringField('warrantly_period',validators=[ Length(min=1, max=400)])
    Contact_data_of_manufacturer  = StringField('Contact_data_of_manufacturer',validators=[Length(min=1, max=400)])
    Department  = StringField('Department',validators=[Length(min=1, max=400)])
    
    cause_of_fault  = StringField('cause_of_fault',validators=[Length(min=1, max=400)])
    fault_description  = StringField('fault_description',validators=[Length(min=1, max=400)])
    Technician_name  = StringField('Technician_name',validators=[ Length(min=1, max=400)])
    
    start_date_of_job_order  = StringField('start_date_of_job_order',validators=[Length(min=1, max=400)])
    Action_taken  = StringField('Action_taken',validators=[Length(min=1, max=400)])
    predictive_maintenance_Scheduling  = StringField('predictive_maintenance_Scheduling',validators=[ Length(min=1, max=400)])
    Price  = StringField('Price',validators=[ Length(min=1, max=400)])
       
 
   
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    
    Nomenclature = StringField('Nomenclature',validators=[DataRequired(), Length(min=1, max=400)])
    

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    
    Nomenclature = StringField('Nomenclature',validators=[DataRequired(), Length(min=1, max=400)])
    Manufacturer = StringField('Manufacturer',validators=[DataRequired(), Length(min=1, max=400)])
    Agent       = StringField('Agent',validators=[DataRequired(), Length(min=1, max=400)])
    inventory_number  = StringField('inventory_number',validators=[DataRequired(), Length(min=1, max=400)])
    Serial_number  = StringField('Serial_number',validators=[DataRequired(), Length(min=1, max=400)])
    Installation_Date  = StringField('Installation_Date',validators=[DataRequired(), Length(min=1, max=400)])
    Operation  = StringField('Operation',validators=[DataRequired(), Length(min=1, max=400)])
    Location  = StringField('Location',validators=[DataRequired(), Length(min=1, max=400)])
    
    warrantly_period  = StringField('warrantly_period',validators=[DataRequired(), Length(min=1, max=400)])
    Contact_data_of_manufacturer  = StringField('Contact_data_of_manufacturer',validators=[DataRequired(), Length(min=1, max=400)])
    Department  = StringField('Department',validators=[DataRequired(), Length(min=1, max=400)])
    
    cause_of_fault  = StringField('cause_of_fault',validators=[DataRequired(), Length(min=1, max=400)])
    fault_description  = StringField('fault_description',validators=[DataRequired(), Length(min=1, max=400)])
    Technician_name  = StringField('Technician_name',validators=[DataRequired(), Length(min=1, max=400)])
    
    start_date_of_job_order  = StringField('start_date_of_job_order',validators=[DataRequired(), Length(min=1, max=400)])
    Action_taken  = StringField('Action_taken',validators=[DataRequired(), Length(min=1, max=400)])
    predictive_maintenance_Scheduling  = StringField('predictive_maintenance_Scheduling',validators=[DataRequired(), Length(min=1, max=400)])
    Price  = StringField('Price',validators=[DataRequired(), Length(min=1, max=400)])
    
    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, Nomenclature):
        if Nomenclature.data != current_user.Nomenclature:
            user = User.query.filter_by(Nomenclature=Nomenclature.data).first()
            if user:
                raise ValidationError('That Nomenclature is taken. Please choose a different one.')

    