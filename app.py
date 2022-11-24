from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/get-img', methods = ['POST'])
def get():
    if request.method == 'POST':
        arg1=request.get_json()['url']

@app.route('/')
def home():
   
    return "hello world"

# app.run()




# %%
import tensorflow
import pickle
import cv2
import numpy as np
from tensorflow.keras.models import load_model

def pridict (url):
  instance=pickle.load(open(r"Label_Instance.pkl","rb"))
  mod=load_model(r"model.h5")
  img = cv2.imread(url)
  img = cv2.resize(img,(256,256))
  img = np.reshape(img,[1,256,256,3]) 
  img=img/255.0
  max_val=np.argmax(mod.predict(img))
  label=instance.classes_[max_val]
  return label

def test(url):
  return url

