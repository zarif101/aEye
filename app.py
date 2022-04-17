from flask import Flask, url_for
from flask import render_template
import requests
from flask import request
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np
from utils import generate_prediction
import os
from twilio.rest import Client

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/cateract')
def cateract():
    return render_template('cateract.html')

@app.route('/glaucoma')
def glaucoma():
    return render_template('glaucoma.html')

@app.route('/myopia')
def myopia():
    return render_template('myopia.html')

@app.route('/cateract-uploader', methods = ['GET', 'POST'])
def upload_file_cateract():
    if request.method == 'POST':
        image = request.files['file']
        img = Image.open(image)
        img = np.array(img)
        prediction = generate_prediction(img,'cateract_model.h5',shape=256)
        # CATERACT GET PREDICTION -> store in prediction
        data = {
        'filename':image.filename,
        'prediction': prediction,
    }
        return render_template('present-prediction.html',data=data)
    return "invalid!"

@app.route('/glaucoma-uploader', methods = ['GET', 'POST'])
def upload_file_glaucoma():
    if request.method == 'POST':
        image = request.files['file']
        img = Image.open(image)
        img = np.array(img)
        prediction = generate_prediction(img,'glaucoma_model.h5',shape=256)
        # CATERACT GET PREDICTION -> store in prediction
        data = {
        'filename':image.filename,
        'prediction': prediction,
    }
        return render_template('present-prediction.html',data=data)
    return "invalid!"

@app.route('/myopia-uploader', methods = ['GET', 'POST'])
def upload_file_myopia():
    if request.method == 'POST':
        image = request.files['file']
        img = Image.open(image)
        img = np.array(img)
        prediction = generate_prediction(img,'myopia_model.h5',shape=256)
        # CATERACT GET PREDICTION -> store in prediction
        data = {
        'filename':image.filename,
        'prediction': prediction,
    }
        return render_template('present-prediction.html',data=data)
    return "invalid!"

@app.route('/notification', methods = ['POST'])
def sent_notification():
    message = str(request.form.get('text-message'))
    number = str(request.form.get('phone-number'))
    account_sid = "AC5bbbc2ecf3d97ae5b7afc57eceb10ddc"
    auth_token = "0cbc62b928a2f384ce077fd955eeeb6d"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  body=str(message),
                                  from_='+19705919814',
                                  to='+1'+str(number)
                              )

    return render_template('home.html')
