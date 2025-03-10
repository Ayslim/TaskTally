import pytest
from unittest.mock import MagicMock
from PyQt5.QtWidgets import QApplication
from program.view.task_page import TaskPage
app = QApplication([])

@pytest.fixture
def mock_controller():
    controller = MagicMock()
    controller.fetch_from_firebase.return_value = {
        "Clean your room": {"completed": True, "score": 10},
        "Do homework": {"completed": False, "score": 20},
    }
    return controller

@pytest.fixture
def task_page(mock_controller):
    """Create instance of TaskPage"""
    return TaskPage(mock_controller)

def test_reset_all_tasks_n_total_score(task_page):
    """Test that resetAllTasks() unchecks all tasks
      updateTotalScore() calculates again properly"""
    
    # Initialise all tasks
    assert task_page.totalScore.text() != "0"  # Before reset, score may not be 0

    # Reset all tasks
    task_page.resetAllTasks()

    # Make sure all tasks are unchecked
    for item in task_page.get_list_of_QListWidgetItems():
        assert item.checkState() == 0  # QtCore.Qt.Unchecked

    # Check that total score is equal 0
    assert task_page.totalScore.text() == "0"
