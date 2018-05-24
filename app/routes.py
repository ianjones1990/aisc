from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html', title='AISC')


@app.route('/blog')
def blog():
    return render_template('blog.html', title='BLOG')
