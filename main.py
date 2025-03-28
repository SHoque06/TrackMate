from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from ui_mainwindow import Ui_MainWindow  # Import converted UI
from ui_progress import Ui_progressDisplay

class ProgressDisplay(Ui_progressDisplay, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Initialize UI

        self.progressDisplay = ProgressDisplay()
        self.display.addWidget(self.progressDisplay)

        self.progressButton.clicked.connect(self.progressButtonClicked)
        self.goalButton.clicked.connect(self.goalButtonClicked)
        self.logButton.clicked.connect(self.logButtonClicked)
        self.profileButton.clicked.connect(self.profileButtonClicked)

    def progressButtonClicked(self):
        self.display.setCurrentWidget(self.progressDisplay)

    def goalButtonClicked(self):
        print("goal")

    def logButtonClicked(self):
        print("log")

    def profileButtonClicked(self):
        print("profile")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()