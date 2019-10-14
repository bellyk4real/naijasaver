from flask import Blueprint

user = Blueprint('user', __name__)

@user.route('/')
def home():
    return {"message" : 'Naijasaver saves you cash'}

@user.route('/login')
def login():
    return {"message" : 'login details'}