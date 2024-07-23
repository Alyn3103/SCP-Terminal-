# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SCPFnalV1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 661)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Wallpaper = QtWidgets.QLabel(self.centralwidget)
        self.Wallpaper.setGeometry(QtCore.QRect(0, 0, 1061, 661))
        self.Wallpaper.setText("")
        self.Wallpaper.setPixmap(QtGui.QPixmap(":/BG/Image/SCPLogo.jpg"))
        self.Wallpaper.setScaledContents(True)
        self.Wallpaper.setObjectName("Wallpaper")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(710, 40, 311, 341))
        self.Image.setStyleSheet("QLabel {\n"
"    border: 1px solid #555555;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.Image.setScaledContents(True)
        self.Image.setObjectName("Image")
        self.Search = QtWidgets.QLineEdit(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(330, 10, 371, 31))
        self.Search.setStyleSheet("QLineEdit {\n"
"    background-color: #1E1E1E;\n"
"    border: 2px solid #555555;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    color: #CCCCCC;\n"
"    font-size: 14pt;\n"
"    selection-background-color: #555555;\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #AAAAAA;\n"
"}")
        self.Search.setObjectName("Search")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(63, 71, 140, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name = QtWidgets.QLabel(self.layoutWidget)
        self.name.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setScaledContents(True)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.Number = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Number.setFont(font)
        self.Number.setStyleSheet("QLabel {\n"
"    color: #CCCCCC;\n"
"\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14pt;\n"
"}\n"
"")
        self.Number.setText("")
        self.Number.setScaledContents(True)
        self.Number.setObjectName("Number")
        self.horizontalLayout.addWidget(self.Number)
        self.Searchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Searchbutton.setGeometry(QtCore.QRect(660, 10, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Searchbutton.setFont(font)
        self.Searchbutton.setStyleSheet("QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    border: 2px solid #555555;    \n"
"    border-radius: 10px;\n"
"    color: #CCCCCC;\n"
"    font-size: 14pt;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2E2E2E;\n"
"    border: 2px solid #AAAAAA;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #3E3E3E;\n"
"}")
        self.Searchbutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Image/Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Searchbutton.setIcon(icon)
        self.Searchbutton.setCheckable(False)
        self.Searchbutton.setObjectName("Searchbutton")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 130, 281, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Object = QtWidgets.QLabel(self.layoutWidget1)
        self.Object.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Object.setFont(font)
        self.Object.setObjectName("Object")
        self.horizontalLayout_2.addWidget(self.Object)
        self.Class = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Class.setFont(font)
        self.Class.setStyleSheet("QLabel {\n"
"    color: #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14pt;\n"
"}\n"
"")
        self.Class.setText("")
        self.Class.setObjectName("Class")
        self.horizontalLayout_2.addWidget(self.Class)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(60, 200, 281, 61))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Clerance = QtWidgets.QLabel(self.layoutWidget2)
        self.Clerance.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Clerance.setFont(font)
        self.Clerance.setObjectName("Clerance")
        self.horizontalLayout_3.addWidget(self.Clerance)
        self.ClearnaceNo = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ClearnaceNo.setFont(font)
        self.ClearnaceNo.setStyleSheet("QLabel {\n"
"    color: #CCCCCC;\n"
"\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14pt;\n"
"}\n"
"")
        self.ClearnaceNo.setText("")
        self.ClearnaceNo.setObjectName("ClearnaceNo")
        self.horizontalLayout_3.addWidget(self.ClearnaceNo)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(60, 270, 621, 251))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Descrip = QtWidgets.QLabel(self.layoutWidget3)
        self.Descrip.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Descrip.sizePolicy().hasHeightForWidth())
        self.Descrip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Descrip.setFont(font)
        self.Descrip.setObjectName("Descrip")
        self.verticalLayout.addWidget(self.Descrip)
        self.Detail = QtWidgets.QLabel(self.layoutWidget3)
        self.Detail.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Detail.setFont(font)
        self.Detail.setStyleSheet("QLabel {\n"
"    color: #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 14pt;\n"
"}\n"
"")
        self.Detail.setText("")
        self.Detail.setScaledContents(True)
        self.Detail.setObjectName("Detail")
        self.verticalLayout.addWidget(self.Detail)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "SCP-"))
        self.Object.setText(_translate("MainWindow", "Object Class:"))
        self.Clerance.setText(_translate("MainWindow", "Clearance Level:"))
        self.Descrip.setText(_translate("MainWindow", "Description:"))
import Resource_rc
import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
