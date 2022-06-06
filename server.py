# pipenv install PyMySQL flask
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

from flask_app.models.user import User

@app.route('/')
def index():
    # returns a list of instances
    all_users = User.get_all()
    # User.create()
    return render_template('index.html', all_users=all_users)

@app.route('/allusers')
def all_users():
    all_users = User.get_all()
    return render_template('allusers.html', users=all_users)




@app.route('/user/edit/<int:id>')
def edit_user(id):
    data ={
        "id":id
    }
    return render_template('edituser.html', user=User.get_one(data)) 


@app.route('/user/select/<int:id>')
def select_user(id):
    data ={
        "id":id
    }
    return render_template('selectuser.html', users=User.get_one(data)) 


@app.route('/user/update', methods=['POST'])
def update():
    # can connect to the hidden form to access the id
    User.update(request.form)
    return redirect('/allusers')


@app.route('/user/new')
def new():
    return render_template("index.html")

@app.route('/user/create', methods=['POST'])
def create_user():
    print(request.form)
    User.create(request.form)
    return redirect('/allusers')


@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        "id":id
    }
    User.destroy(data)
    return redirect('/allusers')


if __name__=="__main__":
    app.run(debug=True)