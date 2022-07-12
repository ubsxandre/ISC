from app_iscs import db
import datetime

class tabel_upload_excel (db.Model):
  # UNTUK FORM REQUEST
  id = db.Column(db.Integer, primary_key=True)
  file = db.Column(db.String(100), default='Default')
  olshop = db.Column(db.String(100), default='Default')
  bulan_pelaporan = db.Column(db.String(2))
  tahun_pelaporan = db.Column(db.String(4))
  created_by = db.Column(db.String(100), default='Default')
  created_date = db.Column(db.DateTime, default=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S'))
  status_aktif = db.Column(db.String(2), default='0')
  def __repr__(self):
    return '<tabel_shopee_tokped {}>'.format(self.id) 
   
# class form_request (db.Model):
#   # UNTUK FORM REQUEST
#   request_id = db.Column(db.Integer, primary_key=True)
#   nama_project = db.Column(db.String(100))
#   departemen = db.Column(db.String(100))
#   pic = db.Column(db.String(100))
#   bagian = db.Column(db.String(100))
#   ext = db.Column(db.String(100))
#   deskripsi = db.Column(db.String(500))
#   foto_area = db.Column(db.String(100))
#   # END UNTUK FORM REQUEST
  
#   # UNTUK FORM SURVEY
  
#   # END UNTUK FORM SURVEY
  
  
#   created_by = db.Column(db.String(100))
#   created_date = db.Column(db.DateTime)
#   status_aktif = db.Column(db.String(2))
#   def __repr__(self):
#     return '<form_request {}>'.format(self.id) 
  
# class history_form_request (db.Model):
#   id_history = db.Column(db.Integer, primary_key=True)
#   id = db.Column(db.Integer)
#   no_urut_edit = db.Column(db.Integer)
#   nama_project = db.Column(db.String(100))
#   departemen = db.Column(db.String(100))
#   pic = db.Column(db.String(100))
#   bagian = db.Column(db.String(100))
#   ext = db.Column(db.String(20))
#   deskripsi = db.Column(db.String(500))
#   foto_area = db.Column(db.String(100))
#   created_by = db.Column(db.String(100))
#   created_date = db.Column(db.DateTime)
#   status_aktif = db.Column(db.String(2))
#   def __repr__(self):
#     return '<form_request {}>'.format(self.id) 