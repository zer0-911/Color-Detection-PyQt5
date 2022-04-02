# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2
from cv2 import line
import imutils
import time
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1112, 754)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 690, 111, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 690, 111, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 690, 131, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(750, 120, 351, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_2.addWidget(self.lineEdit_7)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 700, 600))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(
            "img/DisCov.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(790, 40, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(910, 40, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1020, 40, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(910, 100, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(790, 100, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1020, 100, 67, 17))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(750, 200, 67, 17))
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(750, 230, 113, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(890, 230, 113, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(870, 230, 67, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(750, 280, 161, 17))
        self.label_10.setObjectName("label_10")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(750, 310, 113, 25))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(750, 390, 113, 25))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(750, 360, 121, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(300, 660, 91, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(750, 640, 351, 91))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("img/DisLog.scv"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(750, 460, 67, 17))
        self.label_14.setObjectName("label_14")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(810, 480, 91, 27))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(990, 480, 91, 27))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(780, 490, 67, 17))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(960, 490, 67, 17))
        self.label_16.setObjectName("label_16")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(810, 520, 91, 27))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(920, 530, 67, 17))
        self.label_17.setObjectName("label_17")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(990, 520, 91, 27))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(750, 530, 81, 17))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(810, 570, 81, 17))
        self.label_19.setObjectName("label_19")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(890, 570, 91, 27))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(749, 66, 351, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.loadImage)
        self.pushButton_2.clicked.connect(self.Input_cam)
        self.lineEdit.returnPressed.connect(self.Path)
        self.lineEdit_2.cursorPositionChanged['int', 'int'].connect(
            self.LH)
        self.lineEdit_3.cursorPositionChanged['int', 'int'].connect(
            self.LS)
        self.lineEdit_4.cursorPositionChanged['int', 'int'].connect(
            self.LV)
        self.lineEdit_5.cursorPositionChanged['int', 'int'].connect(
            self.UH)
        self.lineEdit_6.cursorPositionChanged['int', 'int'].connect(
            self.US)
        self.lineEdit_7.cursorPositionChanged['int', 'int'].connect(
            self.UV)
        self.lineEdit_8.cursorPositionChanged['int', 'int'].connect(
            self.kernel_value1)
        self.lineEdit_9.cursorPositionChanged['int', 'int'].connect(
            self.kernel_value2)
        self.lineEdit_10.cursorPositionChanged['int', 'int'].connect(
            self.Erode_iter)
        self.lineEdit_11.cursorPositionChanged['int', 'int'].connect(
            self.Dilate_iter)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tmp = None
        self.kernel_value1_now = 11
        self.kernel_value2_now = 11
        self.UH_now = 179  # Updated UH value
        self.US_now = 255  # Updated US value
        self.UV_now = 255  # Updated UV value
        self.LH_now = 84  # Updated LH value
        self.LS_now = 98  # Updated LS value
        self.LV_now = 0  # Updated LV value
        self.started = False
        self.cam = True  # True for webcam
        self.path = ""  # Path to image
        self.dilate_iter_now = 2
        self.erode_iter_now = 2

    def loadImage(self):
        if self.started:
            self.started = False
            self.pushButton.setText('Start Video')
        else:
            self.started = True
            self.pushButton.setText('Stop Video')

        if self.cam:
            vid = cv2.VideoCapture(0)
        else:
            vid = cv2.VideoCapture(self.path)

        while(vid.isOpened()):
            QtWidgets.QApplication.processEvents()
            img, self.image = vid.read()
            self.image = imutils.resize(self.image, height=480)

            lower = (self.LH_now,  self.LS_now,  self.LV_now)
            upper = (self.UH_now, self.US_now, self.UV_now)
            print(lower, upper)
            print("UH = " + str(self.UH_now) + " US = " +
                  str(self.US_now) + " UV = " + str(self.UV_now))
            print("LH = " + str(self.LH_now) + " LS = " +
                  str(self.LS_now) + " LV = " + str(self.LV_now))
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            # blur
            blurred = cv2.GaussianBlur(
                self.image, (self.kernel_value1_now, self.kernel_value2_now), 0)
            print("Kernel = " + str(self.kernel_value1_now) + " " +
                  str(self.kernel_value2_now))

            print("Dilate = " + str(self.dilate_iter_now) + " Erode =" +
                  str(self.erode_iter_now))

            # HSV
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

            # masking
            mask = cv2.inRange(hsv, lower, upper)

            mask = cv2.erode(mask, None, iterations=self.erode_iter_now)
            mask = cv2.dilate(mask, None, iterations=self.dilate_iter_now)

            contours, _ = cv2.findContours(
                mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(contours) > 0:
                # max contour
                c = max(contours, key=cv2.contourArea)

                # kotak
                rect = cv2.minAreaRect(c)
                ((x, y), (width, height), rotation) = rect
                x = round(x, 2)
                self.textBrowser.append(str(x))
                y = round(y, 2)
                self.textBrowser_2.append(str(y))
                width = round(width, 2)
                self.textBrowser_3.append(str(width))
                height = round(height, 2)
                self.textBrowser_4.append(str(height))
                rotation = round(rotation, 2)
                self.textBrowser_5.append(str(rotation))
                # s = f"x {np.round(x)}, y: {np.round(y)}, width: {np.round(width)}, height: {np.round(height)}, rotation: {np.round(rotation)}"
                # print(s)

                # box
                box = cv2.boxPoints(rect)
                box = np.int64(box)

                # gambar contour
                cv2.drawContours(self.image, [box], 0, (0, 255, 255), 2)

            self.update()
            key = cv2.waitKey(1) & 0xFF
            if self.started == False:
                break
                print('Loop break')

    def setFrame(self, image):
        self.tmp = image
        image = imutils.resize(image, width=600)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(
            frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label_7.setPixmap(QtGui.QPixmap.fromImage(image))
        self.label_7.setScaledContents(True)

    def kernel_value1(self):
        self.kernel_value1_now = int(self.lineEdit_8.text())
        if(self.kernel_value1_now % 2 == 0):
            self.kernel_value1_now = self.kernel_value1_now - 1
        if(self.kernel_value1_now <= 0):
            self.kernel_value1_now = 1
        self.update()

    def kernel_value2(self):
        self.kernel_value2_now = int(self.lineEdit_9.text())
        if(self.kernel_value2_now % 2 == 0):
            self.kernel_value2_now = self.kernel_value2_now - 1
        if(self.kernel_value2_now <= 0):
            self.kernel_value2_now = 1
        self.update()

    def UH(self):
        # print(text)
        self.UH_now = int(self.lineEdit_5.text())
        if(self.UH_now < 0):
            self.UH_now = 0
        elif(self.UH_now > 255):
            self.UH_now = 255
        self.update()

    def US(self):
        # print(text)
        self.US_now = int(self.lineEdit_6.text())
        if(self.US_now < 0):
            self.US_now = 0
        elif(self.US_now > 255):
            self.US_now = 255
        self.update()

    def UV(self):
        # print(text)
        self.UV_now = int(self.lineEdit_7.text())
        if(self.UV_now < 0):
            self.UV_now = 0
        elif(self.UV_now > 255):
            self.UV_now = 255
        self.update()

    def LH(self):
        # print(text)
        self.LH_now = int(self.lineEdit_2.text())
        if(self.LH_now < 0):
            self.LH_now = 0
        elif(self.LH_now > 255):
            self.LH_now = 255
        self.update()

    def LS(self):
        # print(text)
        self.LS_now = int(self.lineEdit_3.text())
        if(self.LS_now < 0):
            self.LS_now = 0
        elif(self.LS_now > 255):
            self.LS_now = 255
        self.update()

    def LV(self):
        # print(text)
        self.LV_now = int(self.lineEdit_4.text())
        if(self.LV_now < 0):
            self.LV_now = 0
        elif(self.LV_now > 255):
            self.LV_now = 255
        self.update()

    def Erode_iter(self):
        self.erode_iter_now = int(self.lineEdit_10.text())
        if(self.erode_iter_now < 0):
            self.erode_iter_now = 0
        self.update()

    def Dilate_iter(self):
        self.dilate_iter_now = int(self.lineEdit_11.text())
        if(self.dilate_iter_now < 0):
            self.dilate_iter_now = 0
        self.update()

    def Input_cam(self):
        if self.cam:
            self.cam = False
            self.pushButton.setText('Video')
        else:
            self.cam = True
            self.pushButton.setText('WebCam')
        self.update()

    def Path(self):
        self.path = self.lineEdit.text()
        self.update()

    def update(self):
        self.setFrame(self.image)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QtGui.QIcon('img/DisLog.png'))
        MainWindow.setWindowTitle(_translate("MainWindow", "Color Detection"))
        self.pushButton.setText(_translate("MainWindow", "Open Video"))
        self.pushButton_2.setText(_translate("MainWindow", "Input"))
        self.label.setText(_translate("MainWindow", "LH"))
        self.label_2.setText(_translate("MainWindow", "LS"))
        self.label_3.setText(_translate("MainWindow", "LV"))
        self.label_4.setText(_translate("MainWindow", "US"))
        self.label_5.setText(_translate("MainWindow", "UH"))
        self.label_6.setText(_translate("MainWindow", "UV"))
        self.label_8.setText(_translate("MainWindow", "Kernel"))
        self.label_9.setText(_translate("MainWindow", "X"))
        self.label_10.setText(_translate("MainWindow", "Erode (Iterations)"))
        self.label_11.setText(_translate("MainWindow", "Dilate (iterations)"))
        self.label_12.setText(_translate("MainWindow", "Path Video"))
        self.label_14.setText(_translate("MainWindow", "Output"))
        self.label_15.setText(_translate("MainWindow", "X ="))
        self.label_16.setText(_translate("MainWindow", "Y ="))
        self.label_17.setText(_translate("MainWindow", "Length ="))
        self.label_18.setText(_translate("MainWindow", "Width ="))
        self.label_19.setText(_translate("MainWindow", "Rotation = "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
