# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QSizePolicy, QWidget)

class Ui_progressDisplay(object):
    def setupUi(self, progressDisplay):
        if not progressDisplay.objectName():
            progressDisplay.setObjectName(u"progressDisplay")
        progressDisplay.resize(700, 800)
        self.progressGraph = QWidget(progressDisplay)
        self.progressGraph.setObjectName(u"progressGraph")
        self.progressGraph.setGeometry(QRect(150, 20, 521, 471))
        self.progressGraph.setStyleSheet(u"background-color: white;")
        self.exerciseMenu = QComboBox(progressDisplay)
        self.exerciseMenu.addItem("")
        self.exerciseMenu.addItem("")
        self.exerciseMenu.setObjectName(u"exerciseMenu")
        self.exerciseMenu.setGeometry(QRect(10, 20, 121, 24))

        self.retranslateUi(progressDisplay)

        QMetaObject.connectSlotsByName(progressDisplay)
    # setupUi

    def retranslateUi(self, progressDisplay):
        progressDisplay.setWindowTitle(QCoreApplication.translate("progressDisplay", u"Form", None))
        self.exerciseMenu.setItemText(0, QCoreApplication.translate("progressDisplay", u"exercise 1", None))
        self.exerciseMenu.setItemText(1, QCoreApplication.translate("progressDisplay", u"exercise 2", None))

    # retranslateUi

