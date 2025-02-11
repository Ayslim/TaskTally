import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from program.controller.controller import Controller


class TestDatabase:
    def __init__(self, parent=None):
        self.controller = Controller()


if __name__ == "__main__":
    test = TestDatabase()
    print("Database test initialized.")
