import firebase_admin
from firebase_admin import db, credentials

# authenticate to firebase
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, { "databaseURL": "https://tasktally-d09dd-default-rtdb.europe-west1.firebasedatabase.app"})

# creating reference to root node 
ref = db.reference("/")

# retrieving from root node
ref.get()
print(db.reference("/tasks").get())

# set operation
""" db.reference("/tasks").set()
ref.get() """

""" def read_test(self):
        task_list = self.database.child("tasks").get()
        
        for task in task_list:
            print(task) """
