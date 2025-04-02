from PySide6.QtWidgets import QWidget
from ui_profilewidget import Ui_profilewidgetDisplay

class profilewidgetDisplay(Ui_profilewidgetDisplay, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)