import os
import pymysql
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists,create_database
from os.path import join, dirname, realpath

# # set the base directory
# basedir = os.path.abspath(os.path.dirname(__file__))

# set the base directory
BASEDIR = os.path.abspath(os.path.dirname(realpath(__file__)))

# Set Create Folder
def createFolder(PATH):
    folderPath = os.path.join(BASEDIR, PATH)
    os.makedirs(folderPath)
    
# Auto Create Name DB
def validateDatabase(DATABASE_FILE):
    dbName = str(os.environ.get("DB_DATABASE"))
    dbFile = DATABASE_FILE
    engine = create_engine(dbFile)
    if not database_exists(engine.url): # Checks for the first time  
        create_database(engine.url)     # Create new DB    
        print(str(dbName)+" Database Created") # Verifies if database is there or not.
    else:
        print("Database "+str(dbName)+" Running")

# Create the super class
class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_COMMIT_ON_TEARDOWN = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  # untuk created folder files
  FOLDER_FILES = os.environ.get('FOLDER_FILES')
  CEK_FOLDER_FILES = os.path.exists(FOLDER_FILES)
  if not CEK_FOLDER_FILES:
    createFolder(FOLDER_FILES)
    print('Folder Telah Dibuat')
  

# Create the development config
class DevelopmentConfig(Config):
  DEBUG = True
  
  HOST = str(os.environ.get("DB_HOST"))
  DATABASE = str(os.environ.get("DB_DATABASE"))
  USERNAME = str(os.environ.get("DB_USERNAME"))
  PASSWORD = str(os.environ.get("DB_PASSWORD"))
  
  DATABASE_FILE = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DATABASE
  validateDatabase(DATABASE_FILE)
  SQLALCHEMY_DATABASE_URI = DATABASE_FILE
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_RECORD_QUERIES = True 
  
  

  
  
