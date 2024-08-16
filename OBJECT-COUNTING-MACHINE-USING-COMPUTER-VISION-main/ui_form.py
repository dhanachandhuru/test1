# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1184, 747)
        MainWindow.setStyleSheet("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QToolButton\" name=\"startButton\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>230</x>\n"
"     <y>440</y>\n"
"     <width>80</width>\n"
"     <height>80</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">border: no-border;</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>...</string>\n"
"   </property>\n"
"   <property name=\"icon\">\n"
"    <iconset>\n"
"     <normaloff>C:/Users/91969/Desktop/arecanut_img_processing-main/GUI/Images/play.png</normaloff>C:/Users/91969/Desktop/arecanut_img_processing-main/GUI/Images/play.png</iconset>\n"
"   </property>\n"
"   <property name=\"iconSize\">\n"
"    <size>\n"
"     <width>80</width>\n"
"     <height>80</height>\n"
"    </size>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QLCDNumber\" name=\"lcdVol\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>830</x>\n"
"     <y>60</y>\n"
"     <width>200</width>\n"
"     <height>60</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">color: rgb(255, 85, 0);\n"
"border: 5px solid white;</string>\n"
"   </property>\n"
"   <property name=\"value\" stdset=\"0\">\n"
"    <double>15.000000000000000</double>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QLineEdit\" name=\"lineEdit\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>760</x>\n"
"     <y>140</y>\n"
"     <width>300</width>\n"
"     <height>4</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">background-color: rgb(255, 85, 0);\n"
"</string>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QToolButton\" name=\"shutDownButton_2\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>960</x>\n"
"     <y>480</y>\n"
"     <width>50</width>\n"
"     <height>50</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">border: no-border;</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>...</string>\n"
"   </property>\n"
"   <property name=\"icon\">\n"
"    <iconset>\n"
"     <normaloff>C:/Users/91969/Desktop/arecanut_img_processing-main/GUI/Images/shutdown.png</normaloff>C:/Users/91969/Desktop/arecanut_img_processing-main/GUI/Images/shutdown.png</iconset>\n"
"   </property>\n"
"   <property name=\"iconSize\">\n"
"    <size>\n"
"     <width>80</width>\n"
"     <height>80</height>\n"
"    </size>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QLCDNumber\" name=\"lcdDensity\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>830</x>\n"
"     <y>380</y>\n"
"     <width>200</width>\n"
"     <height>60</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">color: rgb(255, 85, 0);\n"
"border: 5px solid white;</string>\n"
"   </property>\n"
"   <property name=\"value\" stdset=\"0\">\n"
"    <double>10.000000000000000</double>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QLineEdit\" name=\"lineEdit_2\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>760</x>\n"
"     <y>320</y>\n"
"     <width>300</width>\n"
"     <height>4</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">background-color: rgb(255, 85, 0);\n"
"</string>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QFrame\" name=\"frame\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>60</x>\n"
"     <y>150</y>\n"
"     <width>671</width>\n"
"     <height>271</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">border: 5px solid rgb(255, 85, 0);\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);</string>\n"
"   </property>\n"
"   <property name=\"frameShape\">\n"
"    <enum>QFrame::StyledPanel</enum>\n"
"   </property>\n"
"   <property name=\"frameShadow\">\n"
"    <enum>QFrame::Raised</enum>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"Line\" name=\"line_4\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>1060</x>\n"
"     <y>10</y>\n"
"     <width>4</width>\n"
"     <height>530</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">background-color: rgb(255, 85, 0);</string>\n"
"   </property>\n"
"   <property name=\"orientation\">\n"
"    <enum>Qt::Vertical</enum>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QToolButton\" name=\"stoplButton\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>470</x>\n"
"     <y>440</y>\n"
"     <width>80</width>\n"
"     <height>80</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">border: no-border;</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>...</string>\n"
"   </property>\n"
"   <property name=\"icon\">\n"
"    <iconset>\n"
"     <normaloff>C:/Users/91969/Desktop/arecanut_img_processing-main/GUI/Images/stop.png</normaloff>C:/Users/91969/Desktop/arecanut_img_processing-main/GUI/Images/stop.png</iconset>\n"
"   </property>\n"
"   <property name=\"iconSize\">\n"
"    <size>\n"
"     <width>80</width>\n"
"     <height>80</height>\n"
"    </size>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QLineEdit\" name=\"lineEdit_3\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>760</x>\n"
"     <y>460</y>\n"
"     <width>300</width>\n"
"     <height>4</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">background-color: rgb(255, 85, 0);\n"
"</string>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QPushButton\" name=\"pushButton\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>920</x>\n"
"     <y>277</y>\n"
"     <width>80</width>\n"
"     <height>30</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"font\">\n"
"    <font>\n"
"     <family>Arial</family>\n"
"     <pointsize>12</pointsize>\n"
"     <weight>75</weight>\n"
"     <bold>true</bold>\n"
"    </font>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">\n"
"\n"
"QPushButton\n"
"        {\n"
"            color: white;\n"
"             background-color: rgb(255, 85, 0);\n"
"            border: 5px rgb(255, 85, 0) solid;\n"
"            font-weight: bold;\n"
"            outline: none;\n"
"        }\n"
"        QPushButton:hover{\n"
"            border: 1px #C6C6C6 solid;\n"
"            color: #fff;\n"
"            background-color: rgb(0, 255, 255) ;\n"
"        }</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>Tare</string>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QLabel\" name=\"label\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>800</x>\n"
"     <y>270</y>\n"
"     <width>51</width>\n"
"     <height>41</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"font\">\n"
"    <font>\n"
"     <family>Arial</family>\n"
"     <pointsize>20</pointsize>\n"
"     <weight>75</weight>\n"
"     <bold>true</bold>\n"
"    </font>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">color: rgb(255, 85, 0);</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>gm.</string>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QLabel\" name=\"label_6\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>310</x>\n"
"     <y>100</y>\n"
"     <width>201</width>\n"
"     <height>31</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"font\">\n"
"    <font>\n"
"     <family>Arial</family>\n"
"     <pointsize>16</pointsize>\n"
"     <weight>75</weight>\n"
"     <bold>true</bold>\n"
"    </font>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">color: rgb(255, 255, 255);</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>Camera View</string>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QLabel\" name=\"label_2\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>780</x>\n"
"     <y>20</y>\n"
"     <width>81</width>\n"
"     <height>31</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"font\">\n"
"    <font>\n"
"     <family>Arial</family>\n"
"     <pointsize>14</pointsize>\n"
"     <weight>75</weight>\n"
"     <bold>true</bold>\n"
"    </font>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">color: rgb(255, 255, 255);</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>Volume</string>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QLabel\" name=\"label_4\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>780</x>\n"
"     <y>340</y>\n"
"     <width>101</width>\n"
"     <height>31</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"font\">\n"
"    <font>\n"
"     <family>Arial</family>\n"
"     <pointsize>14</pointsize>\n"
"     <weight>75</weight>\n"
"     <bold>true</bold>\n"
"    </font>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">color: rgb(255, 255, 255);</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>Desnsity</string>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"Line\" name=\"line\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>20</x>\n"
"     <y>10</y>\n"
"     <width>4</width>\n"
"     <height>530</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">background-color: rgb(255, 85, 0);</string>\n"
"   </property>\n"
"   <property name=\"orientation\">\n"
"    <enum>Qt::Vertical</enum>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"Line\" name=\"line_5\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>760</x>\n"
"     <y>10</y>\n"
"     <width>4</width>\n"
"     <height>530</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">background-color: rgb(255, 85, 0);</string>\n"
"   </property>\n"
"   <property name=\"orientation\">\n"
"    <enum>Qt::Vertical</enum>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QLabel\" name=\"label_5\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>80</x>\n"
"     <y>40</y>\n"
"     <width>631</width>\n"
"     <height>41</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"font\">\n"
"    <font>\n"
"     <family>Arial</family>\n"
"     <pointsize>20</pointsize>\n"
"     <weight>75</weight>\n"
"     <bold>true</bold>\n"
"    </font>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">color: rgb(255, 85, 0);</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>DENSITY BASED ARECA NUT SORTING</string>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"Line\" name=\"line_2\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>20</x>\n"
"     <y>540</y>\n"
"     <width>1042</width>\n"
"     <height>4</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">background-color: rgb(255, 85, 0);</string>\n"
"   </property>\n"
"   <property name=\"orientation\">\n"
"    <enum>Qt::Horizontal</enum>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"Line\" name=\"line_3\">\n"
"   <property name=\"enabled\">\n"
"    <bool>false</bool>\n"
"   </property>\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>20</x>\n"
"     <y>10</y>\n"
"     <width>1042</width>\n"
"     <height>4</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"autoFillBackground\">\n"
"    <bool>false</bool>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">background-color: rgb(255, 85, 0);</string>\n"
"   </property>\n"
"   <property name=\"orientation\">\n"
"    <enum>Qt::Horizontal</enum>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QLCDNumber\" name=\"lcdWt\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>830</x>\n"
"     <y>197</y>\n"
"     <width>200</width>\n"
"     <height>60</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">color: rgb(255, 85, 0);\n"
"border: 5px solid white;</string>\n"
"   </property>\n"
"   <property name=\"value\" stdset=\"0\">\n"
"    <double>10.000000000000000</double>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QLabel\" name=\"label_3\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>780</x>\n"
"     <y>157</y>\n"
"     <width>81</width>\n"
"     <height>31</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"font\">\n"
"    <font>\n"
"     <family>Arial</family>\n"
"     <pointsize>14</pointsize>\n"
"     <weight>75</weight>\n"
"     <bold>true</bold>\n"
"    </font>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">color: rgb(255, 255, 255);</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>Weight</string>\n"
"   </property>\n"
"  </widget>\n"
"  <widget class=\"QToolButton\" name=\"settingButton\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>800</x>\n"
"     <y>480</y>\n"
"     <width>50</width>\n"
"     <height>55</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">border: no-border;</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>...</string>\n"
"   </property>\n"
"   <property name=\"icon\">\n"
"    <iconset>\n"
"     <normaloff>C:/Users/91969/Desktop/arecanut_img_processing-main/GUI/Images/settings_prev.png</normaloff>C:/Users/91969/Desktop/arecanut_img_processing-main/GUI/Images/settings_prev.png</iconset>\n"
"   </property>\n"
"   <property name=\"iconSize\">\n"
"    <size>\n"
"     <width>80</width>\n"
"     <height>80</height>\n"
"    </size>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self._2 = QtWidgets.QGridLayout()
        self._2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self._2.setContentsMargins(0, -1, -1, -1)
        self._2.setSpacing(0)
        self._2.setObjectName("_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stoplButton = QtWidgets.QToolButton(self.frame)
        self.stoplButton.setMinimumSize(QtCore.QSize(0, 0))
        self.stoplButton.setStyleSheet("border: no-border;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/91969/Desktop/arecanut_img_processing-main/GUI/Images/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stoplButton.setIcon(icon)
        self.stoplButton.setIconSize(QtCore.QSize(80, 80))
        self.stoplButton.setObjectName("stoplButton")
        self.horizontalLayout_3.addWidget(self.stoplButton)
        self.startButton = QtWidgets.QToolButton(self.frame)
        self.startButton.setMinimumSize(QtCore.QSize(0, 0))
        self.startButton.setStyleSheet("border: no-border;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/91969/Desktop/arecanut_img_processing-main/GUI/Images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon1)
        self.startButton.setIconSize(QtCore.QSize(80, 80))
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_3.addWidget(self.startButton)
        self._2.addLayout(self.horizontalLayout_3, 24, 8, 1, 11)
        self.lcdDensity = QtWidgets.QLCDNumber(self.frame)
        self.lcdDensity.setEnabled(True)
        self.lcdDensity.setStyleSheet("color: rgb(255, 85, 0);\n"
"border: 5px solid white;\n"
"border-radius: 10px;\n"
"")
        self.lcdDensity.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhUppercaseOnly)
        self.lcdDensity.setFrameShape(QtWidgets.QFrame.HLine)
        self.lcdDensity.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdDensity.setLineWidth(4)
        self.lcdDensity.setMidLineWidth(3)
        self.lcdDensity.setSmallDecimalPoint(False)
        self.lcdDensity.setProperty("value", 0.0)
        self.lcdDensity.setProperty("intValue", 0)
        self.lcdDensity.setObjectName("lcdDensity")
        self._2.addWidget(self.lcdDensity, 18, 28, 3, 3)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(85, 170, 0);")
        self.label_5.setObjectName("label_5")
        self._2.addWidget(self.label_5, 2, 5, 3, 18)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 4))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self._2.addWidget(self.lineEdit_2, 15, 27, 1, 5)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self._2.addWidget(self.label_2, 2, 28, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 4))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self._2.addWidget(self.lineEdit_3, 7, 27, 1, 5)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setEnabled(False)
        self.line_3.setAutoFillBackground(False)
        self.line_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self._2.addWidget(self.line_3, 0, 1, 1, 31)
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setEnabled(False)
        self.line_4.setAutoFillBackground(False)
        self.line_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self._2.addWidget(self.line_4, 28, 0, 1, 33)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("border: 5px solid rgb(255, 85, 0);\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self._2.addWidget(self.frame_2, 7, 2, 15, 23)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self._2.addWidget(self.label_3, 9, 28, 1, 1)
        self.shutDownButton_2 = QtWidgets.QToolButton(self.frame)
        self.shutDownButton_2.setStyleSheet("border: no-border;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/91969/Desktop/arecanut_img_processing-main/GUI/Images/shutdown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shutDownButton_2.setIcon(icon2)
        self.shutDownButton_2.setIconSize(QtCore.QSize(80, 80))
        self.shutDownButton_2.setObjectName("shutDownButton_2")
        self._2.addWidget(self.shutDownButton_2, 24, 27, 1, 5, QtCore.Qt.AlignHCenter)
        self.line_8 = QtWidgets.QFrame(self.frame)
        self.line_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self._2.addWidget(self.line_8, 0, 32, 26, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 4))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self._2.addWidget(self.lineEdit, 22, 27, 1, 5)
        self.lcdVol = QtWidgets.QLCDNumber(self.frame)
        self.lcdVol.setStyleSheet("color: rgb(255, 85, 0);\n"
"border: 5px solid rgb(57, 4, 162);\n"
"border-radius: 10px;")
        self.lcdVol.setProperty("value", 0.0)
        self.lcdVol.setProperty("intValue", 0)
        self.lcdVol.setObjectName("lcdVol")
        self._2.addWidget(self.lcdVol, 3, 28, 3, 3)
        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self._2.addWidget(self.label_6, 5, 4, 1, 20, QtCore.Qt.AlignHCenter)
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self._2.addWidget(self.line_6, 0, 0, 26, 1)
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setMaximumSize(QtCore.QSize(3, 16777215))
        self.line_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self._2.addWidget(self.line_5, 1, 26, 25, 1)
        self.lcdWt = QtWidgets.QLCDNumber(self.frame)
        self.lcdWt.setStyleSheet("color: rgb(255, 85, 0);\n"
"border: 5px solid white;\n"
"border-radius: 10px;")
        self.lcdWt.setProperty("value", 0.0)
        self.lcdWt.setProperty("intValue", 0)
        self.lcdWt.setObjectName("lcdWt")
        self._2.addWidget(self.lcdWt, 10, 28, 3, 3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self._2.addWidget(self.label_4, 17, 28, 1, 2)
        self.verticalLayout_2.addLayout(self._2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stoplButton.setText(_translate("MainWindow", "..."))

        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">PLASTIC DETECTION</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Plastic"))
        self.label_3.setText(_translate("MainWindow", "Not Plastic"))
        self.shutDownButton_2.setText(_translate("MainWindow", "..."))
        self.label_6.setText(_translate("MainWindow", "Camera View"))
        self.label_4.setText(_translate("MainWindow", "Result"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
try:
    sys.exit(app.exec_())
except:
    print('exiting')