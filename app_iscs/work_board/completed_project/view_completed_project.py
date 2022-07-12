from django.shortcuts import render
from flask import render_template, request, redirect, url_for
from app_iscs.work_board.completed_project import app_completed_project
from jinja2 import TemplateNotFound

@app_completed_project.route('/completed-project')
def completed_project():
  return render_template('work_board/completed_project/completed-project-table.html')

@app_completed_project.route('/view-completed-project')
def add_completed_project():
  return render_template('work_board/completed_project/completed-project-form.html')

