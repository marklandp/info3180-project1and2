"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from app import db
from app.models import User_info
from flask import jsonify, session
from datetime import *
from .forms import NewProfileForm
import json
from flask import Response
from werkzeug.utils import secure_filename
import os
import time


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


def timeinfo():
    return datetime.now()
    
@app.route('/profile/', methods=['POST', 'GET'])
def profile():
  """Render the profile page"""
  form = NewProfileForm()
  if form.validate_on_submit():
    username = request.form['username']
    email = request.form['email']
    photo = request.files['image']
    imagename = username + '_' + secure_filename(photo.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], imagename)
    photo.save(file_path)
    fname = request.form['fname']
    lname = request.form['lname']
    age = int(request.form['age'])
    sex = request.form['sex']
    newUser = User_info(username, email, imagename, fname, lname, age, sex, timeinfo())
    db.session.add(newUser)
    db.session.commit()
    nu = User_info.query.filter_by(username=username).first()
    return redirect('/profile/'+str(nu.id)) 
  return render_template('form.html', form=form)


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
