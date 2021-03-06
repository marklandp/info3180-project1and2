from . import db
class User_info(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  userid = db.Column(db.Integer, unique=True)
  image = db.Column(db.String(50))
  fname = db.Column(db.String(40))
  lname = db.Column(db.String(40))
  age = db.Column(db.Integer)
  sex = db.Column(db.String(6))
  highscore = db.Column(db.Integer)
  tdollars = db.Column(db.Integer)
  datejoined = db.Column(db.DateTime)
  
  def __init__(self, username, userid, image, fname, lname, age, sex, date): 
    self.username = username
    self.userid = userid
    self.image = image
    self.fname = fname
    self.lname = lname
    self.age = age
    self.sex = sex
    self.highscore = 0
    self.tdollars = 0
    self.datejoined = date

  def __repr__(self):
    return '<User %r>' % self.username