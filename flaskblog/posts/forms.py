from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Optional, NumberRange, InputRequired
from datetime import datetime


class PostForm(FlaskForm):
    date_posted = DateField('Date', validators=[InputRequired()], default=datetime.now)
    pin = IntegerField('PIN', validators=[DataRequired()])
    associate = StringField(u'Associate', validators=[DataRequired(), Length(min=2, max=20)])
    dept = StringField(u'Department', validators=[DataRequired(), Length(min=2, max=40)])
    team_mgr = StringField(u'Team Manager', validators=[DataRequired(), Length(min=2, max=30)])
    ops_mgr = StringField(u'Ops Manager', validators=[DataRequired(), Length(min=2, max=30)])
    surv_trigg = IntegerField(u'Surveys Triggered', validators=[DataRequired()])
    surv_deliv = IntegerField(u'Surveys Delivered', validators=[DataRequired()])
    del_rate = FloatField(u'Delivery Rate', validators=[DataRequired()])
    resp_cnt = IntegerField('Resp. Count', validators=[InputRequired()])
    popo = StringField('Popo', validators=[Optional()])
    resp_rate = FloatField(u'Resp. Rate', validators=[InputRequired()])
    avg_rating = FloatField(u'Avg. Rating', validators=[InputRequired()])
    five_stars = FloatField(u'5 Stars', validators=[InputRequired(), NumberRange(min=0)])
    four_stars = FloatField(u'4 Stars', validators=[InputRequired(), NumberRange(min=0)])
    three_stars = FloatField(u'3 Stars', validators=[InputRequired(), NumberRange(min=0)])
    two_stars = FloatField(u'2 Stars', validators=[InputRequired(), NumberRange(min=0)])
    one_stars = FloatField(u'1 Stars', validators=[InputRequired(), NumberRange(min=0)])
    five_star = IntegerField(u'5 Star', validators=[InputRequired()])
    four_star = StringField(u'4 Star', validators=[InputRequired(), Length(max=10)])
    three_star = IntegerField(u'3 Star', validators=[InputRequired()])
    two_star = IntegerField(u'2 Star', validators=[InputRequired(), NumberRange(min=0)])
    one_star = IntegerField(u'1 Star', validators=[InputRequired(), NumberRange(min=0)])
    team_lead = StringField(u'Team Lead', validators=[Optional()])
    chan = StringField(u'Channel', validators=[DataRequired(), Length(min=2, max=10)])
    submit = SubmitField('Add Record')
    


