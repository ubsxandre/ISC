from flask import render_template, request, redirect, url_for, flash
from app_iscs.home import app_home, controller_home, model_home
from jinja2 import TemplateNotFound
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.utils import secure_filename
import os, asyncio
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
async def uploadShopeeTokopedia():
    v_tahun_pelaporan = request.form.get('tahun_pelaporan')
    v_bulan_pelaporan = request.form.get('bulan_pelaporan')
    v_olshop = request.form.get('olshop')
    v_created_by = current_user.nama
    # print('View v_tahun_pelaporan : ', request.form.get('tahun_pelaporan'))
    # print('View v_bulan_pelaporan : ', request.form.get('bulan_pelaporan'))
    # print('View v_olshop : ', request.form.get('olshop'))
    controller_home.uploadExcelShopeeTokopedia()
    await asyncio.sleep(1)    
    if v_olshop == 'SHOPEE':
      print('View - insert shopee')
      controller_home.insertDbExcelShopee(v_tahun_pelaporan, v_bulan_pelaporan, v_created_by)
      return redirect(url_for('app_home.home')) 
    elif v_olshop == 'TOKOPEDIA':
      print('View - insert tokopedia')
      controller_home.insertDbExcelTokopedia(v_tahun_pelaporan, v_bulan_pelaporan, v_created_by)
      return redirect(url_for('app_home.home'))
    else:
      print('View - else')
    return redirect(url_for('app_home.home'))
  
@app_home.route('/dashboard', methods=['POST', 'GET'])   # Reading data from CSV and save to mysql using sqlalchemy
def dashboard():
  v_tahun_pelaporan = request.form.get('tahun_pelaporan')
  v_bulan_pelaporan = request.form.get('bulan_pelaporan')
  controller_home.readDbShopeeTokopedia(v_tahun_pelaporan, v_bulan_pelaporan)
  # produk, perwaktu1, allcollabs = controller_home.readExcelShopeeTokopedia()
  # print(produk, perwaktu1, allcollabs)
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