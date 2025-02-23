import firebase_admin
from firebase_admin import db, credentials

class TaskListController:

    #Setting up the connection to the database:
    def __init__(self):
        cred = credentials.Certificate("credentials.json")
        firebase_admin.initialize_app(cred, { "databaseURL": "https://tasktally-d09dd-default-rtdb.europe-west1.firebasedatabase.app"})
        self.ref = db.reference("/tasks")

    #Gets tasks from the database:
    # [
    # {"Task 1": {"completed": True, "score": 5}},
    # {"Task 2": {"completed": False, "score": 10}}
    # ]
    def fetch_from_firebase(self):
        return self.ref.get()
    
    #Changes the completed status of a specific task:
    def set_completed_status_on_task(self, task_description, completed):
        return self.ref.child(task_description).update({"completed": completed})