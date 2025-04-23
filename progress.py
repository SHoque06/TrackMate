from PySide6.QtWidgets import QWidget
from ui_progress import Ui_progressDisplay

class ProgressDisplay(Ui_progressDisplay, QWidget):
    def __init__(self, database):
        super().__init__()
        self.setupUi(self)
        self.db = database