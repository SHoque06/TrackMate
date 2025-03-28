from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow  # Import converted UI

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Initialize UI

        self.progressButton.clicked.connect(self.progressButtonClicked)
        self.GoalButton.clicked.connect(self.goalButtonClicked)
        self.logButton.clicked.connect(self.logButtonClicked)
        self.profileButton.clicked.connect(self.profileButtonClicked)

    def progressButtonClicked(self):
        print("progress")

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