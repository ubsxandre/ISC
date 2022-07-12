from app_iscs import db
from flask import abort
from flask_login import UserMixin, current_user
from flask_admin import expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView 

class User(db.Model, UserMixin ):
  id = db.Column(db.Integer, primary_key=True)
  nik = db.Column(db.String(10))
  nama = db.Column(db.String(50))
  password = db.Column(db.String(80))
  is_god = db.Column(db.Boolean, default=False)
  id_roles = db.Column(db.Integer, db.ForeignKey("m_roles.id"))
  
  def __repr__(self):
    return '<User {}>'.format(self.id) 
  def get_id(self):
    return (self.id)
  
class m_roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roles = db.Column(db.String(50))
def __repr__(self):
  return '<m_roles {}>'.format(self.id) 
def get_id(self):
  return (self.id)

class Controller(ModelView):
  def is_accessible(self):
    if current_user.is_god == True:
      return current_user.is_authenticated
    else:
      return abort(404)
    # return current_user.is_authenticated
  def not_auth(self):
    return 'Maaf Anda tidak Punya Akses untuk melihat ini !!!'
  
class DashboardView(AdminIndexView):

    def is_visible(self):
        # This view won't appear in the menu structure
        return False

    # @expose('/')
    # def index(self):

    #     return self.render(
    #         'admin/dashboard.html',
    #     )

  

  
  