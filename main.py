#! /usr/bin/env python3
from utils import logger, LostDBConnection
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    content = db.Column(db.LargeBinary)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/datasets')
def datasets():
    return render_template("datasets.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']
    new_file = FileContents(name=file.filename, content=file.read())
    try:
        db.session.add(new_file)
        db.session.commit()
        return redirect('/datasets')
    except LostDBConnection:
        logger.error('Error during connection into database.')


if __name__ == '__main__':
    app.run(debug=True)
