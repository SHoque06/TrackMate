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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)


class Ui_progressDisplay(object):
    def setupUi(self, progressDisplay):
        if not progressDisplay.objectName():
            progressDisplay.setObjectName(u"progressDisplay")
        progressDisplay.resize(750, 370)
        self.label = QLabel(progressDisplay)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 200, 331, 181))

        self.retranslateUi(progressDisplay)

        QMetaObject.connectSlotsByName(progressDisplay)
    # setupUi

    def retranslateUi(self, progressDisplay):
        progressDisplay.setWindowTitle(QCoreApplication.translate("progressDisplay", u"Form", None))
        self.label.setText(QCoreApplication.translate("progressDisplay", u"progress display", None))
    # retranslateUi

