#!/usr/bin/env python
#
#  Copyright (C) 2019 Tieto Czech s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@tieto.com
#  http://www.tieto.com
#
#
#

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
