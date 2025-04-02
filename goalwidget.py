from PySide6.QtWidgets import QWidget
from ui_goalwidget import Ui_goalwidgetDisplay

class goalwidgetDisplay(Ui_goalwidgetDisplay, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)