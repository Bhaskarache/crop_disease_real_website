from flask import Flask,render_template,request,jsonify
from pathlib import Path
from werkzeug.utils import secure_filename
app=Flask(__name__); Path("uploads").mkdir(exist_ok=True); model=None; classes=[]
try:
 from tensorflow.keras.models import load_model
 if Path("model/model.h5").exists(): model=load_model("model/model.h5")
 if Path("model/classes.txt").exists(): classes=Path("model/classes.txt").read_text().splitlines()
except Exception as e: print("Model not loaded:",e)
@app.get("/")
def home(): return render_template("index.html")
@app.post("/predict")
def predict():
 f=request.files.get("image")
 if not f or not f.filename:return jsonify(error="Please upload an image."),400
 p=Path("uploads")/secure_filename(f.filename); f.save(p)
 if model and classes:
  import numpy as np
  from tensorflow.keras.utils import load_img,img_to_array
  a=img_to_array(load_img(p,target_size=(224,224)))/255.; a=np.expand_dims(a,0)
  q=model.predict(a,verbose=0)[0]; i=int(np.argmax(q))
  return jsonify(disease=classes[i],confidence=round(float(q[i])*100,2),description="Prediction from the connected machine-learning model.",recommendation="Confirm the result with an agricultural expert before treatment.")
 return jsonify(setup_required=True,message="The website is working. Add model/model.h5 and model/classes.txt to enable real disease prediction.")
app.run(debug=True)
