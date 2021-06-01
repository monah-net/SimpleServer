#! /usr/bin/env python3
import os
from os.path import isfile

from werkzeug.utils import secure_filename, redirect
from utils import app
from flask import Flask, render_template, request, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
UPLOAD_FOLDER = os.getcwd()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'xlsx', 'xls', 'csv'}
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///FileFolder.db'
db = SQLAlchemy(app)


# class File(db.Mode):


@app.route("/")
def index():
    uploaded_files = fetch_all_files()
    return render_template("index.html", data=uploaded_files)


def fetch_all_files():
    return [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if '.' in f and f.rsplit('.', 1)[1] in
                      ALLOWED_EXTENSIONS]

@app.route("/uploads")
def upload():
    return render_template("uploads.html")


@app.route("/about")
def about():
    return render_template("about.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploads', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['filename']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploaded_files = fetch_all_files()
            return render_template("index.html", data=uploaded_files)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.run(debug=True)
