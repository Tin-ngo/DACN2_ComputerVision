# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1251, 671)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    border-image: url(:/background/img/background.png);\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 220, 511, 411))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/C:/Users/Admin/Pictures/image_Tin/background2.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 170, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(730, 220, 511, 411))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/C:/Users/Admin/Pictures/image_Tin/sieunhan.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(730, 180, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.pushButtonsave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonsave.setGeometry(QtCore.QRect(900, 170, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButtonsave.setFont(font)
        self.pushButtonsave.setObjectName("pushButtonsave")
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setGeometry(QtCore.QRect(820, 170, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_reset.setFont(font)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(530, 220, 191, 271))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_removeBG = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_removeBG.setGeometry(QtCore.QRect(70, 30, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_removeBG.setFont(font)
        self.pushButton_removeBG.setObjectName("pushButton_removeBG")
        self.pushButton_blurBG = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_blurBG.setGeometry(QtCore.QRect(10, 90, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_blurBG.setFont(font)
        self.pushButton_blurBG.setObjectName("pushButton_blurBG")
        self.pushButton_grayBG = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_grayBG.setGeometry(QtCore.QRect(10, 150, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_grayBG.setFont(font)
        self.pushButton_grayBG.setObjectName("pushButton_grayBG")
        self.pushButton_changeBG = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_changeBG.setGeometry(QtCore.QRect(10, 210, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_changeBG.setFont(font)
        self.pushButton_changeBG.setObjectName("pushButton_changeBG")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 51, 31))
        self.comboBox.setObjectName("comboBox")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(530, 510, 191, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(80, 20, 31, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(80, 80, 31, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(80, 50, 31, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 20, 31, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 20, 31, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 80, 31, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 50, 31, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_7.setGeometry(QtCore.QRect(120, 50, 31, 21))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_8.setGeometry(QtCore.QRect(120, 80, 31, 21))
        self.pushButton_8.setObjectName("pushButton_8")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(170, 170, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1251, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Phần mềm xử lý ảnh cơ bản"))
        self.label_2.setText(_translate("MainWindow", "Ảnh gốc"))
        self.pushButton.setText(_translate("MainWindow", "Chọn ảnh"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>#ffffff</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Ảnh kết quả"))
        self.pushButtonsave.setText(_translate("MainWindow", "Lưu ảnh"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Xử lý nền ảnh"))
        self.pushButton_removeBG.setText(_translate("MainWindow", "Xóa bỏ nền ảnh"))
        self.pushButton_blurBG.setText(_translate("MainWindow", "Làm mờ nền ảnh"))
        self.pushButton_grayBG.setText(_translate("MainWindow", "Làm xám nền ảnh"))
        self.pushButton_changeBG.setText(_translate("MainWindow", "Thay đổi nền ảnh"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Màu"))
        self.label_5.setText(_translate("MainWindow", "Red"))
        self.label_6.setText(_translate("MainWindow", "Green"))
        self.label_7.setText(_translate("MainWindow", "Blue"))
        self.pushButton_3.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "+"))
        self.pushButton_5.setText(_translate("MainWindow", "-"))
        self.pushButton_6.setText(_translate("MainWindow", "-"))
        self.pushButton_7.setText(_translate("MainWindow", "+"))
        self.pushButton_8.setText(_translate("MainWindow", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
