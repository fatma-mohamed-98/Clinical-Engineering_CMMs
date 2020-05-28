import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask import request
import csv
from io import TextIOWrapper
import csv
from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
global csv_reader

global i
i=19

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]



@app.route("/")


 
@app.route('/', methods=['GET', 'POST'])
def New_data():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            user = User(id=row[0],Nomenclature=row[1], Manufacturer=row[2] ,Agent=row[3],inventory_number=row[4],Serial_number=row[5],Installation_Date=row[6],Operation=row[7],Location=row[8],warrantly_period=row[9],Contact_data_of_manufacturer=row[10],Department=row[11],cause_of_fault=row[12],fault_description=row[13],Technician_name=row[14],start_date_of_job_order=row[15],Action_taken=row[16],predictive_maintenance_Scheduling=row[17],Price=row[18])
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('Home'))
    return """
            <form method='post' action='/' enctype='multipart/form-data'>
              Upload a csv file: <input type='file' name='file'>
              <input type='submit' value='Upload'>
            </form>
           """

################################################################################################
@app.route('/whoosh', methods=['GET', 'POST'])
def whoosh():

    return render_template('Page-1.html')


@app.route('/Repair_OR', methods=['GET', 'POST'])
def Repair_OR():
    if request.method == 'GET':
        return render_template('Repair.html')

    elif request.method == 'POST':

        i=["0","0","0","0","inventory number","0","0","0","0","0","0","0","cause of fault","fault description","Technician name","start date of job order","Action taken"]
       
        search = request.form.get('search')
        results = []
        user_csv = open("OR.csv")
        reader = csv.DictReader(user_csv)
        for row in reader:
            results.append(dict(row))
        fieldnames = [key for key in results[0].keys()]
        return render_template('Repair.html', results=results, fieldnames=fieldnames, i=i,len=len)



@app.route('/Installation_OR', methods=['GET', 'POST'])
def Installation_OR():
    if request.method == 'GET':
        return render_template('Installation.html')

    elif request.method == 'POST':

        i=["0","0","0","0","inventory number","0","Installation Date"]
        search = request.form.get('search')
        results = []
        user_csv = open("OR.csv")
        reader = csv.DictReader(user_csv)
        for row in reader:
            results.append(dict(row))
        fieldnames = [key for key in results[0].keys()]
        return render_template('Installation.html', results=results, fieldnames=fieldnames,i=i, len=len)


@app.route('/Repair_ICU', methods=['GET', 'POST'])
def Repair_ICU():
    if request.method == 'GET':
        return render_template('Repair.html')

    elif request.method == 'POST':

        i=["0","0","0","0","inventory number","0","0","0","0","0","0","0","cause of fault","fault description","Technician name","start date of job order","Action taken"]
       
        search = request.form.get('search')
        results = []
        user_csv = open("ICU.csv")
        reader = csv.DictReader(user_csv)
        for row in reader:
            results.append(dict(row))
        fieldnames = [key for key in results[0].keys()]
        return render_template('Repair.html', results=results, fieldnames=fieldnames, i=i,len=len)



@app.route('/Installation_ICU', methods=['GET', 'POST'])
def Installation_ICU():
    if request.method == 'GET':
        return render_template('Installation.html')

    elif request.method == 'POST':

        i=["0","0","0","0","inventory number","0","Installation Date"]
        search = request.form.get('search')
        results = []
        user_csv = open("ICU.csv")
        reader = csv.DictReader(user_csv)
        for row in reader:
            results.append(dict(row))
        fieldnames = [key for key in results[0].keys()]
        return render_template('Installation.html', results=results, fieldnames=fieldnames, i=i,len=len)



@app.route('/Repair_Cardiology', methods=['GET', 'POST'])
def Repair_Cardiology():
    if request.method == 'GET':
        return render_template('Repair.html')

    elif request.method == 'POST':

        i=["0","0","0","0","inventory number","0","0","0","0","0","0","0","cause of fault","fault description","Technician name","start date of job order","Action taken"]
       
        search = request.form.get('search')
        results = []
        user_csv = open("Cardiology.csv")
        reader = csv.DictReader(user_csv)
        for row in reader:
            results.append(dict(row))
        fieldnames = [key for key in results[0].keys()]
        return render_template('Repair.html', results=results, fieldnames=fieldnames, i=i,len=len)



@app.route('/Installation_Cardiology', methods=['GET', 'POST'])
def Installation_Cardiology():
    if request.method == 'GET':
        return render_template('Installation.html')

    elif request.method == 'POST':

        i=["0","0","0","0","inventory number","0","Installation Date"]
        search = request.form.get('search')
        results = []
        user_csv = open("Cardiology.csv")
        reader = csv.DictReader(user_csv)
        for row in reader:
            results.append(dict(row))
        fieldnames = [key for key in results[0].keys()]
        return render_template('Installation.html', results=results, fieldnames=fieldnames,i=i, len=len)



@app.route('/OR', methods=['GET', 'POST'])
def OR():
    if request.method == 'GET':
        return render_template('OR.html')

    elif request.method == 'POST':

        i=["0","0","0","0","inventory number","0","0","0","0","0","0","0","cause of fault","fault description","Technician name","start date of job order","Action taken"]
       
        search = request.form.get('search')
        results = []
        user_csv = open("OR.csv")
        reader = csv.DictReader(user_csv)
        for row in reader:
            results.append(dict(row))
        fieldnames = [key for key in results[0].keys()]
        return render_template('OR.html', results=results, fieldnames=fieldnames, len=len)


@app.route('/ICU', methods=['GET', 'POST'])
def ICU():
    if request.method == 'GET':
        return render_template('ICU.html')

    elif request.method == 'POST':

        search = request.form.get('search')
        results = []
        user_csv = open("ICU.csv")
        reader = csv.DictReader(user_csv)
        for row in reader:
            results.append(dict(row))
        fieldnames = [key for key in results[0].keys()]
        return render_template('ICU.html', results=results, fieldnames=fieldnames, len=len)

@app.route('/Cardiology', methods=['GET', 'POST'])
def Cardiology():
    if request.method == 'GET':
        return render_template('Cardiology.html')

    elif request.method == 'POST':

        search = request.form.get('search')
        results = []
        user_csv = open("Cardiology.csv")
        reader = csv.DictReader(user_csv)
        for row in reader:
            results.append(dict(row))
        fieldnames = [key for key in results[0].keys()]
        return render_template('Cardiology.html', results=results, fieldnames=fieldnames, len=len)



###################################################################################################
@app.route("/Home",methods=['GET', 'POST'])
def Home():
    if request.method == 'GET':
        return render_template('home.html')

    elif request.method == 'POST':

        search = request.form.get('search')
        results = []
        user_csv = open("proxies.csv")
        reader = csv.DictReader(user_csv)
        for row in reader:
            results.append(dict(row))
        fieldnames = [key for key in results[0].keys()]
        return render_template('home.html', results=results, fieldnames=fieldnames, len=len)




####################################################################################################

@app.route("/register", methods=['GET', 'POST'])
def register():
    global i
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    form = RegistrationForm()
    if form.validate_on_submit():

        pop=pd.read_csv(r"C:\Users\DELL\Desktop\asas\07-User-Account-Profile-Pic\proxies.csv")

        m=str(pop.iloc[:,0].max()+1)
        
        user = User(id=m,Nomenclature=form.Nomenclature.data, Manufacturer=form.Manufacturer.data,Agent=form.Agent.data,
            inventory_number=form.inventory_number.data,Serial_number=form.Serial_number.data,Installation_Date=form.Installation_Date.data
            ,Operation=form.Operation.data,Location=form.Location.data,
            warrantly_period=form.warrantly_period.data,Contact_data_of_manufacturer=form.Contact_data_of_manufacturer.data
            ,Department=form.Department.data,    
            cause_of_fault=form.cause_of_fault.data
            ,fault_description=form.fault_description.data,Technician_name=form.Technician_name.data,
            start_date_of_job_order=form.start_date_of_job_order.data,
            Action_taken=form.Action_taken.data
            ,predictive_maintenance_Scheduling=form.predictive_maintenance_Scheduling.data
            ,Price=form.Price.data)

        db.session.add(user)
        db.session.commit()


        to_append = f'{str(m)}{","}{form.Nomenclature.data}{","}{form.Manufacturer.data}{","}{form.Agent.data}{","}{form.inventory_number.data}{","}{form.Serial_number.data}{","}{form.Installation_Date.data}{","}{form.Operation.data}{","}{form.Location.data}{","}{form.warrantly_period.data}{","}{form.Contact_data_of_manufacturer.data}{","}{form.Department.data}{","}{form.cause_of_fault.data}{","}{form.fault_description.data}{","}{form.Technician_name.data}{","}{form.start_date_of_job_order.data}{","}{form.Action_taken.data}{","}{form.predictive_maintenance_Scheduling.data}{","}{form.Price.data}  '    
        i=i+1
        #####################################   ALL     ##########################
        file = open('proxies.csv', 'a', newline='')
        with file:
            writer = csv.writer(file,skipinitialspace=True)
            writer.writerow(to_append.split(","))

        
        ##################################     ICU    #############################
        if form.Department.data== "Neonatal":
            file = open('ICU.csv', 'a', newline='')
            with file:
                writer = csv.writer(file,skipinitialspace=True)
                writer.writerow(to_append.split(","))
           
        ##################################  OR  #########################

        if form.Department.data== "OR":
            file = open('OR.csv', 'a', newline='')
            with file:
                writer = csv.writer(file,skipinitialspace=True)
                writer.writerow(to_append.split(","))
        
        ###########################    Cardiology ###################

        if form.Department.data== "Radiology":
            file = open('Cardiology.csv', 'a', newline='')
            with file:
                writer = csv.writer(file,skipinitialspace=True)
                writer.writerow(to_append.split(","))

        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)


#####################################################


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(Nomenclature=form.Nomenclature.data).first()
        if user :
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Home'))
        else:
            flash('Login Unsuccessful. Please check Nomenclature', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('Home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn



@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.Nomenclature = form.Nomenclature.data
        current_user.Manufacturer = form.Manufacturer.data
        current_user.Agent = form.Agent.data
        current_user.inventory_number = form.inventory_number.data
        current_user.Serial_number = form.Serial_number.data
        current_user.Installation_Date = form.Installation_Date.data
        current_user.Operation = form.Operation.data
        current_user.Location = form.Location.data
        current_user.warrantly_period = form.warrantly_period.data
        current_user.Contact_data_of_manufacturer = form.Contact_data_of_manufacturer.data
        current_user.Department = form.Department.data
        current_user.cause_of_fault = form.cause_of_fault.data
        current_user.fault_description = form.fault_description.data
        current_user.Technician_name = form.Technician_name.data
        current_user.start_date_of_job_order = form.start_date_of_job_order.data
        current_user.Action_taken = form.Action_taken.data
        current_user.predictive_maintenance_Scheduling = form.predictive_maintenance_Scheduling.data
        current_user.Price = form.Price.data
        
        p=str(current_user.id)

        User.query.filter_by(Nomenclature=form.Nomenclature.data).delete()
        user = User(id=p,Nomenclature=form.Nomenclature.data, Manufacturer=form.Manufacturer.data,Agent=form.Agent.data,
            inventory_number=form.inventory_number.data,Serial_number=form.Serial_number.data,Installation_Date=form.Installation_Date.data
            ,Operation=form.Operation.data,Location=form.Location.data,
            warrantly_period=form.warrantly_period.data,Contact_data_of_manufacturer=form.Contact_data_of_manufacturer.data
            ,Department=form.Department.data,    
            cause_of_fault=form.cause_of_fault.data
            ,fault_description=form.fault_description.data,Technician_name=form.Technician_name.data,
            start_date_of_job_order=form.start_date_of_job_order.data,
            Action_taken=form.Action_taken.data
            ,predictive_maintenance_Scheduling=form.predictive_maintenance_Scheduling.data
            ,Price=form.Price.data)
        db.session.add(user)
        db.session.commit()




        to_append = f'{current_user.id}{","}{form.Nomenclature.data}{","}{form.Manufacturer.data}{","}{form.Agent.data}{","}{form.inventory_number.data}{","}{form.Serial_number.data}{","}{form.Installation_Date.data}{","}{form.Operation.data}{","}{form.Location.data}{","}{form.warrantly_period.data}{","}{form.Contact_data_of_manufacturer.data}{","}{form.Department.data}{","}{form.cause_of_fault.data}{","}{form.fault_description.data}{","}{form.Technician_name.data}{","}{form.start_date_of_job_order.data}{","}{form.Action_taken.data}{","}{form.predictive_maintenance_Scheduling.data}{","}{form.Price.data}  '    
        file = open('proxies.csv', 'a', newline='')
        with file:

            writer = csv.writer(file,skipinitialspace=True)
            writer.writerow(to_append.split(","))
        


        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.Nomenclature.data = current_user.Nomenclature
        form.Manufacturer.data = current_user.Manufacturer
        form.Agent.data = current_user.Agent
        form.inventory_number.data = current_user.inventory_number
        form.Serial_number.data = current_user.Serial_number
        form.Installation_Date.data = current_user.Installation_Date
        form.Operation.data = current_user.Operation
        form.Location.data = current_user.Location
        
        form.warrantly_period.data = current_user.warrantly_period
        form.Contact_data_of_manufacturer.data = current_user.Contact_data_of_manufacturer
        
        form.Department.data = current_user.Department
        
        form.cause_of_fault.data = current_user.cause_of_fault
        form.fault_description.data = current_user.fault_description
        form.Technician_name.data = current_user.Technician_name
        form.Action_taken.data = current_user.Action_taken
        form.predictive_maintenance_Scheduling.data = current_user.predictive_maintenance_Scheduling
        form.start_date_of_job_order.data = current_user.start_date_of_job_order
        form.Price.data = current_user.Price



    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)




@app.route("/calender")
def calender():
    
    return render_template('calender.html')
