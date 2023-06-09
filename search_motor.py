# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_motor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(831, 414)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setStyleSheet("#Form{\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"}")
        self.search_lineedit = QtWidgets.QLineEdit(Form)
        self.search_lineedit.setGeometry(QtCore.QRect(50, 40, 731, 51))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        font.setPointSize(19)
        self.search_lineedit.setFont(font)
        self.search_lineedit.setStyleSheet("border:3px solid black;\n"
"border-radius:15px;")
        self.search_lineedit.setText("")
        self.search_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.search_lineedit.setObjectName("search_lineedit")
        self.search_button = QtWidgets.QPushButton(Form)
        self.search_button.setGeometry(QtCore.QRect(200, 140, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.search_button.setFont(font)
        self.search_button.setStyleSheet("QPushButton{\n"
"    border:2px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    border:2px;\n"
"    border-radius: 15px;\n"
"    \n"
"    background-color: rgb(213, 213, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    border:2px;\n"
"    border-radius: 15px;\n"
"    \n"
"    background-color: rgb(113, 113, 56);\n"
"}")
        self.search_button.setObjectName("search_button")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 220, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.status = QtWidgets.QLabel(Form)
        self.status.setGeometry(QtCore.QRect(450, 220, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setStyleSheet("\n"
"color: rgb(255, 170, 127);")
        self.status.setObjectName("status")
        self.learn_button = QtWidgets.QPushButton(Form)
        self.learn_button.setGeometry(QtCore.QRect(320, 300, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.learn_button.setFont(font)
        self.learn_button.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.learn_button.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    border:2px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(170, 0, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    border:4px solid green;\n"
"    border-radius: 15px;\n"
"    \n"
"    background-color: rgb(56, 0, 85);\n"
"}\n"
"QPushButton:pressed{\n"
"    border:2px;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(113, 113, 56);\n"
"}")
        self.learn_button.setObjectName("learn_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.search_lineedit.setPlaceholderText(_translate("Form", "Search movie.."))
        self.search_button.setText(_translate("Form", "SEARCH ON DATABASE"))
        self.label.setText(_translate("Form", "STATUS : "))
        self.status.setText(_translate("Form", "NONE"))
        self.learn_button.setText(_translate("Form", "LEARN ABOUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())