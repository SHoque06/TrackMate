# Prog-Group-CW
TrackMate Gym App

Programming 2 Group Coursework, Year 1

To convert UI file to python class: pyside6-uic filename.ui -o ui_classname.py

Explanation of how stacked widget works (used for display): https://www.youtube.com/watch?v=Vq1laKeSk9M

To create a new UI that is displayed within the display:
    1. Qt Designer File->New->Widget, design the ui.
    2. Save .ui file and generate a python class (above), import into main.py - all same as with mainwindow
    3. Create a wrapper class inheriting from QWidget in main.py (QStackedWidget can only stack objects that are QWidgets themselves) e.g.
        class ProgressDisplay(Ui_progressDisplay, QWidget):
            def __init__(self):
                super().__init__()
                self.setupUi(self)
    4. Instantiate the wrapper class in the constructor of mainwindow, and add it to the QStackedWidget (display):
        self.progressDisplay = ProgressDisplay()
        self.display.addWidget(self.progressDisplay)
    5. self.display.setCurrentWidget(self.progressDisplay) will change the display to the ui at runtime.
