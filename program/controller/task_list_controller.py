import firebase_admin
from firebase_admin import db, credentials

class TaskListController:
    def __init__(self):
        cred = credentials.Certificate("credentials.json")
        firebase_admin.initialize_app(cred, { "databaseURL": "https://tasktally-d09dd-default-rtdb.europe-west1.firebasedatabase.app"})
        self.ref = db.reference("/tasks")

    def fetch_from_firebase(self):
        return self.ref.get()
    
    def set_in_firebase(self, task_description, completed):
        return self.ref.child(task_description).update({"completed": completed})