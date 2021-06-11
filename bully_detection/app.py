from flask import Flask,render_template,url_for,request
import numpy as np
import pickle
import pandas as pd
import tensorflow as tf
import math
import os
import joblib
import keras
import smtplib

from keras.models import load_model
loaded_model = load_model('the_final_model.h5')

import joblib
tok = joblib.load('tokenizer.pkl')

app=Flask(__name__)

def Predict(x):
    seed_text = str(x)
    seed_text = [seed_text]
    print(seed_text)
    seed_text = tok.texts_to_sequences(seed_text)
    seed_text = tf.keras.preprocessing.sequence.pad_sequences(seed_text, 342)
    prediction = loaded_model(seed_text)
    a = str(prediction)
    a = float(a[12:18])
    return a


def report(userid):
    sender = 'tcr19cs017@gectcr.ac.in'
    receivers = ['tcr19cs017@gectcr.ac.in']
    password=""
    message ="Cyber Team, \n "+str(userid)+"was caught for defaming others!!\n\n This is a test email !!!"
    try:
        smtpObj = smtplib.SMTP("smtp.gmail.com",int(587))
        smtpObj.starttls()
        smtpObj.login(sender,password)
        smtpObj.sendmail(sender, receivers, message)         
        print("Successfully sent email")
        return "\n\nReported as cyber crime!!"
    except Exception as e:
        print("Error: unable to send email : "+str(e))
        return "\n\nError: unable to send email"


@app.route('/',methods=['PUT',"GET","POST"])
def home():
    id=request.form.get("userid")
    ans = Predict(id)
    if ans > 0.5:
        pred = "Inappropriate Content"
        r=report(id)
    else:
        pred = "Appropriate Content"    

    return render_template('index.html', ans=[id, pred,r])


if __name__=="__main__":
    app.run(debug=True)
