from email.policy import default
from app_iscs import db
import datetime

class tabel_shopee_tokped (db.Model):
  # UNTUK FORM REQUEST
  id = db.Column(db.Integer, primary_key=True)
  waktu_pesanan_dibuat = db.Column(db.DateTime)
  status_pesanan = db.Column(db.String(100))
  nama_produk = db.Column(db.String(100))
  nomer_referensi_sku = db.Column(db.String(100))
  harga_awal = db.Column(db.Float(15,2))
  jumlah = db.Column(db.Float(6,2))
  username_pembeli = db.Column(db.String(100))
  kota_kabupaten = db.Column(db.String(100))
  provinsi = db.Column(db.String(100))
  jenis_baru = db.Column(db.String(100))
  waktu_new = db.Column(db.Integer)
  kategori_waktu = db.Column(db.String(100))
  kode_bulan = db.Column(db.Integer)
  bulan=db.Column(db.String(20))
  kode_1 = db.Column(db.String(10))
  kode_2 = db.Column(db.String(10))
  kode_3 = db.Column(db.String(10))
  jenis_produk = db.Column(db.String(100))
  kategori_produk = db.Column(db.String(100))
  olshop = db.Column(db.String(100))
  bulan_pelaporan = db.Column(db.String(2))
  tahun_pelaporan = db.Column(db.String(4))
  created_by = db.Column(db.String(100), default='Default')
  created_date = db.Column(db.DateTime, default=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))
  status_aktif = db.Column(db.String(2), default='0')
  
  # def __init__(self, waktu_pesanan_dibuat, status_pesanan, nama_produk, nomer_referensi_sku, harga_awal,
  #              jumlah, username_pembeli, kota_kabupaten):
  #   self.waktu_pesanan_dibuat = waktu_pesanan_dibuat
  #   self.status_pesanan = status_pesanan
  #   self.nama_produk = nama_produk
  #   self.nomer_referensi_sku = nomer_referensi_sku
  
  def __repr__(self):
    return '<tabel_shopee_tokped {}>'.format(self.id, self.waktu_pesanan_dibuat) 
  
  
  

