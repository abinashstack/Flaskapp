from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import forms
from datetime import datetime
from models import Task
from app import app,db




@app.route('/index')#we can have multiple routes and as the route is accessed something is returned
def index():
    task2=Task.query.all()
    return render_template('index2.html',tasks=task2)
# we are calling a get request to /http/127/...etc
# all the html files need to exist in the templates folder
@app.route('/about',methods=['GET',"POST"])
def about():
    form=forms.SubmitForm()
    if form.validate_on_submit():
        task=Task(title=form.title.data,date=datetime.utcnow())
        db.session.add(task)
        db.session.commit()

        return redirect(url_for('index'))#url_for takes a function name

    return render_template('about.html',form=form)
