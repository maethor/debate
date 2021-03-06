#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu


from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

from datetime import datetime

from flask import Flask, render_template, abort, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.restless import APIManager
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView
from flask.ext.gravatar import Gravatar
from flask.ext.markdown import Markdown

from settings import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings['DATABASE']
db = SQLAlchemy(app)

gravatar = Gravatar(app,
                    size=60,
                    rating='x',
                    default='retro',
                    force_default=False,
                    force_lower=False)

Markdown(app,
         output_format='html5',
         safe_mode=True)


class Thread(db.Model):
    id = db.Column(db.Unicode, primary_key=True)
    is_closed = db.Column(db.Boolean)

    def __init__(self, id, is_closed=False):
        self.id = id
        self.is_closed = is_closed

    def __repr__(self):
        return self.id


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_website = db.Column(db.Unicode)
    author_name = db.Column(db.Unicode)
    author_email = db.Column(db.Unicode)
    author_website = db.Column(db.Unicode)
    body = db.Column(db.Unicode)
    thread_id = db.Column(db.Unicode, db.ForeignKey('thread.id'))
    thread = db.relationship('Thread',
                             backref=db.backref('comments', lazy='dynamic'))
    created_at = db.Column(db.DateTime)

    def __init__(self, body, author_name, author_email, author_website,
                 thread, created_at=None):
        self.body = body
        self.author_name = author_name
        self.author_email = author_email
        self.author_website = author_website
        self.thread = thread
        if created_at is None:
            created_at = datetime.utcnow()
        self.created_at = created_at

    def __repr__(self):
        return '<Comment %r>' % self.id


admin = Admin(app)
admin.add_view(ModelView(Thread, db.session))
admin.add_view(ModelView(Comment, db.session))

#manager = APIManager(app, flask_sqlalchemy_db=db)
#manager.create_api(Thread, methods=['GET'])
#manager.create_api(Comment, methods=['GET', 'POST'])


@app.errorhandler(404)
def error404(e):
    return render_template('404.html'), 404


@app.route('/')
def home():
    return "toto"


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/thread/<thread_id>')
def print_thread(thread_id):
    thread = Thread.query.filter_by(id=thread_id).first()
    return render_template('thread.html', thread_id=thread_id, thread=thread)


@app.route('/comment/new', methods=['GET', 'POST'])
def comment_new():
    if request.method == 'POST':
        f = request.form
        thread = Thread.query.filter_by(id=f['thread_id']).first()
        if not thread:
            thread = Thread(f['thread_id'])
            db.session.add(thread)

        c = Comment(f['body'], f['author_name'], f['author_email'],
                    f['author_website'], thread)
        db.session.add(c)
        db.session.commit()
        return redirect(request.referrer)
    else:
        abort(404)


if __name__ == '__main__':
    db.create_all()

    app.debug = True
    app.config['SECRET_KEY']=b"ezrbzifbvshbfvpefnrv"
    app.run()
