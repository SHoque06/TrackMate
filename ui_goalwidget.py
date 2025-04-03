# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'goalwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_goalwidgetDisplay(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(400, 300)
        self.label = QLabel(widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 110, 47, 13))

        self.goalList = QListWidget(widget)
        self.goalList.setObjectName(u"goalList")
        self.goalList.setGeometry(QRect(140, 90, 256, 121))

        self.addgoal = QPushButton(widget)
        self.addgoal.setObjectName(u"addgoal")
        self.addgoal.setGeometry(QRect(30, 140, 75, 23))
        
        self.removegoal = QPushButton(widget)
        self.removegoal.setObjectName(u"removegoal")
        self.removegoal.setGeometry(QRect(20, 180, 75, 23))

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("widget", u"goals", None))
        self.addgoal.setText(QCoreApplication.translate("widget", u"add goal", None))
        self.removegoal.setText(QCoreApplication.translate("widget", u"remove goal", None))
    # retranslateUi

