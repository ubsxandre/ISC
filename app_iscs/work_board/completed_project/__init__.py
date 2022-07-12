# add views (endpoints) 
from flask import Blueprint

app_completed_project = Blueprint('app_completed_project', __name__, template_folder='templates', static_folder='static')

from app_iscs.work_board.completed_project import view_completed_project