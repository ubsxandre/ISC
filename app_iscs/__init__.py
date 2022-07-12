from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from config import DevelopmentConfig

from flask_sqlalchemy import SQLAlchemy

from flask_mysqldb import MySQL
import MySQLdb.cursors

from os.path import join, dirname, realpath
import os

# import extensions instance
db = SQLAlchemy()
migrate = Migrate()
mysql = MySQL()
curMysql = MySQLdb.cursors.DictCursor

# UPLOAD
BASEDIR = os.path.abspath(os.path.dirname(realpath(__file__)))
UPLOAD_FOLDER = os.path.join(BASEDIR, './static/files')
current_working_directory = os.path.join(BASEDIR, UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# END UPLOAD


def app_iscs(config=DevelopmentConfig):
  app = Flask(__name__)
  app.config.from_object(config)
  app.config["DEBUG"] = True 
  app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
  # app.config['UPLOAD_DIRECTORY'] = './static/img/uploads/'
  # app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB
  # app.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.png', '.gif', 'jpeg']
  
  @app.after_request
  def after_request(response):
      response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
      response.headers["Expires"] = 0
      response.headers["Pragma"] = "no-cache"
      return response
  
  app.config['MYSQL_HOST']='localhost'  # dikoneksikan dengan database
  # app.config['MYSQL_HOST']='172.20.140.98'  # dikoneksikan dengan database
  app.config['MYSQL_USER']='root'
  app.config['MYSQL_PASSWORD']='666666'
  # app.config['MYSQL_PASSWORD']=''
  app.config['MYSQL_DB']='isc_db'

  # initialize extension instances
  mysql.init_app(app)
  mysql.app = app

  # initialize extension instances
  db.init_app(app)
  db.app = app
  
  # migrate initialization
  migrate.init_app(app, db)
  migrate.app = app
  
  from app_iscs.authentication.login import model, controller
    
    
  admin = Admin(app, name='Control Panel', template_mode='bootstrap5', index_view=model.DashboardView())
  admin.add_view(model.Controller(model.User, db.session, name='User'))
  # admin.add_view(ModelView(model_elo.m_jenis_kawat, db.session, name='Jenis Kawat'))
  # admin.add_view(ModelView(model_elo.m_diameter_kawat, db.session, name='Diameter Kawat'))
  # admin.add_view(ModelView(model_elo.m_tebal_kawat, db.session, name='Tebal Kawat'))
  # admin.add_view(ModelView(model_elo.m_kadar, db.session, name='Kadar'))
  # admin.add_view(ModelView(model_elo.m_alloy, db.session, name='Alloy'))
  
  login_manager = LoginManager()
  login_manager.init_app(app)  
  login_manager.login_view = 'login.login'
  
  
  from app_iscs.authentication.login import model
  
  @login_manager.user_loader
  def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return model.User.query.get(int(user_id))
  
    
  # ----------register blueprints of applications----------- #
  
  # HOME AWAL
  from app_iscs.authentication.login import app_login_init as login
  app.register_blueprint(login)
  
  # HOME AWAL - Iki mengko diganti dashboard
  from app_iscs.home import app_home as home
  app.register_blueprint(home) 
  
  # FORM SURVEY
  from app_iscs.tabel import app_tabel as tabel
  app.register_blueprint(tabel)
  
  return app 