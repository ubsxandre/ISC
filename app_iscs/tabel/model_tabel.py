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
  olshop = db.Column(db.String(100))
  bulan_pelaporan = db.Column(db.String(2))
  tahun_pelaporan = db.Column(db.String(4))
  created_by = db.Column(db.String(100), default='Default')
  created_date = db.Column(db.DateTime, default=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))
  status_aktif = db.Column(db.String(2), default='0')
  def __repr__(self):
    return '<tabel_shopee_tokped {}>'.format(self.id) 