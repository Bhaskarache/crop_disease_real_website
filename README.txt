REAL WEBSITE SETUP
1. Install Python 3.10+.
2. Open terminal in this folder.
3. Run: pip install -r requirements.txt
4. Run: python app.py
5. Open http://127.0.0.1:5000

REAL MODEL
Put a trained Keras model at model/model.h5 and its class names at model/classes.txt.
The model should accept 224x224 RGB images and output one probability per class.
Without a trained model, the website will NOT fake a disease result; it will tell you to add the model.
