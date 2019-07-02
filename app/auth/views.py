#!/usr/bin/env python
#
#  Copyright (C) 2019 Tieto Czech s.r.o.
#  Lumir Jasiok
#  lumir.jasiok@tieto.com
#  http://www.tieto.com
#
#
#

from flask import render_template
from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')
