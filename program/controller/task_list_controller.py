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
    
    def addTaskToDatabase(self, customTaskDescription, customTaskPoints):
        self.ref.child(customTaskDescription).set({"completed": False, "score": customTaskPoints})

    def get_total_score(self):
        tasks = self.fetch_from_firebase()
        return sum(task["score"] for task in tasks.values() if task["completed"])
    
    def get_max_score(self):
        return 100
    
    def getProgressBarValue(self):
        return int((self.get_total_score() / self.get_max_score()) * 100)
    
