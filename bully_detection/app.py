from flask import Flask,render_template,url_for,request
import numpy as np
import pickle
import pandas as pd
import tensorflow as tf
import math
import os
import joblib

from keras.models import load_model
loaded_model = load_model('network.h5')
Tokeniser = tf.keras.preprocessing.text.Tokenizer()

def Predict(seed_text):
    seed_text = Tokeniser.texts_to_sequences(seed_text)
    seed_text = tf.keras.preprocessing.sequence.pad_sequences(seed_text, 342)
    prediction = loaded_model(seed_text)
    print(str(prediction))

app=Flask(__name__)

@app.route('/',methods=['PUT',"GET","POST"])
def home():
    id=request.form.get("userid")
    #Predict(id)
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
