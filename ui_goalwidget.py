from PySide6.QtCore import (QCoreApplication, QRect, QMetaObject, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QLineEdit, QListWidget, QPushButton, QWidget)


class Ui_goalwidgetDisplay(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(500, 400)
        widget.setStyleSheet("""
            QWidget {
                background-color: #f0f4f8;
                font-family: 'Segoe UI';
                font-size: 14px;
            }
            QLabel {
                color: #333;
                font-size: 20px;
                font-weight: bold;
            }
            QLineEdit {
                padding: 6px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #fff;
            }
            QPushButton {
                padding: 6px;
                border: none;
                border-radius: 5px;
                background-color: #007BFF;
                color: white;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QListWidget {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)

        self.label = QLabel(widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 200, 40))
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)

        self.goalList = QListWidget(widget)
        self.goalList.setObjectName(u"goalList")
        self.goalList.setGeometry(QRect(30, 70, 440, 180))

        self.inputGoal = QLineEdit(widget)
        self.inputGoal.setObjectName(u"inputGoal")
        self.inputGoal.setGeometry(QRect(30, 270, 300, 30))

        self.addgoal = QPushButton(widget)
        self.addgoal.setObjectName(u"addgoal")
        self.addgoal.setGeometry(QRect(340, 270, 60, 30))

        self.removegoal = QPushButton(widget)
        self.removegoal.setObjectName(u"removegoal")
        self.removegoal.setGeometry(QRect(410, 270, 60, 30))

        self.retranslateUi(widget)
        QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Goal Tracker", None))
        self.label.setText(QCoreApplication.translate("widget", u"Your Goals", None))
        self.addgoal.setText(QCoreApplication.translate("widget", u"+", None))
        self.removegoal.setText(QCoreApplication.translate("widget", u"-", None))