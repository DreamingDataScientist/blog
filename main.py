import os
import sys

# sys.path includes 'server/lib' due to appengine_config.py
from flask import Flask
from flask import render_template

import markdown
from models import Post

app = Flask(__name__.split('.')[0])


@app.route('/')
@app.route('/index')
def index():
    """ Return hello template at application root URL."""
    return render_template('index.html')

@app.route('/blog')
def post():
    return render_template('post.html')

@app.route('/create-blog')
def create_post():
    return render_template('create_post.html')

@app.route('/admin')
def post():
    return render_template('post.html')
