from django.shortcuts import render
from flask import render_template, request, redirect, url_for
from app_iscs.tabel import app_tabel, controller_tabel, model_tabel
from app_iscs.home import controller_home, model_home
from jinja2 import TemplateNotFound
from flask_login import login_user, login_required, current_user, logout_user


@app_tabel.route('/tabel-upload')
@login_required
def tabelUpload():
  data_tabel_upload = controller_tabel.tabel_shopee_tokped();
  return render_template('tabel/tabel-upload.html', data_tabel_upload=data_tabel_upload)

@app_tabel.route('/upload-shopee-tokopedia', methods=['POST', 'GET'])   # Reading data from CSV and save to mysql using sqlalchemy
# Get the uploaded files
def uploadShopeeTokopedia():
    controller_home.readExcel()
  # # print('Upload SHopee : ', controller_tabel.readFileName(request.files['file'].filename)[0:6])
  # if request.method == 'POST' and controller_tabel.readFileName(request.files['file'].filename)[0:6] == 'Shopee' and (controller_tabel.readFileExt(request.files['file'].filename) == '.xls' or controller_tabel.readFileExt(request.files['file'].filename) == '.xlsx'):
  #   print('Upload Shopee IF Shopee')
  #   return controller_tabel.uploadfileShopee_excel()
  # elif request.method == 'POST' and controller_tabel.readFileName(request.files['file'].filename)[0:9] == 'Tokopedia' and (controller_tabel.readFileExt(request.files['file'].filename) == '.xls' or controller_tabel.readFileExt(request.files['file'].filename) == '.xlsx'):
  #   print('Upload Shopee IF Tokopedia')
  #   return controller_tabel.uploadfileTokopedia_excel()
  # else:
  #   print('Upload Shopee MBOOOHHH')
  # # if request.method == 'POST' and controller_rusak_reparasi.readFileExt(request.files['file'].filename) == '.csv':
  # #   return controller_rusak_reparasi.uploadfilesRusakReparasi_csv()
  # # elif request.method == 'POST' and controller_rusak_reparasi.readFileExt(request.files['file'].filename) == '.xls':
  # #   return controller_rusak_reparasi.uploadfilesRusakReparasi_excel()
  # # elif request.method == 'POST' and (controller_rusak_reparasi.readFileExt(request.files['file'].filename) != '.csv' or controller_rusak_reparasi.readFileExt(request.files['file'].filename) != '.xls'):
  # #   return render_template('/elo/zzz_upload-hollow-elo.html') 
  # # return redirect(url_for('tabelUpload.tabel-upload'))
    return redirect(url_for('app_tabel.tabelUpload'))