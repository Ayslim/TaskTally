import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..')))
import pyrebase

class readDB:
    def __init__(self):
        config = {
            "apiKey": "AIzaSyBdeH9uelVdA54VNtFNtTiNXpWpI-qnVxw",
            "authDomain": "tasktally-d09dd.firebaseapp.com",
            "databaseURL": "https://tasktally-d09dd-default-rtdb.europe-west1.firebasedatabase.app",
            "projectId": "tasktally-d09dd",
            "storageBucket": "tasktally-d09dd.firebasestorage.app",
            "messagingSenderId": "892299139303",
            "appId": "1:892299139303:web:36373d6a48011b39536a42",
            "measurementId": "G-7GEWMKQSF2"
            }
        firebase = pyrebase.initialize_app(config)
        self.database = firebase.database()