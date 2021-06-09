from flask import Flask,render_template,url_for,request
import numpy as np
import pickle
import pandas as pd

app=Flask(__name__)

@app.route('/',methods=['PUT',"GET","POST"])
def home():
    id=request.form.get("userid")
    print(id)
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
