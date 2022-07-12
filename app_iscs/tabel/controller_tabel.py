from multiprocessing import current_process
from flask import json, jsonify, request, flash, redirect, Response, send_file, url_for
import os, datetime, csv, io, pandas as pd, xlrd, openpyxl, pandas.io as sql, numpy as np
from io import TextIOWrapper, BytesIO
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.utils import secure_filename
from app_iscs import *
from app_iscs.tabel import model_tabel

def tabel_shopee_tokped():
  data_shopee_tokped = model_tabel.tabel_shopee_tokped.query.filter_by(status_aktif=1)
  db.session.close()
  return data_shopee_tokped


def readFileExt(fileUpload):    # membaca ext
  namaFile, namaExt = os.path.splitext(fileUpload)
  # print('Nama File : ', namaFile, namaExt)
  return namaExt

def readFileName(fileUpload):    # membaca ext
  namaFile, namaExt = os.path.splitext(fileUpload)
  # print('Nama File : ', namaFile, namaExt)
  return namaFile

def uploadfileShopee_excel():
  if request.method == 'POST':
    # cur.commit()      # **FYI : kalau pakai commit manual itu harus con.autocommit = False
    v_bulan_laporan = request.form.get('bulan_pelaporan')
    v_tahun_laporan = request.form.get('tahun_pellaporan')
    cek_data = db.session.query(model_tabel.tabel_shopee_tokped).filter_by(tahun_pelaporan=v_tahun_laporan, bulan_pelaporan=v_bulan_laporan, olshop='SHOPEE', status_aktif=1).all()
    print('Cek data ', type(cek_data), cek_data)
    if not cek_data:      
      excel_file = request.files['file']
      excel_file_name = request.files['file'].filename
      shopee = pd.read_excel(excel_file, engine='openpyxl', index_col=0)
  # Hanya digunakan yang pesanan selesai
      shopee=shopee.loc[shopee['Status Pesanan'].isin(['Selesai'])]
  # Mengambil Variabel yang digunakan
      shopee = shopee[["Waktu Pesanan Dibuat","Status Pesanan","Nama Produk","Nomor Referensi SKU","Harga Awal","Jumlah","Username (Pembeli)","Kota/Kabupaten","Provinsi"]]
      shopee['Jenis Baru'] = shopee['Nomor Referensi SKU'].str.split('-').str[0].str.strip()
      shopee['tiga huruf pertama']=shopee['Nomor Referensi SKU'].str[:3]
      v_delete_yak = shopee[shopee["tiga huruf pertama"] == 'YAK'].count()
      v_delete_sj1 = shopee[shopee["tiga huruf pertama"] == 'SJ1'].count()
      v_delete_yak = v_delete_yak["tiga huruf pertama"]
      v_delete_sj1 = v_delete_sj1["tiga huruf pertama"]
      # print('ASDASDASDASD : ', v_delete_yak, v_delete_sj1)
  # DATA CLEANSING
      mkt_with_index = shopee.set_index("tiga huruf pertama")
      if v_delete_yak >= 1 and v_delete_sj1 >= 1:
        data_with_index = mkt_with_index.drop(['YAK', 'SJ1'], axis=0, inplace=True)
        shopee=data_with_index.reset_index()
      elif v_delete_yak >= 1:
        data_with_index = mkt_with_index.drop(['YAK'], axis=0, inplace=True)
        shopee=data_with_index.reset_index()
      elif v_delete_sj1 >= 1:
        data_with_index = mkt_with_index.drop(['SJ1'], axis=0, inplace=True)
        shopee=data_with_index.reset_index()
      else:
        shopee=shopee.drop(columns=['tiga huruf pertama'])
      dua = pd.to_datetime(shopee['Waktu Pesanan Dibuat']).dt.hour.map(str).str.zfill(2)
      tiga = pd.to_datetime(shopee['Waktu Pesanan Dibuat']).dt.minute.map(str).str.zfill(2)
      empat = dua+tiga
      shopee['Waktu New'] = empat.map(int)
      conditions =[
          (shopee['Waktu New'] >= 1) & (shopee['Waktu New'] <= 100), 
          (shopee['Waktu New'] >= 101) & (shopee['Waktu New'] <= 200), 
          (shopee['Waktu New'] >= 201) & (shopee['Waktu New'] <= 300), 
          (shopee['Waktu New'] >= 301) & (shopee['Waktu New'] <= 400), 
          (shopee['Waktu New'] >= 401) & (shopee['Waktu New'] <= 500), 
          (shopee['Waktu New'] >= 501) & (shopee['Waktu New'] <= 600), 
          (shopee['Waktu New'] >= 601) & (shopee['Waktu New'] <= 700), 
          (shopee['Waktu New'] >= 701) & (shopee['Waktu New'] <= 800),
          (shopee['Waktu New'] >= 801) & (shopee['Waktu New'] <= 900),
          (shopee['Waktu New'] >= 901) & (shopee['Waktu New'] <= 1000),
          (shopee['Waktu New'] >= 1001) & (shopee['Waktu New'] <= 1100),
          (shopee['Waktu New'] >= 1101) & (shopee['Waktu New'] <= 1200),
          (shopee['Waktu New'] >= 1201) & (shopee['Waktu New'] <= 1300), 
          (shopee['Waktu New'] >= 1301) & (shopee['Waktu New'] <= 1400), 
          (shopee['Waktu New'] >= 1401) & (shopee['Waktu New'] <= 1500), 
          (shopee['Waktu New'] >= 1501) & (shopee['Waktu New'] <= 1600), 
          (shopee['Waktu New'] >= 1601) & (shopee['Waktu New'] <= 1700), 
          (shopee['Waktu New'] >= 1701) & (shopee['Waktu New'] <= 1800), 
          (shopee['Waktu New'] >= 1801) & (shopee['Waktu New'] <= 1900), 
          (shopee['Waktu New'] >= 1901) & (shopee['Waktu New'] <= 2000),
          (shopee['Waktu New'] >= 2001) & (shopee['Waktu New'] <= 2100),
          (shopee['Waktu New'] >= 2101) & (shopee['Waktu New'] <= 2200),
          (shopee['Waktu New'] >= 2201) & (shopee['Waktu New'] <= 2300),
          (shopee['Waktu New'] >= 2301) & (shopee['Waktu New'] <= 2359),
          (shopee['Waktu New'] ==0)
      ]

      letters = ['00:01-01:00', '01:01-02:00', '02:01-03:00', '03:01-04:00', '04:01-05:00','05:01-06:00','06:01-07:00','07:01-08:00','08:00-09:00','09:01-10:00',
                '10:01-11:00','11:01-12:00', '12:01-13:00', '13:01-14:00', '14:01-15:00', '15:01-16:00','16:01-17:00','17:01-18:00','18:01-19:00','19:01-20:00',
                '20:01-21:00','21:01-22:00', '22:01-23:00', '23:01-00:00', '23:01-00:00']
      shopee['Kategori Waktu'] = np.select(conditions, letters)   
      # shopee['Harga Awal']=shopee['Harga Awal'].str.replace('Rp','').str.replace('.','').astype(int)
      # print('Book : ', shopee)
      # sql.write(book, con=con, name='table_name_for_df', if_exists='replace', flavor='mysql')
      # v_harga_awal = book.cell_value(rowx=1, colx=15).replace('Rp ', '').replace('.', '')
      for index, row in shopee.iterrows():
        v_waktu_pesanan_dibuat = datetime.datetime.strptime(row["Waktu Pesanan Dibuat"], "%Y-%m-%d %H:%M") # Uploadan kalau tanggalnya string 2022-03-08 08:29
        v_harga_awal = row["Harga Awal"].replace('Rp ', '').replace('.', '')
        # print(type(sh.cell_value(rowx=row, colx=0)), ' : ', sh.cell_value(rowx=row, colx=0))
        v_created_by = 'UPLOAD ' + current_user.nama
        datetime_now = datetime.datetime.now()
        if row["Username (Pembeli)"] == 'nan':
          v_username = ''
        else:
          v_username = row["Username (Pembeli)"]
        new_menu = model_tabel.tabel_shopee_tokped(waktu_pesanan_dibuat=v_waktu_pesanan_dibuat, status_pesanan=row["Status Pesanan"], 
                                                    nama_produk=row["Nama Produk"], nomer_referensi_sku=row["Nomor Referensi SKU"], 
                                                    harga_awal=float(v_harga_awal), jumlah=row["Jumlah"], olshop='SHOPEE',
                                                    username_pembeli=v_username, kota_kabupaten=row["Kota/Kabupaten"],
                                                    provinsi=row["Provinsi"], bulan_pelaporan=v_bulan_laporan, tahun_pelaporan=v_tahun_laporan,
                                                    created_by=v_created_by, created_date=datetime_now, status_aktif=1,)
        db.session.add(new_menu)
        db.session.commit()    
      flash(excel_file_name + ' Berhasil di upload!!!')
    else : 
      flash('Sudah pernah di upload!!!')
  return redirect(url_for('app_tabel.tabelUpload'))


def uploadfileTokopedia_excel():
  if request.method == 'POST':
    # cur.commit()      # **FYI : kalau pakai commit manual itu harus con.autocommit = False
    v_bulan_laporan = request.form.get('bulan_laporan_tokopedia')
    v_tahun_laporan = request.form.get('tahun_laporan_tokopedia')
    cek_data = db.session.query(model_tabel.tabel_shopee_tokped).filter_by(tahun_pelaporan=v_tahun_laporan, bulan_pelaporan=v_bulan_laporan, olshop='TOKOPEDIA', status_aktif=1).all()
    print('Cek data ', type(cek_data), cek_data)
    if not cek_data:      
      excel_file = request.files['file']
      excel_file_name = request.files['file'].filename
      tokopedia = pd.read_excel(excel_file, engine='openpyxl', index_col=0)
      tokopedia=tokopedia.fillna(method="ffill")
  # Mengambil Variabel yang digunakan
      tokopedia = tokopedia[["Tanggal Pembayaran","Status Terakhir","Nama Produk","Nomor SKU","Harga Awal (IDR)","Jumlah Produk Dibeli","Nama Pembeli","Kota","Provinsi"]]
      tokopedia['Jenis Baru'] = tokopedia['Nomor SKU'].str.split('-').str[0].str.strip()
      tokopedia['tiga huruf pertama']=tokopedia['Nomor SKU'].str[:3]
      v_delete_yak = tokopedia[tokopedia["tiga huruf pertama"] == 'YAK'].count()
      v_delete_yak = v_delete_yak["tiga huruf pertama"]
      v_delete_sj1 = tokopedia[tokopedia["tiga huruf pertama"] == 'SJ1'].count()
      v_delete_sj1 = v_delete_sj1["tiga huruf pertama"]
      # print('v_delete_yak', type(v_delete_yak), v_delete_yak)
      # print('v_delete_sj1', type(v_delete_sj1), v_delete_sj1)
  # Ganti nama kolom
      tokopedia=tokopedia.rename(columns = {"Tanggal Pembayaran": "Waktu Pesanan Dibuat",
                     "Status Terakhir":"Status Pesanan", "Nomor SKU":"Nomor Referensi SKU", "Harga Awal (IDR)":"Harga Awal",
                        "Jumlah Produk Dibeli":"Jumlah", "Nama Pembeli":"Username (Pembeli)", "Kota":"Kota/Kabupaten"})
  # Hanya digunakan yang pesanan selesai
      tokopedia=tokopedia.loc[tokopedia['Status Pesanan'].isin(['Pesanan Selesai'])]
  # DATA CLEANSING 
      # mkt_with_index = tokopedia.set_index("tiga huruf pertama")
      flash(excel_file_name + ' Berhasil di upload!!!')
    else : 
      flash('Sudah pernah di upload!!!')
  return redirect(url_for('app_tabel.tabelUpload'))