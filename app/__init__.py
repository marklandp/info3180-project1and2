from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://proj1:proj1@localhost/proj1'
db = SQLAlchemy(app)

from app import views, models


