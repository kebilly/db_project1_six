import re, os, random, string
from typing_extensions import Self
from flask import Flask, request, template_rendered, Blueprint, url_for, redirect, flash, render_template
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from datetime import datetime
from numpy import identity, product
from sqlalchemy import null
from api.api import *
from api.sql import *
from travelschedule.views.store import *
from backstage.views.analysis import *
from backstage.views.manager import *
from link import *
from werkzeug.utils import secure_filename
import oracledb 
#import cx_Oracle
connection = oracledb.connect(user='Group6', password='WoXLK9f2n', host='140.117.69.60', port=1521, service_name='ORCLPDB1')
cursor = connection.cursor()
## Oracle 連線
#cx_Oracle.init_oracle_client(lib_dir="C:/oracle/instantclient_21_12") # init Oracle instant client 位置
#connection = cx_Oracle.connect('Group6', 'WoXLK9f2n', cx_Oracle.makedsn('140.117.69.60', 1521, 'ORCLPDB1')) # 連線資訊

## Flask-Login : 確保未登入者不能使用系統
app = Flask(__name__)
app.secret_key = 'Your Key' 

app.register_blueprint(api, url_prefix='/')
app.register_blueprint(store, url_prefix='/travelschedule')
app.register_blueprint(analysis, url_prefix='/backstage')
app.register_blueprint(manager, url_prefix='/backstage')

login_manager.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.secret_key = "Your Key"
    app.run(host='0.0.0.0')