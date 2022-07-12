from flask import Blueprint

app_login_init = Blueprint('login', __name__, static_folder='static', template_folder='templates')

from app_iscs.authentication.login import view