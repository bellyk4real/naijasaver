from flask import Blueprint

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/')
def home():
    return 'Naijasaver saves you cash'