from PySide6.QtWidgets import QWidget
from ui_logworkout import Ui_logworkoutDisplay

class logworkoutDisplay(Ui_logworkoutDisplay, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)