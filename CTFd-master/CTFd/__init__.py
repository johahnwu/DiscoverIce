from flask import Flask, render_template, request, redirect, abort, session, jsonify, json as json_mod, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler
from flask.ext.session import Session
import os
import sqlalchemy
from flask.ext.mysqldb import MySQL


def create_app(config='CTFd.config'):
    app = Flask("CTFd")

    with app.app_context():
        app.config.from_object(config)

        from CTFd.models import db, Teams, Solves, Challenges, WrongKeys, Keys, Tags, Files, Tracking, mysql

        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
        app.config['MYSQL_DATABASE_DB'] = 'EmpData'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        mysql.init_app(app)

        cursor = mysql.connection.cursor()
        

#        cursor.execute('CREATE DATABASE  IF NOT EXISTS info_sec;')
#        cursor.execute('USE info_sec;')        
#        cursor.execute('CREATE TABLE IF NOT EXISTS info_sec.security_table \
#        (\
#        username varchar(255),\
#        pass char(255));')



        db.init_app(app)
        db.create_all()

        app.db = db

        #Session(app)

        from CTFd.views import views
        from CTFd.challenges import challenges
        from CTFd.scoreboard import scoreboard
        from CTFd.auth import auth
        from CTFd.admin import admin
        from CTFd.utils import init_utils, init_errors, init_logs

        init_utils(app)
        init_errors(app)
        init_logs(app)

        app.register_blueprint(views)
        app.register_blueprint(challenges)
        app.register_blueprint(scoreboard)
        app.register_blueprint(auth)
        app.register_blueprint(admin)

        return app
