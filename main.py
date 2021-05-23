#! /usr/bin/env python3
import os
from werkzeug.utils import secure_filename, redirect
from utils import app
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = set(['txt', 'xlsx', 'xls', 'csv'])

@app.route("/")
def index():
    return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return render_template("index.html")
