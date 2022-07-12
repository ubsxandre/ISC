# add views (endpoints) 
from flask import Blueprint

app_tabel = Blueprint('app_tabel', __name__, template_folder='templates', static_folder='static')

from app_iscs.tabel import view_tabel