# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graph.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(844, 608)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plot_widget = PlotWidget(self.centralwidget)
        self.plot_widget.setObjectName(u"plot_widget")

        self.verticalLayout.addWidget(self.plot_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.voltage_start = QDoubleSpinBox(self.centralwidget)
        self.voltage_start.setObjectName(u"voltage_start")
        self.voltage_start.setMaximum(3.300000000000000)
        self.voltage_start.setSingleStep(0.100000000000000)

        self.horizontalLayout.addWidget(self.voltage_start)

        self.voltage_end = QDoubleSpinBox(self.centralwidget)
        self.voltage_end.setObjectName(u"voltage_end")
        self.voltage_end.setMaximum(3.300000000000000)
        self.voltage_end.setSingleStep(0.100000000000000)
        self.voltage_end.setValue(3.300000000000000)

        self.horizontalLayout.addWidget(self.voltage_end)

        self.repeats = QSpinBox(self.centralwidget)
        self.repeats.setObjectName(u"repeats")
        self.repeats.setMinimum(1)
        self.repeats.setMaximum(1000)
        self.repeats.setValue(1)

        self.horizontalLayout.addWidget(self.repeats)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ports_combo = QComboBox(self.centralwidget)
        self.ports_combo.setObjectName(u"ports_combo")

        self.horizontalLayout_2.addWidget(self.ports_combo)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")

        self.horizontalLayout_2.addWidget(self.start_button)

        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout_2.addWidget(self.save_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.portlabel = QLabel(self.centralwidget)
        self.portlabel.setObjectName(u"portlabel")

        self.verticalLayout_2.addWidget(self.portlabel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 844, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.voltage_start.setPrefix(QCoreApplication.translate("MainWindow", u"Start voltage: ", None))
        self.voltage_end.setPrefix(QCoreApplication.translate("MainWindow", u"End voltage: ", None))
        self.repeats.setPrefix(QCoreApplication.translate("MainWindow", u"Repeats: ", None))
        self.ports_combo.setCurrentText("")
        self.ports_combo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose port", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start measurement", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save data", None))
        self.portlabel.setText("")
    # retranslateUi

