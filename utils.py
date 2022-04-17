import tensorflow as tf
import tensorflow
import numpy as np
import cv2
from tensorflow.keras.models import load_model


def generate_prediction(image,model_file,shape=256,threshold=0.5):
    model = load_model(model_file)
    image = cv2.resize(image,(256,256))
    image = image.reshape((1,shape,shape,3))
    prediction = model.predict(image)[0][0]
    disease = model_file.split('_')[0]
    if prediction > threshold:
        prediction = disease
    else:
        prediction = 'no '+str(disease)
    return str(prediction)
