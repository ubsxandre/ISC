from multiprocessing import current_process
from flask import json, jsonify, request, flash, redirect, Response, send_file, url_for
import os, datetime, csv, io, pandas as pd, numpy as np, plotly.express as px, asyncio
from matplotlib.font_manager import json_dump
from io import TextIOWrapper, BytesIO
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.utils import secure_filename
import os
from app_iscs import *
from app_iscs.home import model_home
from app_iscs.tabel import model_tabel

def uploadExcelShopeeTokopedia():
  v_tahun_laporan = request.form.get('tahun_pelaporan')
  v_bulan_laporan = request.form.get('bulan_pelaporan')
  v_olshop = request.form.get('olshop')
  # print('v_tahun_laporan', v_tahun_laporan)
  # print('v_bulan_laporan', v_bulan_laporan)
  # print(v_olshop)
  cek_data_shopee = db.session.query(model_home.tabel_upload_excel).filter_by(tahun_pelaporan=v_tahun_laporan, bulan_pelaporan=v_bulan_laporan, olshop='SHOPEE', status_aktif=1).first()
  cek_data_tokopedia = db.session.query(model_home.tabel_upload_excel).filter_by(tahun_pelaporan=v_tahun_laporan, bulan_pelaporan=v_bulan_laporan, olshop='TOKOPEDIA', status_aktif=1).first()
  # print('cek_data_shopee', cek_data_shopee)
  # print('cek_data_tokopedia', cek_data_tokopedia)
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
      v_berhasil = "Berhasil Upload " + " Shopee !"
      return flash(v_berhasil, 'success')
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
      v_berhasil = "Berhasil Upload " + " Tokopedia !"
      return flash(v_berhasil, 'success')
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
  
  
  
def insertDbExcelShopee(v_tahun_pelaporan, v_bulan_pelaporan, v_created_by):
  cek_data_shopee = db.session.query(model_tabel.tabel_shopee_tokped).filter_by(tahun_pelaporan=v_tahun_pelaporan, bulan_pelaporan=v_bulan_pelaporan, olshop='SHOPEE', status_aktif=1).first()
  nama_file = db.session.query(model_home.tabel_upload_excel).filter_by(tahun_pelaporan=v_tahun_pelaporan, bulan_pelaporan=v_bulan_pelaporan, olshop='SHOPEE', status_aktif=1).first()
  if not cek_data_shopee:   # Jika data shopee belum di insert di tabel tabel_shopee_tokped
    # print('Insert data Shopee tok : ', cek_data_shopee)
    folder_path = os.path.join(current_working_directory, 'read_excel')
    path_excel_shopee = os.path.join(folder_path, nama_file.file)
    # print('Path excel shopee : ', path_excel_shopee)
    if path_excel_shopee: # Jika sudah berhasil di upload
      shopee = pd.read_excel(path_excel_shopee, engine='openpyxl')
          # Mengambil Variabel yang digunakan
      shopee = shopee[["Waktu Pesanan Dibuat","Status Pesanan","Nama Produk","Nomor Referensi SKU","Harga Awal","Jumlah","Username (Pembeli)","Kota/Kabupaten","Provinsi"]]
      shopee['Jenis Baru'] = shopee['Nomor Referensi SKU'].str.split('-').str[0].str.strip()
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
          # DIambil yang pesanan selesai tok
      mkt = shopee.loc[shopee['Status Pesanan'].isin(['Selesai'] )]
      mkt = mkt[mkt['Username (Pembeli)'].notna()]
      
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
      mkt['Kode Bulan'] = enam.map(int) 
      conditions =[
          (mkt['Kode Bulan'] == 1),
          (mkt['Kode Bulan'] == 2),
          (mkt['Kode Bulan'] == 3),
          (mkt['Kode Bulan'] == 4),
          (mkt['Kode Bulan'] == 5),
          (mkt['Kode Bulan'] == 6),
          (mkt['Kode Bulan'] == 7),
          (mkt['Kode Bulan'] == 8),
          (mkt['Kode Bulan'] == 9),
          (mkt['Kode Bulan'] == 10),
          (mkt['Kode Bulan'] == 11),
          (mkt['Kode Bulan'] == 12),
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
    v_created_by = 'UPLOAD ' + v_created_by
    for index, row in mkt.iterrows():
      v_waktu_pesanan_dibuat = datetime.datetime.strptime(row["Waktu Pesanan Dibuat"], "%Y-%m-%d %H:%M") # Uploadan kalau tanggalnya string 2022-03-08 08:29
      v_harga_awal = row["Harga Awal"].replace('Rp ', '').replace('.', '')
      # print(type(sh.cell_value(rowx=row, colx=0)), ' : ', sh.cell_value(rowx=row, colx=0))
      datetime_now = datetime.datetime.now()
      if row["Username (Pembeli)"] == 'nan':
        v_username = ''
      else:
        v_username = row["Username (Pembeli)"]
      insert_shopee_db = model_tabel.tabel_shopee_tokped(waktu_pesanan_dibuat=v_waktu_pesanan_dibuat, status_pesanan=row["Status Pesanan"], 
                      nama_produk=row["Nama Produk"], nomer_referensi_sku=row["Nomor Referensi SKU"], 
                      harga_awal=float(v_harga_awal), jumlah=row["Jumlah"], olshop='SHOPEE',
                      username_pembeli=v_username, kota_kabupaten=row["Kota/Kabupaten"],
                      provinsi=row["Provinsi"], jenis_baru=row["Jenis Baru"],
                      waktu_new=row["Waktu New"], kategori_waktu=row["Kategori Waktu"],
                      kode_bulan=row["Kode Bulan"], bulan=row["Bulan"],
                      kode_1=row["Kode 1"], kode_2=row["Kode 2"], kode_3=row["Kode 3"],
                      jenis_produk=row["Jenis Produk"], kategori_produk=row["Kategori Waktu"],
                      bulan_pelaporan=v_bulan_pelaporan, tahun_pelaporan=v_tahun_pelaporan,
                      created_by=v_created_by, created_date=datetime_now, status_aktif=1,)
      db.session.add(insert_shopee_db)
      db.session.commit()    
      
    return mkt
  elif cek_data_shopee:
    return flash('Data sudah pernah di insert, tidak bisa di insert lagi !')
  else :
    return flash('Data shopee kosong !')      
  # return flash('MBOH ! READ EXCEL SHOPEE ERROR')

  

def insertDbExcelTokopedia(v_tahun_pelaporan, v_bulan_pelaporan, v_created_by):
  cek_data_tokopedia = db.session.query(model_tabel.tabel_shopee_tokped).filter_by(tahun_pelaporan=v_tahun_pelaporan, bulan_pelaporan=v_bulan_pelaporan, olshop='TOKOPEDIA', status_aktif=1).first()
  nama_file = db.session.query(model_home.tabel_upload_excel).filter_by(tahun_pelaporan=v_tahun_pelaporan, bulan_pelaporan=v_bulan_pelaporan, olshop='TOKOPEDIA', status_aktif=1).first()
  if not cek_data_tokopedia:   # Jika data shopee belum di insert di tabel tabel_shopee_tokped
    # print('Insert data Tokopedia tok : ', cek_data_tokopedia)
    folder_path = os.path.join(current_working_directory, 'read_excel')
    path_excel_tokopedia = os.path.join(folder_path, nama_file.file)
    # print('Path excel shopee : ', path_excel_tokopedia)
    if path_excel_tokopedia: # Jika sudah berhasil di upload
      tokopedia = pd.read_excel(path_excel_tokopedia, engine='openpyxl')
      tokopedia=tokopedia.fillna(method="ffill") # Data yang kosong diisi dengan data sebelumnya.
      tokopedia=tokopedia.drop(columns=['Tipe Produk', 'Diskon Produk (IDR)','Bebas Ongkir'], axis=1) # Gawe template
      
      tokopedia = tokopedia[["Tanggal Pembayaran","Status Terakhir","Nama Produk","Nomor SKU","Harga Awal (IDR)","Jumlah Produk Dibeli","Nama Pembeli","Kota","Provinsi"]]
      tokopedia['Jenis Baru'] = tokopedia['Nomor SKU'].str.split('-').str[0].str.strip() # Mengambil value sebelum -
      tokopedia['tiga huruf pertama']=tokopedia['Nomor SKU'].str[:3] # Diambil huruf 3 pertama 
      
      v_delete_yak_tokopedia = tokopedia[tokopedia["tiga huruf pertama"] == 'YAK'].count()
      v_delete_sj1_tokopedia = tokopedia[tokopedia["tiga huruf pertama"] == 'SJ1'].count()
      v_delete_yak_tokopedia = v_delete_yak_tokopedia["tiga huruf pertama"]
      v_delete_sj1_tokopedia = v_delete_sj1_tokopedia["tiga huruf pertama"]
      
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
      
          # DIambil yang pesanan selesai tok
      mkt = tokopedia.loc[tokopedia['Status Pesanan'].isin(['Pesanan Selesai'] )]
      mkt = mkt[mkt['Username (Pembeli)'].notna()]
      
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
      mkt['Kode Bulan'] = enam.map(int) 
      conditions =[
          (mkt['Kode Bulan'] == 1),
          (mkt['Kode Bulan'] == 2),
          (mkt['Kode Bulan'] == 3),
          (mkt['Kode Bulan'] == 4),
          (mkt['Kode Bulan'] == 5),
          (mkt['Kode Bulan'] == 6),
          (mkt['Kode Bulan'] == 7),
          (mkt['Kode Bulan'] == 8),
          (mkt['Kode Bulan'] == 9),
          (mkt['Kode Bulan'] == 10),
          (mkt['Kode Bulan'] == 11),
          (mkt['Kode Bulan'] == 12),
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
      
    v_created_by = 'UPLOAD ' + v_created_by    
    for index, row in mkt.iterrows():
      v_waktu_pesanan_dibuat = datetime.datetime.strptime(row["Waktu Pesanan Dibuat"], "%d-%m-%Y %H:%M:%S") # Uploadan kalau tanggalnya string 2022-03-08 08:29
      # v_harga_awal = row["Harga Awal"].replace('Rp ', '').replace('.', '')
      # print(type(sh.cell_value(rowx=row, colx=0)), ' : ', sh.cell_value(rowx=row, colx=0))
      datetime_now = datetime.datetime.now()
      if row["Username (Pembeli)"] == 'nan':
        v_username = ''
      else:
        v_username = row["Username (Pembeli)"]
      new_menu = model_tabel.tabel_shopee_tokped(waktu_pesanan_dibuat=v_waktu_pesanan_dibuat, status_pesanan=row["Status Pesanan"], 
                      nama_produk=row["Nama Produk"], nomer_referensi_sku=row["Nomor Referensi SKU"], 
                      harga_awal=row["Harga Awal"], jumlah=row["Jumlah"], olshop='TOKOPEDIA',
                      username_pembeli=v_username, kota_kabupaten=row["Kota/Kabupaten"],
                      provinsi=row["Provinsi"], jenis_baru=row["Jenis Baru"],
                      waktu_new=row["Waktu New"], kategori_waktu=row["Kategori Waktu"],
                      kode_bulan=row["Kode Bulan"], bulan=row["Bulan"],
                      kode_1=row["Kode 1"], kode_2=row["Kode 2"], kode_3=row["Kode 3"],
                      jenis_produk=row["Jenis Produk"], kategori_produk=row["Kategori Waktu"],
                      bulan_pelaporan=v_bulan_pelaporan, tahun_pelaporan=v_tahun_pelaporan,
                      created_by=v_created_by, created_date=datetime_now, status_aktif=1,)
      db.session.add(new_menu)
      db.session.commit()    
      
    return mkt
  elif cek_data_tokopedia:
    return flash('Data sudah pernah di insert, tidak bisa di insert lagi !')
  else :
    return flash('Data shopee kosong !')  
  
def readDbShopeeTokopedia(v_tahun_pelaporan, v_bulan_pelaporan):
  print(v_tahun_pelaporan, v_bulan_pelaporan)
  query_shopee = db.session.query(model_tabel.tabel_shopee_tokped).filter_by(tahun_pelaporan=v_tahun_pelaporan, bulan_pelaporan=v_bulan_pelaporan, status_aktif=1).statement
  df = pd.read_sql(sql=query_shopee, con=db.engine ) 
    # PENJUALAN PRODUK - Pie Chart
  produk=df.groupby(['jenis_produk'])['jumlah'].sum().reset_index()
  # fig = px.pie(produk, values='jumlah', names='jenis_produk', title='Persentase Penjualan ALL Produk',color_discrete_sequence=px.colors.sequential.RdBu)
  # fig.show()
    # PEMBELIAN PRODUK LM DAN PERHIASAN BERDASARKAN PERIODE WAKTU
  perwaktu1=df.groupby(['kategori_waktu'])['jumlah'].sum().astype(int).reset_index()
    # PRODUK COLLABS
  collabs=df.groupby(['kode_3','kode_1','jenis_baru','jenis_produk'])['jumlah'].sum().reset_index()
  disney=collabs[collabs['kode_3']=='Y']
  line=collabs[collabs['kode_1']=='H']
  sanrio=collabs[collabs['kode_3']=='Z']
  emoji=collabs[collabs['kode_3']=='Q']
  line=line.rename(columns = {"kode_1": "collabs"})
  disney=disney.rename(columns = {"kode_3": "collabs"})
  sanrio=sanrio.rename(columns = {"kode_3": "collabs"})
  emoji=emoji.rename(columns = {"kode_3": "collabs"})
  allcollabsperhiasan=pd.concat([line, disney, sanrio, emoji])
  allcollabsperhiasan=allcollabsperhiasan.drop(columns=['kode_3','kode_1'])
  conditions =[
      (allcollabsperhiasan['collabs'] =='Y'),
      (allcollabsperhiasan['collabs'] =='H'),
      (allcollabsperhiasan['collabs'] =='Z'),
      (allcollabsperhiasan['collabs'] =='Q')
  ]

  letters = ['Disney','Line','Sanrio','Emoji']
  allcollabsperhiasan['collabs'] = np.select(conditions, letters)  
  # print(allcollabs)
  
  allcollabslm=df.groupby(['nama_produk','jenis_produk'])['jumlah'].sum().reset_index()
  allcollabslm['nama_produk'] = allcollabslm['nama_produk'].str.lower()
  allcollabslm=allcollabslm[allcollabslm['jenis_produk']=='LM']
    # PRODUK LM
  collabslmdisney=allcollabslm.loc[allcollabslm['nama_produk'].str.contains("disney", case=False)]
  collabslmdisney=collabslmdisney.assign(collabs='Disney')
  collabslmsanrio=allcollabslm.loc[allcollabslm['nama_produk'].str.contains("sanrio", case=False)]
  collabslmsanrio=collabslmsanrio.assign(collabs='Sanrio')  
  collabslmemoji =allcollabslm.loc[allcollabslm['nama_produk'].str.contains("emoji", case=False)]
  collabslmemoji=collabslmemoji.assign(collabs='Emoji')
  collabslmbt21 =allcollabslm.loc[allcollabslm['nama_produk'].str.contains("bt21", case=False)]
  collabslmbt21=collabslmbt21.assign(collabs='Line')
  collabslmline =allcollabslm.loc[allcollabslm['nama_produk'].str.contains("line", case=False)]
  collabslmline=collabslmline.assign(collabs='Line')
  allcollabsperhiasanlm=pd.concat([collabslmdisney, collabslmsanrio, collabslmemoji, collabslmbt21, collabslmline, allcollabsperhiasan])
  allcollabsperhiasanlm
  
  
    # JENIS PRODUK DAN REPEAT ORDER
  repeatorder = df.groupby(['jenis_produk','kategori_produk'])['jumlah'].count().reset_index()
  repeatorder
  
    # USERNAME LM
  username1 = df.groupby(['username_pembeli','jenis_produk','kategori_produk'])['jumlah'].sum().reset_index()
  username1 = username1.sort_values(by='jumlah',ascending=False)
  usernamel = username1[username1['kategori_produk']=="LM"]
  usernamel = usernamel.head(10)
  
    # USERNAME PERHIASAN
  username2 = df.groupby(['kategori_produk','username_pembeli'])['jumlah'].sum().reset_index()
  username2 = username2.sort_values(by='jumlah',ascending=False)
  username2 = username2[username2['kategori_produk']=="Perhiasan"]
  username2 = username2.head(10)
  username2
  
  alluser= pd.concat([username1, username2])
  
    # RATA - RATA HARGA AWAL
  ratha = df[df['jenis_produk']=='Anting']
  ratha = ratha['harga_awal'].sum()/ratha['jumlah'].sum()
  # ratha = round(ratha)
  # print('ASDASDASDASD : ',ratha)
  
  return produk, perwaktu1, allcollabsperhiasanlm, repeatorder, alluser, ratha
  
  
    
def readExcelShopeeTokopedia():
  if request.method == 'POST':
    v_tahun_laporan = request.form.get('tahun_pelaporan')
    v_bulan_laporan = request.form.get('bulan_pelaporan')
    # print('read v_tahun_laporan', v_tahun_laporan)
    # print('read v_bulan_laporan', v_bulan_laporan)
    cek_data_shopee = db.session.query(model_home.tabel_upload_excel).filter_by(tahun_pelaporan=v_tahun_laporan, bulan_pelaporan=v_bulan_laporan, olshop='SHOPEE', status_aktif=1).first()
    cek_data_tokopedia = db.session.query(model_home.tabel_upload_excel).filter_by(tahun_pelaporan=v_tahun_laporan, bulan_pelaporan=v_bulan_laporan, olshop='TOKOPEDIA', status_aktif=1).first()
    # print('cek_data_tokopedia', cek_data_shopee.file)
    # print('cek_data_tokopedia', cek_data_tokopedia['file'])
    if cek_data_shopee and cek_data_tokopedia:
      # print('Shopee x Tokopedia')
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
      # print('v_delete_yak_tokopedia : ', v_delete_yak_tokopedia)
      # print('v_delete_sj1_tokopedia : ', v_delete_sj1_tokopedia)
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
          # Pie Chart
      produk=mkt.groupby(['Jenis Produk'])['Jumlah'].sum().reset_index()
          # PEMBELIAN PRODUK LM DAN PERHIASAN BERDASARKAN PERIODE WAKTU
      perwaktu1=mkt.groupby(['Kategori Waktu'])['Jumlah'].sum().astype(int).reset_index()
          # PRODUK COLLABS
      collabs=mkt.groupby(['Kode 3','Kode 1','Jenis Baru','Jenis Produk'])['Jumlah'].sum().reset_index()
      disney=collabs[collabs['Kode 3']=='Y']
      line=collabs[collabs['Kode 1']=='H']
      sanrio=collabs[collabs['Kode 3']=='Z']
      emoji=collabs[collabs['Kode 3']=='Q']
      line=line.rename(columns = {"Kode 1": "Collabs"})
      disney=disney.rename(columns = {"Kode 3": "Collabs"})
      sanrio=sanrio.rename(columns = {"Kode 3": "Collabs"})
      emoji=emoji.rename(columns = {"Kode 3": "Collabs"})
      allcollabs=pd.concat([line, disney])
      allcollabs=pd.concat([allcollabs, sanrio])
      allcollabs=pd.concat([allcollabs, emoji])
      allcollabs=allcollabs.drop(columns=['Kode 3','Kode 1'])
      conditions =[
          (allcollabs['Collabs'] =='Y'),
          (allcollabs['Collabs'] =='H'),
          (allcollabs['Collabs'] =='Z'),
          (allcollabs['Collabs'] =='Q')
      ]

      letters = ['Disney','Line','Sanrio','Emoji']
      allcollabs['Collabs'] = np.select(conditions, letters)  
      
      return produk, perwaktu1, allcollabs
    elif not cek_data_tokopedia:
      return flash('File Tokopedia bulan tsb BELUM pernah di upload !!', 'warning')
    elif not cek_data_shopee:
      return flash('File Shopee bulan tsb BELUM pernah di upload !!', 'warning')
    else:
      return flash('MBOHHHH')
  return 'Bukan method post'