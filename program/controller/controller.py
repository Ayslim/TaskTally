import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from program.model.writeDB import WriteDB
from program.model.readDB import ReadDB


class Controller:
    def __init__(self) -> None:
        self.write_db = WriteDB()
        self.read_db = ReadDB()


if __name__ == "__main__":
    controller = Controller()
    print("Controller initialized successfully.")