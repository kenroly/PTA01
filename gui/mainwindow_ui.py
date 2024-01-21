# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSplitter, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet(u"padding: 10px")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainSplitter = QSplitter(self.centralWidget)
        self.mainSplitter.setObjectName(u"mainSplitter")
        self.mainSplitter.setOrientation(Qt.Horizontal)
        self.leftPanel = QWidget(self.mainSplitter)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftLayout = QVBoxLayout(self.leftPanel)
        self.leftLayout.setObjectName(u"leftLayout")
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.headerLabel = QLabel(self.leftPanel)
        self.headerLabel.setObjectName(u"headerLabel")

        self.headerLayout.addWidget(self.headerLabel)

        self.addNoteButton = QPushButton(self.leftPanel)
        self.addNoteButton.setObjectName(u"addNoteButton")

        self.headerLayout.addWidget(self.addNoteButton)


        self.leftLayout.addLayout(self.headerLayout)

        self.searchBar = QLineEdit(self.leftPanel)
        self.searchBar.setObjectName(u"searchBar")

        self.leftLayout.addWidget(self.searchBar)

        self.noteList = QListWidget(self.leftPanel)
        self.noteList.setObjectName(u"noteList")

        self.leftLayout.addWidget(self.noteList)

        self.mainSplitter.addWidget(self.leftPanel)
        self.rightPanel = QWidget(self.mainSplitter)
        self.rightPanel.setObjectName(u"rightPanel")
        self.rightLayout = QVBoxLayout(self.rightPanel)
        self.rightLayout.setObjectName(u"rightLayout")
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.noteTitle = QLineEdit(self.rightPanel)
        self.noteTitle.setObjectName(u"noteTitle")

        self.rightLayout.addWidget(self.noteTitle)

        self.noteContent = QTextEdit(self.rightPanel)
        self.noteContent.setObjectName(u"noteContent")

        self.rightLayout.addWidget(self.noteContent)

        self.mainSplitter.addWidget(self.rightPanel)

        self.horizontalLayout.addWidget(self.mainSplitter)

        MainWindow.setCentralWidget(self.centralWidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.headerLabel.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-size: 20pt; font-weight: bold;", None))
        self.headerLabel.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.addNoteButton.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"                                                        QPushButton {\n"
"                                                            border: none;\n"
"                                                            background-color: transparent;\n"
"                                                            font-size: 25pt;\n"
"                                                            color: black;\n"
"                                                        }\n"
"                                                        QPushButton:hover {\n"
"                                                            color: blue;\n"
"                                                        }\n"
"                                                        QPushButton:pressed {\n"
"                                                            color: red;\n"
"                                                        }\n"
"                                                    ", None))
        self.addNoteButton.setText(QCoreApplication.translate("MainWindow", u"                       +", None))
        self.searchBar.setStyleSheet(QCoreApplication.translate("MainWindow", u"border: 1px solid #cccccc; border-radius: 10px; padding: 5px;", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search notes...", None))
        self.noteTitle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter note title...", None))
    # retranslateUi

