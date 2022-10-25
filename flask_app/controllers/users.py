from flask_app.models.user import User
from flask import Flask, render_template, redirect, request
from flask_app import app

@app.route('/')
def index():
    return redirect('/users/new')

@app.route('/users/new')
def new_user_form():

    return render_template('create.html')

@app.route('/users')
def show_users():
    all_users = User.show_all()
    return render_template('read_all.html', all_users=all_users)

@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_one_user(user_id):
    data = {
        "id": user_id
    }
    one_user = User.show_one(data)
    return render_template('read_one.html', one_user = one_user[0])

@app.route('/users/<int:user_id>/edit')
def edit_one_user(user_id):
    data = {
        "id" : user_id
    }
    one_user = User.show_one(data)
    return render_template('edit_user.html', one_user = one_user[0])

@app.route('/user_update/<int:id>', methods=['POST'])
def user_update(id):
    data = {
        'id' : id,
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    id = id
    
    User.edit_one(data)
    return show_one_user(id)

@app.route('/users/delete/<int:user_id>')
def delete_one_user(user_id):
    data = {
        'id' : user_id
    }
    
    User.delete_one(data)
    
    return redirect('/users')