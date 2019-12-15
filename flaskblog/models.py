from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    #We pass the relationship with other model, backref does not have to be present in Posts
    posts = db.relationship('Post', backref='username', lazy=True)
    
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    pin = db.Column(db.Integer, nullable=False)
    associate = db.Column(db.Text, nullable=False)
    dept = db.Column(db.Text, nullable=False)
    team_mgr = db.Column(db.Text, nullable=False)
    ops_mgr = db.Column(db.Text, nullable=False)
    surv_trigg = db.Column(db.Integer, nullable=False)
    surv_deliv = db.Column(db.Integer, nullable=False)
    del_rate = db.Column(db.Float, nullable=False)
    resp_cnt = db.Column(db.Integer, nullable=False)
    popo = db.Column(db.Text, nullable=True, default="")
    resp_rate = db.Column(db.Float, nullable=False)
    avg_rating = db.Column(db.Float, nullable=False)
    five_stars = db.Column(db.Float, nullable=False)
    four_stars = db.Column(db.Float, nullable=False)
    three_stars = db.Column(db.Float, nullable=False)
    two_stars = db.Column(db.Float, nullable=False)
    one_stars = db.Column(db.Float, nullable=False)
    five_star = db.Column(db.Integer, nullable=False)
    four_star = db.Column(db.Integer, nullable=False)
    three_star = db.Column(db.Integer, nullable=False)
    two_star = db.Column(db.Integer, nullable=False)
    one_star = db.Column(db.Integer, nullable=False)
    team_lead = db.Column(db.Text, nullable=True, default="")
    chan = db.Column(db.Text, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.associate}', '{self.date_posted}', '{self.pin}')"

