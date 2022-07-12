from flask import render_template, request, redirect, url_for, flash
from app_iscs.home import app_home, controller_home, model_home
from jinja2 import TemplateNotFound
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.utils import secure_filename
import os
from app_iscs import *
  
@app_home.route('/home', methods=['POST', 'GET'])
@login_required
def home():
  if request.method == 'POST':    
    controller_home.formRequest()
    return redirect(request.url + '#request')
    # return render_template('home/index.html')  
  return render_template('home/index.html')


@app_home.route('/upload-shopee-tokopedia', methods=['POST', 'GET'])   # Reading data from CSV and save to mysql using sqlalchemy
# Get the uploaded files
def uploadShopeeTokopedia():
    controller_home.uploadExcelShopeeTokopedia()
    return redirect(url_for('app_home.home'))
  
@app_home.route('/read-excel-shopee-tokopedia', methods=['POST', 'GET'])   # Reading data from CSV and save to mysql using sqlalchemy
# Get the uploaded files
def readExcelShopeeTokopedia():
    controller_home.readExcelShopeeTokopedia()
    return redirect(url_for('app_home.home'))
  


  
  
  
  
  
  
  
  
  
  


# @app_home.route('/<template>')
# def route_template(template):

#     try:

#         if not template.endswith('.html'):
#             template += '.html'

#         # Detect the current page
#         segment = get_segment(request)

#         # Serve the file (if exists) from app/templates/home/FILE.html
#         return render_template("home/" + template, segment=segment)

#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404

#     except:
#         return render_template('home/page-500.html'), 500


# # Helper - Extract current page name from request
# def get_segment(request):

#     try:

#         segment = request.path.split('/')[-1]

#         if segment == '':
#             segment = 'index'

#         return segment

#     except:
#         return None