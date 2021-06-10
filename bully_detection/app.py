from flask import Flask,render_template,url_for,request
import numpy as np
import pickle
import pandas as pd
import tensorflow as tf
import math
import os
import joblib
import keras


#from keras import model_from_json
#json_file = open('model.json','r') 
#loaded_model_json = json_file.read() 
#json_file.close() 

# use Keras model_from_json to make a loaded model 
#loaded_model = model_from_json(loaded_model_json) 

# load weights into new model 
#loaded_model.load_weights("model.h5") 
#print("Loaded Model from disk") 

# compile and evaluate loaded model 
#loaded_model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])


from keras.models import load_model
loaded_model = load_model('network.h5')

def Predict(seed_text):
    print('About to predict')
    #seed_text = Tokeniser.texts_to_sequences(seed_text)
    #seed_text = tf.keras.preprocessing.sequence.pad_sequences(seed_text, 342)

    x = [seed_text]
    Tokeniser = tf.keras.preprocessing.text.Tokenizer()
    Tokeniser.fit_on_texts(x)
    x = Tokeniser.texts_to_sequences(x)
    x = tf.keras.preprocessing.sequence.pad_sequences(x, 342)

    x = np.array(x)
    #print(x)
    
    prediction = loaded_model(x)
    print(str(prediction))
    return str(prediction)

app=Flask(__name__)

@app.route('/',methods=['PUT',"GET","POST"])
def home():
    id=request.form.get("userid")
    ans = Predict(id)
    return render_template('index.html', ans=[id, ans])


if __name__=="__main__":
    app.run(debug=True)
