from PySide6.QtWidgets import QWidget
from ui_workoutLogPage import Ui_WorkoutLogPage  

class logworkoutDisplay(Ui_WorkoutLogPage, QWidget):
    def __init__(self, database):
        super().__init__()
        self.setupUi(self)
        self.db = database
