from multiprocessing import current_process
from flask import json, jsonify, request, flash, redirect, Response, send_file, url_for
import os, datetime, csv, io, pandas as pd, numpy as np, plotly.express as px
from io import TextIOWrapper, BytesIO
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.utils import secure_filename
import os
from app_iscs import *
from app_iscs.home import model_home

def uploadExcelShopeeTokopedia():
  v_tahun_laporan = request.form.get('tahun_pelaporan')
  v_bulan_laporan = request.form.get('bulan_pelaporan')
  v_olshop = request.form.get('olshop')
  print('v_tahun_laporan', v_tahun_laporan)
  print('v_bulan_laporan', v_bulan_laporan)
  print(v_olshop)
  cek_data_shopee = db.session.query(model_home.tabel_upload_excel).filter_by(tahun_pelaporan=v_tahun_laporan, bulan_pelaporan=v_bulan_laporan, olshop='SHOPEE', status_aktif=1).first()
  cek_data_tokopedia = db.session.query(model_home.tabel_upload_excel).filter_by(tahun_pelaporan=v_tahun_laporan, bulan_pelaporan=v_bulan_laporan, olshop='TOKOPEDIA', status_aktif=1).first()
  print('cek_data_shopee', cek_data_shopee)
  print('cek_data_tokopedia', cek_data_tokopedia)
  if not cek_data_shopee and request.form.get('olshop') == 'SHOPEE':
    datetime_now = datetime.datetime.now()
    file = request.files['upload_excel']
    olshop = request.form.get('olshop')
    bulan_pelaporan = request.form.get('bulan_pelaporan')
    tahun_pelaporan = request.form.get('tahun_pelaporan')
    created_by = current_user.nama
    created_date = datetime_now
    status_aktif = 1
    
    # SAVE DATA JIKA ADA FOLDER
    if request.files and allowed_file(file.filename):
      date = str(datetime.datetime.now())
      # print('DATE : ', date)
      if file.filename.rsplit('.', 1)[1].lower() == 'xlsx':
        file.filename = olshop + "_"+tahun_pelaporan + "-"+ bulan_pelaporan + "_" + date +".xlsx"
      elif file.filename.rsplit('.', 1)[1].lower() == 'jpg':
        file.filename = olshop + "_"+tahun_pelaporan + "-"+ bulan_pelaporan + "_" + date +".jpg"
      elif file.filename.rsplit('.', 1)[1].lower() == 'jpeg':
        file.filename = olshop + "_"+tahun_pelaporan + "-"+ bulan_pelaporan + "_" + date +".jpeg"
      elif file.filename.rsplit('.', 1)[1].lower() == 'png':
        file.filename = olshop + "_"+tahun_pelaporan + "-"+ bulan_pelaporan + "_" + date +".png"
      files = secure_filename(file.filename)
      
      
      # ADD FOLDER BARU
      folder_path = os.path.join(current_working_directory, 'read_excel')
      CEK_FOLDER_FILES = os.path.exists(folder_path)
      
      # CEK FOLDER IF EXISTS
      if not CEK_FOLDER_FILES:
        os.makedirs(folder_path)
      filefolder = os.path.join(folder_path, files)
      file.save(filefolder)
      data_tabel_upload_excel = model_home.tabel_upload_excel(
        file=files,
        olshop=olshop,
        bulan_pelaporan=bulan_pelaporan,
        tahun_pelaporan=tahun_pelaporan,
        created_by=created_by,
        created_date=created_date,
        status_aktif=status_aktif
      )
      db.session.add(data_tabel_upload_excel)    
      db.session.commit()
      db.session.close()
      return flash("Berhasil Request Data !!!", 'success')
      # flash('Nyimpen data + onok file e', 'success')
      
    # ADD FORM IF FILE KOSONG (TAPI GA DI GAWE , DI GAWE ENGKOK LEK ONOK KASUS DATA BOLEH KOSONG)
    elif file.filename == '':
      return flash('Ga onok file e tapi tetep nyimpen', 'success')
    
    # FORMAT GA SESUAI
    else:
      return flash('Format Tidak di dukung', 'warning')
      # return redirect(request.url + '#request')
  elif not cek_data_tokopedia and request.form.get('olshop') == 'TOKOPEDIA':
    datetime_now = datetime.datetime.now()
    file = request.files['upload_excel']
    olshop = request.form.get('olshop')
    bulan_pelaporan = request.form.get('bulan_pelaporan')
    tahun_pelaporan = request.form.get('tahun_pelaporan')
    created_by = current_user.nama
    created_date = datetime_now
    status_aktif = 1
    
    # SAVE DATA JIKA ADA FOLDER
    if request.files and allowed_file(file.filename):
      date = str(datetime.datetime.now())
      # print('DATE : ', date)
      if file.filename.rsplit('.', 1)[1].lower() == 'xlsx':
        file.filename = olshop + "_"+tahun_pelaporan + "-"+ bulan_pelaporan + "_" + date +".xlsx"
      elif file.filename.rsplit('.', 1)[1].lower() == 'jpg':
        file.filename = olshop + "_"+tahun_pelaporan + "-"+ bulan_pelaporan + "_" + date +".jpg"
      elif file.filename.rsplit('.', 1)[1].lower() == 'jpeg':
        file.filename = olshop + "_"+tahun_pelaporan + "-"+ bulan_pelaporan + "_" + date +".jpeg"
      elif file.filename.rsplit('.', 1)[1].lower() == 'png':
        file.filename = olshop + "_"+tahun_pelaporan + "-"+ bulan_pelaporan + "_" + date +".png"
      files = secure_filename(file.filename)
      
      
      # ADD FOLDER BARU
      folder_path = os.path.join(current_working_directory, 'read_excel')
      CEK_FOLDER_FILES = os.path.exists(folder_path)
      
      # CEK FOLDER IF EXISTS
      if not CEK_FOLDER_FILES:
        os.makedirs(folder_path)
      filefolder = os.path.join(folder_path, files)
      file.save(filefolder)
      data_tabel_upload_excel = model_home.tabel_upload_excel(
        file=files,
        olshop=olshop,
        bulan_pelaporan=bulan_pelaporan,
        tahun_pelaporan=tahun_pelaporan,
        created_by=created_by,
        created_date=created_date,
        status_aktif=status_aktif
      )
      db.session.add(data_tabel_upload_excel)    
      db.session.commit()
      db.session.close()
      return flash("Berhasil Request Data !!!", 'success')
      # flash('Nyimpen data + onok file e', 'success')
      
    # ADD FORM IF FILE KOSONG (TAPI GA DI GAWE , DI GAWE ENGKOK LEK ONOK KASUS DATA BOLEH KOSONG)
    elif file.filename == '':
      return flash('Ga onok file e tapi tetep nyimpen', 'success')
    
    # FORMAT GA SESUAI
    else:
      return flash('Format Tidak di dukung', 'warning')
      # return redirect(request.url + '#request')
  elif cek_data_tokopedia :
    return flash('File Tokopedia bulan tsb SUDAH pernah di upload !!', 'warning')
  elif cek_data_shopee:
    return flash('File Shopee bulan tsb SUDAH pernah di upload !!', 'warning')
  else:
    return flash('MBOHHHH')
    
    
def readExcelShopeeTokopedia():
  if request.method == 'POST':
    v_tahun_laporan = request.form.get('tahun_pelaporan')
    v_bulan_laporan = request.form.get('bulan_pelaporan')
    print('read v_tahun_laporan', v_tahun_laporan)
    print('read v_bulan_laporan', v_bulan_laporan)
    cek_data_shopee = db.session.query(model_home.tabel_upload_excel).filter_by(tahun_pelaporan=v_tahun_laporan, bulan_pelaporan=v_bulan_laporan, olshop='SHOPEE', status_aktif=1).first()
    cek_data_tokopedia = db.session.query(model_home.tabel_upload_excel).filter_by(tahun_pelaporan=v_tahun_laporan, bulan_pelaporan=v_bulan_laporan, olshop='TOKOPEDIA', status_aktif=1).first()
    # print('cek_data_tokopedia', cek_data_shopee.file)
    # print('cek_data_tokopedia', cek_data_tokopedia['file'])
    if cek_data_shopee and cek_data_tokopedia:
      print('Shopee x Tokopedia')
      folder_path = os.path.join(current_working_directory, 'read_excel')
      path_excel_shopee = os.path.join(folder_path, cek_data_shopee.file)
      path_excel_tokopedia = os.path.join(folder_path, cek_data_tokopedia.file)
      
      shopee = pd.read_excel(path_excel_shopee, engine='openpyxl')
      tokopedia = pd.read_excel(path_excel_tokopedia, engine='openpyxl')
      
      tokopedia=tokopedia.fillna(method="ffill") # Data yang kosong diisi dengan data sebelumnya.
      tokopedia=tokopedia.drop(columns=['Tipe Produk', 'Diskon Produk (IDR)','Bebas Ongkir'], axis=1) # Gawe template

#           # Mengambil Variabel yang digunakan
      shopee = shopee[["Waktu Pesanan Dibuat","Status Pesanan","Nama Produk","Nomor Referensi SKU","Harga Awal","Jumlah","Username (Pembeli)","Kota/Kabupaten","Provinsi"]]
      tokopedia = tokopedia[["Tanggal Pembayaran","Status Terakhir","Nama Produk","Nomor SKU","Harga Awal (IDR)","Jumlah Produk Dibeli","Nama Pembeli","Kota","Provinsi"]]
      shopee['Jenis Baru'] = shopee['Nomor Referensi SKU'].str.split('-').str[0].str.strip()
      tokopedia['Jenis Baru'] = tokopedia['Nomor SKU'].str.split('-').str[0].str.strip() # Mengambil value sebelum -
      tokopedia['tiga huruf pertama']=tokopedia['Nomor SKU'].str[:3] # Diambil huruf 3 pertama 
      shopee['tiga huruf pertama']=shopee['Nomor Referensi SKU'].str[:3]
      
      v_delete_yak = shopee[shopee["tiga huruf pertama"] == 'YAK'].count()
      v_delete_sj1 = shopee[shopee["tiga huruf pertama"] == 'SJ1'].count()
      v_delete_yak = v_delete_yak["tiga huruf pertama"]
      v_delete_sj1 = v_delete_sj1["tiga huruf pertama"]
          # DATA CLEANSING
      mkt_with_index=shopee.set_index("tiga huruf pertama")
      if v_delete_yak >= 1 and v_delete_sj1 >= 1:
        shopee= mkt_with_index.drop(['YAK', 'SJ1'], axis=0, inplace=True)
        shopee=mkt_with_index.reset_index(drop=True)
      elif v_delete_yak >= 1:
        shopee=mkt_with_index.drop(['YAK'], axis=0, inplace=True)
        shopee=mkt_with_index.reset_index(drop=True)
      elif v_delete_sj1 >= 1:
        shopee=mkt_with_index.drop(['SJ1'], axis=0, inplace=True)
        shopee=mkt_with_index.reset_index(drop=True)
      else:
        shopee=shopee.drop(columns=['tiga huruf pertama'])
        
      # shopee['Harga Awal']=shopee['Harga Awal'].str.replace('Rp','').str.replace('.','').astype(int)
      
      v_delete_yak_tokopedia = tokopedia[tokopedia["tiga huruf pertama"] == 'YAK'].count()
      v_delete_sj1_tokopedia = tokopedia[tokopedia["tiga huruf pertama"] == 'SJ1'].count()
      v_delete_yak_tokopedia = v_delete_yak_tokopedia["tiga huruf pertama"]
      v_delete_sj1_tokopedia = v_delete_sj1_tokopedia["tiga huruf pertama"]
      print('v_delete_yak_tokopedia : ', v_delete_yak_tokopedia)
      print('v_delete_sj1_tokopedia : ', v_delete_sj1_tokopedia)
      mkt_with_index_tokopedia = tokopedia.set_index("tiga huruf pertama")
      if v_delete_yak_tokopedia >= 1 and v_delete_sj1_tokopedia >= 1:
        tokopedia=mkt_with_index_tokopedia.drop(['YAK', 'SJ1'], axis=0, inplace=True)
        tokopedia=mkt_with_index_tokopedia.reset_index(drop=True)
      elif v_delete_yak_tokopedia >= 1 and v_delete_sj1_tokopedia < 1:
        tokopedia=mkt_with_index_tokopedia.drop(['YAK'], axis=0, inplace=True)
        tokopedia=mkt_with_index_tokopedia.reset_index(drop=True)
      elif v_delete_yak_tokopedia < 1 and v_delete_sj1_tokopedia >= 1:
        tokopedia=mkt_with_index_tokopedia.drop(['SJ1'], axis=0, inplace=True)
        tokopedia.mkt_with_index_tokopedia.reset_index(drop=True)
      else:
        tokopedia=tokopedia.drop(columns=['tiga huruf pertama'])
      tokopedia=tokopedia.rename(columns = {"Tanggal Pembayaran": "Waktu Pesanan Dibuat",
                     "Status Terakhir":"Status Pesanan", "Nomor SKU":"Nomor Referensi SKU", "Harga Awal (IDR)":"Harga Awal",
                        "Jumlah Produk Dibeli":"Jumlah", "Nama Pembeli":"Username (Pembeli)", "Kota":"Kota/Kabupaten"})
      
      mkt=pd.concat([shopee, tokopedia])
          # Hanya digunakan yang pesanan selesai
      mkt=mkt.loc[mkt['Status Pesanan'].isin(['Pesanan Selesai','Selesai'] )]
      
      dua = pd.to_datetime(mkt['Waktu Pesanan Dibuat']).dt.hour.map(str).str.zfill(2)
      tiga = pd.to_datetime(mkt['Waktu Pesanan Dibuat']).dt.minute.map(str).str.zfill(2)
      empat = dua+tiga
      mkt['Waktu New'] = empat.map(int)
      conditions =[
          (mkt['Waktu New'] >= 1) & (mkt['Waktu New'] <= 100), 
          (mkt['Waktu New'] >= 101) & (mkt['Waktu New'] <= 200), 
          (mkt['Waktu New'] >= 201) & (mkt['Waktu New'] <= 300), 
          (mkt['Waktu New'] >= 301) & (mkt['Waktu New'] <= 400), 
          (mkt['Waktu New'] >= 401) & (mkt['Waktu New'] <= 500), 
          (mkt['Waktu New'] >= 501) & (mkt['Waktu New'] <= 600), 
          (mkt['Waktu New'] >= 601) & (mkt['Waktu New'] <= 700), 
          (mkt['Waktu New'] >= 701) & (mkt['Waktu New'] <= 800),
          (mkt['Waktu New'] >= 801) & (mkt['Waktu New'] <= 900),
          (mkt['Waktu New'] >= 901) & (mkt['Waktu New'] <= 1000),
          (mkt['Waktu New'] >= 1001) & (mkt['Waktu New'] <= 1100),
          (mkt['Waktu New'] >= 1101) & (mkt['Waktu New'] <= 1200),
          (mkt['Waktu New'] >= 1201) & (mkt['Waktu New'] <= 1300), 
          (mkt['Waktu New'] >= 1301) & (mkt['Waktu New'] <= 1400), 
          (mkt['Waktu New'] >= 1401) & (mkt['Waktu New'] <= 1500), 
          (mkt['Waktu New'] >= 1501) & (mkt['Waktu New'] <= 1600), 
          (mkt['Waktu New'] >= 1601) & (mkt['Waktu New'] <= 1700), 
          (mkt['Waktu New'] >= 1701) & (mkt['Waktu New'] <= 1800), 
          (mkt['Waktu New'] >= 1801) & (mkt['Waktu New'] <= 1900), 
          (mkt['Waktu New'] >= 1901) & (mkt['Waktu New'] <= 2000),
          (mkt['Waktu New'] >= 2001) & (mkt['Waktu New'] <= 2100),
          (mkt['Waktu New'] >= 2101) & (mkt['Waktu New'] <= 2200),
          (mkt['Waktu New'] >= 2201) & (mkt['Waktu New'] <= 2300),
          (mkt['Waktu New'] >= 2301) & (mkt['Waktu New'] <= 2359),
          (mkt['Waktu New'] ==0)
      ]

      letters = ['00:01-01:00', '01:01-02:00', '02:01-03:00', '03:01-04:00', '04:01-05:00','05:01-06:00','06:01-07:00','07:01-08:00','08:00-09:00','09:01-10:00',
                '10:01-11:00','11:01-12:00', '12:01-13:00', '13:01-14:00', '14:01-15:00', '15:01-16:00','16:01-17:00','17:01-18:00','18:01-19:00','19:01-20:00',
                '20:01-21:00','21:01-22:00', '22:01-23:00', '23:01-00:00', '23:01-00:00']
      mkt['Kategori Waktu'] = np.select(conditions, letters)  
          # PENENTUAN BULAN
      # lima = pd.to_datetime(mkt['Waktu Pesanan Dibuat'])
      enam = pd.to_datetime(mkt['Waktu Pesanan Dibuat']).dt.month.map(str).str.zfill(2)
      mkt['kode bulan'] = enam.map(int) 
      conditions =[
          (mkt['kode bulan'] == 1),
          (mkt['kode bulan'] == 2),
          (mkt['kode bulan'] == 3),
          (mkt['kode bulan'] == 4),
          (mkt['kode bulan'] == 5),
          (mkt['kode bulan'] == 6),
          (mkt['kode bulan'] == 7),
          (mkt['kode bulan'] == 8),
          (mkt['kode bulan'] == 9),
          (mkt['kode bulan'] == 10),
          (mkt['kode bulan'] == 11),
          (mkt['kode bulan'] == 12),
      ]

      letters = ['Januari', 'Februari', 'Maret', 'April', 'Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
      mkt['Bulan'] = np.select(conditions, letters)  
      mkt['Kode 1']=mkt['Jenis Baru'].str[1:2].str.upper()
      ab1=mkt['Jenis Baru'].str[2].str.upper()
          # PENENTUAN JENIS PRODUK
      mkt['Kode 2']= np.where(np.logical_or(np.logical_or(mkt['Kode 1'] == 'D',mkt['Kode 1']=='S'),mkt['Kode 1']=='H'), ab1, mkt['Kode 1'])
          # Jika "Kode 1" nya D / S / H maka diganti ab1 (Huruf ke 3 dari "Kode 1")
      conditions =[
          (mkt['Kode 2']=='C'), 
          (mkt['Kode 2']=='A'),
          (mkt['Kode 2']=='B'),
          (mkt['Kode 2']=='G'),
          (mkt['Kode 2']=='K'),
          (mkt['Kode 2']=='L'),
          (mkt['Kode 2']=='M'),
          (mkt['Kode 2']=='N'),
          (mkt['Kode 2']=='W'),
      ]
      letters = ['Cincin','Anting','Bross','Gelang','Kalung','Liontin','Mainan','LM','Giwang']
      mkt['Jenis Produk'] = np.select(conditions, letters)
      conditions =[
          (mkt['Jenis Produk'] == 'Anting') |(mkt['Jenis Produk'] == 'Bross')|(mkt['Jenis Produk'] == 'Cincin')|(mkt['Jenis Produk'] == 'Gelang')|(mkt['Jenis Produk'] == 'Giwang')|(mkt['Jenis Produk'] == 'Kalung')|(mkt['Jenis Produk'] == 'Liontin')|(mkt['Jenis Produk'] == 'Mainan') ,
          (mkt['Jenis Produk'] == 'LM')
      ]   
      letters = ['Perhiasan','LM']
      mkt['Kategori Produk'] = np.select(conditions, letters)
      mkt['Kode 3']= ab1
      produk=mkt.groupby(['Jenis Produk'])['Jumlah'].sum().reset_index()
      fig = px.pie(produk, values='Jumlah', names='Jenis Produk', title='Persentase Penjualan ALL Produk',color_discrete_sequence=px.colors.sequential.RdBu)
          # Kurang nampilke neng dashboard
    elif not cek_data_tokopedia:
      return flash('File Tokopedia bulan tsb BELUM pernah di upload !!', 'warning')
    elif not cek_data_shopee:
      return flash('File Shopee bulan tsb BELUM pernah di upload !!', 'warning')
    else:
      return flash('MBOHHHH')
  return 'Bukan method post'