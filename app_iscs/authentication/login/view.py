from flask.helpers import flash
from app_iscs.authentication.login import app_login_init, controller, model
from flask import render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from app_iscs import db
from flask_login import login_user, login_required, current_user, logout_user

@app_login_init.route('/')
def route_default():
  return redirect(url_for('login.login'))

@app_login_init.route('/login')
def login():
  return render_template('accounts/login.html')
  # return 'tes'

# ----------------------- LOGIN -----------------------------------------#
@app_login_init.route('/login', methods=['POST', 'GET'])
def login_post():
  msg = ''
  v_nik = request.form.get('nik')
  v_password = request.form.get('password')

  user = model.User.query.filter_by(nik=v_nik, password=v_password).first()
  # password = model.User.query.filter_by(password=v_password).first()

  if not user :
    msg = 'Kombinasi username dan password salah !!!'
    return render_template('accounts/login.html', msg=msg) # if the user doesn't exist or password is wrong, reload the page

  login_user(user)
  # if the above check passes, then we know the user has the right credentials
  return redirect(url_for('app_home.home'))


# ----------------------- LOGOUT -----------------------------------------#
@app_login_init.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('login.logout'))

# # REGISTER
# @app_login_init.route('/register', methods=['POST', 'GET'])
# def register():
#   msg = ''
#   nik = request.form.get('nik_daftar')
#   nama = request.form.get('nama_daftar')
#   password = request.form.get('password_daftar')
  
#   user = model.User.query.filter_by(nik=nik).first()
  
#   if user:
#     return 'user sudah ada'
  
#   # new_user = model.User(nik=nik, nama=nama, password=generate_password_hash(password, method='sha256'))
#   new_user = model.User(nik=nik, nama=nama, password=password)
  
#   # add the new user to the database
#   db.session.add(new_user)
#   db.session.commit() 
  
#   msg='Berhasil Mendaftar'
#   return render_template('login/login.html', msg=msg)



# ----------------------- ERORR -----------------------------------------#

@app_login_init.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@app_login_init.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@app_login_init.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500