# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASETvlMMh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

#PyQT5 imports
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 825)
        MainWindow.setMinimumSize(QSize(1100, 825))
        MainWindow.setMaximumSize(QSize(1600, 900))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/angle-double-right-solid.png) ;\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMinimumSize(QSize(32, 32))
        self.frame_icon_top_bar.setMaximumSize(QSize(34, 34))
        self.frame_icon_top_bar.setBaseSize(QSize(32, 32))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/Fontawsome/icons/fontawsome/TIGS-32x32.png) ;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_12 = QLabel(self.frame_label_top_btns)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background: transparent;")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)

        self.label_12.raise_()
        self.label_title_bar_top.raise_()
        self.frame_icon_top_bar.raise_()

        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_clean = QLabel(self.frame_top_info)
        self.label_top_clean.setObjectName(u"label_top_clean")
        self.label_top_clean.setStyleSheet(u"color: rgb(98, 103, 111);\n"
"font: bold;")

        self.horizontalLayout_8.addWidget(self.label_top_clean)

        self.label_TIGS_balanceAlivibe = QLabel(self.frame_top_info)
        self.label_TIGS_balanceAlivibe.setObjectName(u"label_TIGS_balanceAlivibe")
        self.label_TIGS_balanceAlivibe.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_8.addWidget(self.label_TIGS_balanceAlivibe)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setBold(True)
        font2.setWeight(75)
        self.label_top_info_2.setFont(font2)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)

        self.widget_LogOut = QWidget(self.frame_top_info)
        self.widget_LogOut.setObjectName(u"widget_LogOut")
        self.widget_LogOut.setMaximumSize(QSize(100, 16777215))
        self.pushButton_LoggoutEverywere = QPushButton(self.widget_LogOut)
        self.pushButton_LoggoutEverywere.setObjectName(u"pushButton_LoggoutEverywere")
        self.pushButton_LoggoutEverywere.setGeometry(QRect(20, 0, 75, 21))
        self.pushButton_LoggoutEverywere.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 9px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 10%;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_8.addWidget(self.widget_LogOut)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)

        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_unlock = QWidget()
        self.page_unlock.setObjectName(u"page_unlock")
        self.verticalLayout_10 = QVBoxLayout(self.page_unlock)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_4 = QFrame(self.page_unlock)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_4)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_67 = QFrame(self.frame_4)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.frame_72 = QFrame(self.frame_67)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setGeometry(QRect(10, 10, 951, 131))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_72)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(-10, 0, 431, 61))
        self.label_10.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")
        self.label_3 = QLabel(self.frame_72)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 70, 451, 41))
        self.frame_9 = QFrame(self.frame_72)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(550, 0, 81, 71))
        self.frame_9.setStyleSheet(u"background-image:url(:/Fontawsome/icons/fontawsome/Token_Pancake64x64.png);\n"
"background-repeat: no-reperat;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.frame_72)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(670, 40, 71, 71))
        self.frame_11.setStyleSheet(u"background-image: url(:/Fontawsome/icons/fontawsome/Token_Bakery64x64.png) ;\n"
"background-repeat: no-reperat;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_21.addWidget(self.frame_67)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        self.frame_8.setTabletTracking(False)
        self.frame_8.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.frame_69 = QFrame(self.frame_8)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setStyleSheet(u"border:0;")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_69)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.frame_69)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(250, 16777215))
        self.label.setStyleSheet(u"")

        self.verticalLayout_20.addWidget(self.label)

        self.comboBox_Accounts = QComboBox(self.frame_69)
        self.comboBox_Accounts.setObjectName(u"comboBox_Accounts")
        self.comboBox_Accounts.setMinimumSize(QSize(0, 100))
        self.comboBox_Accounts.setMaximumSize(QSize(250, 16777215))
        self.comboBox_Accounts.setStyleSheet(u"QComboBox {\n"
"	font-size: 24px ;\n"
"	font:bold;\n"
"	color: rgb(219, 160, 6);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	border-radius:25px;\n"
"}\n"
"")
        self.comboBox_Accounts.setFrame(True)

        self.verticalLayout_20.addWidget(self.comboBox_Accounts)


        self.horizontalLayout_45.addWidget(self.frame_69)

        self.frame_70 = QFrame(self.frame_8)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setStyleSheet(u"border:0;")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_70)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_Create_Wallet = QPushButton(self.frame_70)
        self.pushButton_Create_Wallet.setObjectName(u"pushButton_Create_Wallet")
        self.pushButton_Create_Wallet.setMinimumSize(QSize(250, 50))
        self.pushButton_Create_Wallet.setMaximumSize(QSize(250, 16777215))
        self.pushButton_Create_Wallet.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 25px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_6.addWidget(self.pushButton_Create_Wallet, 0, 0, 1, 1)

        self.pushButton_Import_Wallet = QPushButton(self.frame_70)
        self.pushButton_Import_Wallet.setObjectName(u"pushButton_Import_Wallet")
        self.pushButton_Import_Wallet.setMinimumSize(QSize(250, 50))
        self.pushButton_Import_Wallet.setMaximumSize(QSize(250, 16777215))
        self.pushButton_Import_Wallet.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 25px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_6.addWidget(self.pushButton_Import_Wallet, 1, 0, 1, 1)


        self.horizontalLayout_45.addWidget(self.frame_70)


        self.verticalLayout_21.addWidget(self.frame_8)

        self.frame_71 = QFrame(self.frame_4)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_71)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_74 = QFrame(self.frame_71)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_74)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.input_password = QLineEdit(self.frame_74)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setMinimumSize(QSize(471, 70))
        self.input_password.setStyleSheet(u"QLineEdit {\n"
"	font-size:24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 25px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setClearButtonEnabled(True)

        self.verticalLayout_23.addWidget(self.input_password)

        self.widget_wrong_pw = QWidget(self.frame_74)
        self.widget_wrong_pw.setObjectName(u"widget_wrong_pw")
        self.widget_wrong_pw.setEnabled(False)
        self.widget_wrong_pw.setMinimumSize(QSize(471, 41))
        self.widget_wrong_pw.setStyleSheet(u"\n"
"	    font-size:24px;\n"
"	    background-color: rgb(130, 0, 0) ;\n"
"		border: 6px solid rgb(33, 37, 43);\n"
"	    border-radius: 20px;\n"
"	    padding-left: 10px;\n"
"")
        self.verticalLayout_22 = QVBoxLayout(self.widget_wrong_pw)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_wrong_password = QLabel(self.widget_wrong_pw)
        self.label_wrong_password.setObjectName(u"label_wrong_password")
        self.label_wrong_password.setEnabled(False)
        self.label_wrong_password.setStyleSheet(u"background-color:rgba(0, 255, 0, 0);\n"
"border: 0 px solid rgb(33, 37, 43);")

        self.verticalLayout_22.addWidget(self.label_wrong_password)


        self.verticalLayout_23.addWidget(self.widget_wrong_pw)

        self.pushButton_Unlock_Wallet = QPushButton(self.frame_74)
        self.pushButton_Unlock_Wallet.setObjectName(u"pushButton_Unlock_Wallet")
        self.pushButton_Unlock_Wallet.setMinimumSize(QSize(470, 90))
        self.pushButton_Unlock_Wallet.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 35px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_Unlock_Wallet.setCheckable(False)
        self.pushButton_Unlock_Wallet.setAutoDefault(True)
        self.pushButton_Unlock_Wallet.setFlat(False)

        self.verticalLayout_23.addWidget(self.pushButton_Unlock_Wallet)


        self.gridLayout_5.addWidget(self.frame_74, 0, 1, 1, 1)

        self.frame_77 = QFrame(self.frame_71)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(200, 0))
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_77, 0, 0, 1, 1)

        self.frame_78 = QFrame(self.frame_71)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(200, 0))
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_78, 0, 2, 1, 1)

        self.frame_78.raise_()
        self.frame_77.raise_()
        self.frame_74.raise_()

        self.verticalLayout_21.addWidget(self.frame_71)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_unlock)
        self.page_sending = QWidget()
        self.page_sending.setObjectName(u"page_sending")
        self.verticalLayout_12 = QVBoxLayout(self.page_sending)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_41 = QFrame(self.page_sending)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 120))
        self.frame_41.setMaximumSize(QSize(16777215, 130))
        self.frame_41.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"border:0;")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.label_53 = QLabel(self.frame_42)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(100, 60, 331, 25))
        self.label_54 = QLabel(self.frame_42)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(0, 0, 401, 61))
        self.label_54.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")

        self.horizontalLayout_28.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_41)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"border:0;")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")

        self.horizontalLayout_28.addWidget(self.frame_43)


        self.verticalLayout_12.addWidget(self.frame_41)

        self.frame_19 = QFrame(self.page_sending)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"border-radius: 5px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_19)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_44 = QFrame(self.frame_19)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_44)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 250))
        self.frame_45.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_45)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_48 = QFrame(self.frame_45)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_46 = QFrame(self.frame_48)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_57 = QLabel(self.frame_46)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"")

        self.horizontalLayout_30.addWidget(self.label_57)

        self.comboBox_sending_Asset = QComboBox(self.frame_46)
        self.comboBox_sending_Asset.setObjectName(u"comboBox_sending_Asset")
        self.comboBox_sending_Asset.setMinimumSize(QSize(200, 0))
        self.comboBox_sending_Asset.setAutoFillBackground(False)
        self.comboBox_sending_Asset.setStyleSheet(u"QComboBox {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(219, 160, 6) ;\n"
"	border-radius: 25px;\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_30.addWidget(self.comboBox_sending_Asset)


        self.horizontalLayout_32.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.frame_48)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_58 = QLabel(self.frame_47)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"")

        self.horizontalLayout_31.addWidget(self.label_58)

        self.lineEdit_SendAsset_Balance = QLineEdit(self.frame_47)
        self.lineEdit_SendAsset_Balance.setObjectName(u"lineEdit_SendAsset_Balance")
        self.lineEdit_SendAsset_Balance.setMinimumSize(QSize(240, 0))
        self.lineEdit_SendAsset_Balance.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_SendAsset_Balance.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_SendAsset_Balance.setCursorPosition(11)
        self.lineEdit_SendAsset_Balance.setReadOnly(True)

        self.horizontalLayout_31.addWidget(self.lineEdit_SendAsset_Balance)

        self.label_60 = QLabel(self.frame_47)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_31.addWidget(self.label_60)

        self.lineEdit_SendBalanceUSD = QLineEdit(self.frame_47)
        self.lineEdit_SendBalanceUSD.setObjectName(u"lineEdit_SendBalanceUSD")
        self.lineEdit_SendBalanceUSD.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_31.addWidget(self.lineEdit_SendBalanceUSD)


        self.horizontalLayout_32.addWidget(self.frame_47)


        self.verticalLayout_14.addWidget(self.frame_48)

        self.frame_52 = QFrame(self.frame_45)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.frame_49 = QFrame(self.frame_52)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_56 = QLabel(self.frame_49)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"color: ;")

        self.horizontalLayout_34.addWidget(self.label_56)

        self.lineEdit_SendAmount = QLineEdit(self.frame_49)
        self.lineEdit_SendAmount.setObjectName(u"lineEdit_SendAmount")
        self.lineEdit_SendAmount.setMinimumSize(QSize(350, 0))
        self.lineEdit_SendAmount.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_SendAmount.setInputMethodHints(Qt.ImhHiddenText)
        self.lineEdit_SendAmount.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit_SendAmount.setClearButtonEnabled(True)

        self.horizontalLayout_34.addWidget(self.lineEdit_SendAmount)


        self.horizontalLayout_35.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_52)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_55 = QLabel(self.frame_50)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_33.addWidget(self.label_55)

        self.lineEdit_SendAmountUSD = QLineEdit(self.frame_50)
        self.lineEdit_SendAmountUSD.setObjectName(u"lineEdit_SendAmountUSD")
        self.lineEdit_SendAmountUSD.setEnabled(False)
        self.lineEdit_SendAmountUSD.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_33.addWidget(self.lineEdit_SendAmountUSD)

        self.frame_51 = QFrame(self.frame_50)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(100, 0))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_51)


        self.horizontalLayout_35.addWidget(self.frame_50)


        self.verticalLayout_14.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_45)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_59 = QLabel(self.frame_53)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"color: ;")

        self.horizontalLayout_36.addWidget(self.label_59)

        self.lineEdit_send_receiver = QLineEdit(self.frame_53)
        self.lineEdit_send_receiver.setObjectName(u"lineEdit_send_receiver")
        self.lineEdit_send_receiver.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_send_receiver.setClearButtonEnabled(True)

        self.horizontalLayout_36.addWidget(self.lineEdit_send_receiver)


        self.verticalLayout_14.addWidget(self.frame_53)


        self.verticalLayout_13.addWidget(self.frame_45)


        self.verticalLayout_16.addWidget(self.frame_44)


        self.verticalLayout_12.addWidget(self.frame_19)

        self.frame_106 = QFrame(self.page_sending)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMaximumSize(QSize(16777215, 50))
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_106)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.frame_114 = QFrame(self.frame_106)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMinimumSize(QSize(100, 0))
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_67.addWidget(self.frame_114)

        self.lineEdit_Send_InfoField = QLineEdit(self.frame_106)
        self.lineEdit_Send_InfoField.setObjectName(u"lineEdit_Send_InfoField")
        self.lineEdit_Send_InfoField.setMinimumSize(QSize(0, 40))
        self.lineEdit_Send_InfoField.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_Send_InfoField.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 8, 0);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_Send_InfoField.setAlignment(Qt.AlignCenter)
        self.lineEdit_Send_InfoField.setDragEnabled(True)
        self.lineEdit_Send_InfoField.setReadOnly(True)

        self.horizontalLayout_67.addWidget(self.lineEdit_Send_InfoField)

        self.frame_115 = QFrame(self.frame_106)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMinimumSize(QSize(100, 0))
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_67.addWidget(self.frame_115)


        self.verticalLayout_12.addWidget(self.frame_106)

        self.frame_104 = QFrame(self.page_sending)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMaximumSize(QSize(16777215, 100))
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.frame_105 = QFrame(self.frame_104)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setStyleSheet(u"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_63 = QLabel(self.frame_105)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(0, 0))
        self.label_63.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_63.addWidget(self.label_63)

        self.slider_gasSend = QSlider(self.frame_105)
        self.slider_gasSend.setObjectName(u"slider_gasSend")
        self.slider_gasSend.setMaximumSize(QSize(275, 16777215))
        self.slider_gasSend.setStyleSheet(u"color:rgb(220, 161, 1);")
        self.slider_gasSend.setMinimum(5)
        self.slider_gasSend.setMaximum(50)
        self.slider_gasSend.setSliderPosition(6)
        self.slider_gasSend.setOrientation(Qt.Horizontal)

        self.horizontalLayout_63.addWidget(self.slider_gasSend)

        self.lineEdit_gasSendGwei = QLineEdit(self.frame_105)
        self.lineEdit_gasSendGwei.setObjectName(u"lineEdit_gasSendGwei")
        self.lineEdit_gasSendGwei.setMinimumSize(QSize(111, 0))
        self.lineEdit_gasSendGwei.setMaximumSize(QSize(111, 16777215))
        self.lineEdit_gasSendGwei.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_63.addWidget(self.lineEdit_gasSendGwei)

        self.btn_Send_BNBTOKEN = QPushButton(self.frame_105)
        self.btn_Send_BNBTOKEN.setObjectName(u"btn_Send_BNBTOKEN")
        self.btn_Send_BNBTOKEN.setMinimumSize(QSize(60, 60))
        self.btn_Send_BNBTOKEN.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_63.addWidget(self.btn_Send_BNBTOKEN)


        self.horizontalLayout_64.addWidget(self.frame_105)


        self.verticalLayout_12.addWidget(self.frame_104)

        self.stackedWidget.addWidget(self.page_sending)
        self.page_confirm = QWidget()
        self.page_confirm.setObjectName(u"page_confirm")
        self.verticalLayout_18 = QVBoxLayout(self.page_confirm)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_54 = QFrame(self.page_confirm)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 120))
        self.frame_54.setMaximumSize(QSize(16777215, 130))
        self.frame_54.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.frame_55 = QFrame(self.frame_54)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"border:0;")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.label_61 = QLabel(self.frame_55)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(230, 60, 191, 25))
        self.label_62 = QLabel(self.frame_55)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(0, 0, 391, 61))
        self.label_62.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")

        self.horizontalLayout_37.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.frame_54)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"border:0;")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")

        self.horizontalLayout_37.addWidget(self.frame_56)


        self.verticalLayout_18.addWidget(self.frame_54)

        self.frame_20 = QFrame(self.page_confirm)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border-radius: 60px;\n"
"}	")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.frame_58 = QFrame(self.frame_20)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"\n"
"	background-color:rgba(255, 0, 0, 0);")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_44.addWidget(self.frame_58)

        self.frame_64 = QFrame(self.frame_20)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_64)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_60 = QFrame(self.frame_64)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_33 = QLabel(self.frame_60)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_43.addWidget(self.label_33)

        self.label_send_TokenName = QLabel(self.frame_60)
        self.label_send_TokenName.setObjectName(u"label_send_TokenName")
        self.label_send_TokenName.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_43.addWidget(self.label_send_TokenName)

        self.frame_66 = QFrame(self.frame_60)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_43.addWidget(self.frame_66)

        self.frame_65 = QFrame(self.frame_60)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_43.addWidget(self.frame_65)


        self.verticalLayout_17.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_64)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_64 = QLabel(self.frame_61)
        self.label_64.setObjectName(u"label_64")

        self.horizontalLayout_42.addWidget(self.label_64)

        self.frame_76 = QFrame(self.frame_61)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(100, 0))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_42.addWidget(self.frame_76)

        self.output_send_TokenAmount = QLineEdit(self.frame_61)
        self.output_send_TokenAmount.setObjectName(u"output_send_TokenAmount")
        self.output_send_TokenAmount.setEnabled(True)
        self.output_send_TokenAmount.setMinimumSize(QSize(0, 30))
        self.output_send_TokenAmount.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_send_TokenAmount.setReadOnly(True)
        self.output_send_TokenAmount.setClearButtonEnabled(False)

        self.horizontalLayout_42.addWidget(self.output_send_TokenAmount)

        self.frame_75 = QFrame(self.frame_61)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(200, 0))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_81 = QLabel(self.frame_75)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(0, 0))
        self.label_81.setMaximumSize(QSize(35, 16777215))
        self.label_81.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_61.addWidget(self.label_81)

        self.output_send_TokenUSD_2 = QLineEdit(self.frame_75)
        self.output_send_TokenUSD_2.setObjectName(u"output_send_TokenUSD_2")
        self.output_send_TokenUSD_2.setEnabled(True)
        self.output_send_TokenUSD_2.setMinimumSize(QSize(0, 30))
        self.output_send_TokenUSD_2.setMaximumSize(QSize(100, 16777215))
        self.output_send_TokenUSD_2.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_send_TokenUSD_2.setReadOnly(True)
        self.output_send_TokenUSD_2.setClearButtonEnabled(False)

        self.horizontalLayout_61.addWidget(self.output_send_TokenUSD_2)


        self.horizontalLayout_42.addWidget(self.frame_75)

        self.label_TokenAmountInUsdt = QLabel(self.frame_61)
        self.label_TokenAmountInUsdt.setObjectName(u"label_TokenAmountInUsdt")

        self.horizontalLayout_42.addWidget(self.label_TokenAmountInUsdt)


        self.verticalLayout_17.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_64)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_65 = QLabel(self.frame_62)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_41.addWidget(self.label_65)

        self.frame_79 = QFrame(self.frame_62)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(160, 0))
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_41.addWidget(self.frame_79)

        self.output_send_rece = QLineEdit(self.frame_62)
        self.output_send_rece.setObjectName(u"output_send_rece")
        self.output_send_rece.setEnabled(True)
        self.output_send_rece.setMinimumSize(QSize(420, 30))
        self.output_send_rece.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_send_rece.setReadOnly(True)
        self.output_send_rece.setClearButtonEnabled(False)

        self.horizontalLayout_41.addWidget(self.output_send_rece)

        self.frame_80 = QFrame(self.frame_62)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(0, 0))
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_41.addWidget(self.frame_80)

        self.label_send_Receiver = QLabel(self.frame_62)
        self.label_send_Receiver.setObjectName(u"label_send_Receiver")
        self.label_send_Receiver.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_41.addWidget(self.label_send_Receiver)


        self.verticalLayout_17.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_64)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_66 = QLabel(self.frame_63)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_40.addWidget(self.label_66)

        self.output_send_TokenGasBNB = QLineEdit(self.frame_63)
        self.output_send_TokenGasBNB.setObjectName(u"output_send_TokenGasBNB")
        self.output_send_TokenGasBNB.setEnabled(True)
        self.output_send_TokenGasBNB.setMinimumSize(QSize(250, 30))
        self.output_send_TokenGasBNB.setMaximumSize(QSize(100, 16777215))
        self.output_send_TokenGasBNB.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_send_TokenGasBNB.setReadOnly(True)
        self.output_send_TokenGasBNB.setClearButtonEnabled(False)

        self.horizontalLayout_40.addWidget(self.output_send_TokenGasBNB)

        self.label_send_TokenName_2 = QLabel(self.frame_63)
        self.label_send_TokenName_2.setObjectName(u"label_send_TokenName_2")
        self.label_send_TokenName_2.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_40.addWidget(self.label_send_TokenName_2)

        self.label_82 = QLabel(self.frame_63)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMinimumSize(QSize(0, 0))
        self.label_82.setMaximumSize(QSize(35, 16777215))
        self.label_82.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_40.addWidget(self.label_82)

        self.label_send_Gas_2 = QLabel(self.frame_63)
        self.label_send_Gas_2.setObjectName(u"label_send_Gas_2")
        self.label_send_Gas_2.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_40.addWidget(self.label_send_Gas_2)

        self.output_send_FeeUSD = QLineEdit(self.frame_63)
        self.output_send_FeeUSD.setObjectName(u"output_send_FeeUSD")
        self.output_send_FeeUSD.setEnabled(True)
        self.output_send_FeeUSD.setMinimumSize(QSize(0, 30))
        self.output_send_FeeUSD.setMaximumSize(QSize(100, 16777215))
        self.output_send_FeeUSD.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_send_FeeUSD.setReadOnly(True)
        self.output_send_FeeUSD.setClearButtonEnabled(False)

        self.horizontalLayout_40.addWidget(self.output_send_FeeUSD)

        self.label_send_Gas = QLabel(self.frame_63)
        self.label_send_Gas.setObjectName(u"label_send_Gas")
        self.label_send_Gas.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_40.addWidget(self.label_send_Gas)


        self.verticalLayout_17.addWidget(self.frame_63)

        self.frame_57 = QFrame(self.frame_64)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.pushButton_TXCancel = QPushButton(self.frame_57)
        self.pushButton_TXCancel.setObjectName(u"pushButton_TXCancel")
        self.pushButton_TXCancel.setMinimumSize(QSize(0, 60))
        self.pushButton_TXCancel.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	color:rgb(170, 0, 0);\n"
"	font-size:15px;\n"
"	border-radius: 25px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_39.addWidget(self.pushButton_TXCancel)

        self.pushButton_SendConfirm = QPushButton(self.frame_57)
        self.pushButton_SendConfirm.setObjectName(u"pushButton_SendConfirm")
        self.pushButton_SendConfirm.setMinimumSize(QSize(0, 60))
        self.pushButton_SendConfirm.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size:15px;\n"
"	color: rgb(85, 170, 0);\n"
"	border-radius: 25px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_39.addWidget(self.pushButton_SendConfirm)


        self.verticalLayout_17.addWidget(self.frame_57)


        self.horizontalLayout_44.addWidget(self.frame_64)

        self.frame_59 = QFrame(self.frame_20)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setStyleSheet(u"\n"
"	background-color:rgba(255, 0, 0, 0);")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_44.addWidget(self.frame_59)


        self.verticalLayout_18.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.page_confirm)
        self.page_WaitingForConfirm = QWidget()
        self.page_WaitingForConfirm.setObjectName(u"page_WaitingForConfirm")
        self.verticalLayout_25 = QVBoxLayout(self.page_WaitingForConfirm)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_107 = QFrame(self.page_WaitingForConfirm)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMinimumSize(QSize(0, 120))
        self.frame_107.setMaximumSize(QSize(16777215, 130))
        self.frame_107.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:none;\n"
"}\n"
"")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_107)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_108 = QFrame(self.frame_107)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setStyleSheet(u"border: none;")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_108)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_84 = QLabel(self.frame_108)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")

        self.verticalLayout_38.addWidget(self.label_84)

        self.label_83 = QLabel(self.frame_108)
        self.label_83.setObjectName(u"label_83")

        self.verticalLayout_38.addWidget(self.label_83)


        self.verticalLayout_37.addWidget(self.frame_108)


        self.verticalLayout_25.addWidget(self.frame_107)

        self.frame_110 = QFrame(self.page_WaitingForConfirm)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMinimumSize(QSize(1000, 390))
        self.frame_110.setMaximumSize(QSize(1000, 16777215))
        self.frame_110.setStyleSheet(u"")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_110)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.frame_127 = QFrame(self.frame_110)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setMinimumSize(QSize(200, 0))
        self.frame_127.setMaximumSize(QSize(980, 16777215))
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_127)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.frame_100 = QFrame(self.frame_127)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(200, 0))
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_66.addWidget(self.frame_100)

        self.label_Waiting_Confirm = QLabel(self.frame_127)
        self.label_Waiting_Confirm.setObjectName(u"label_Waiting_Confirm")
        self.label_Waiting_Confirm.setMinimumSize(QSize(500, 380))
        self.label_Waiting_Confirm.setMaximumSize(QSize(650, 16777215))
        self.label_Waiting_Confirm.setLayoutDirection(Qt.LeftToRight)
        self.label_Waiting_Confirm.setAutoFillBackground(False)
        self.label_Waiting_Confirm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.label_Waiting_Confirm)

        self.frame_102 = QFrame(self.frame_127)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setMinimumSize(QSize(200, 0))
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_66.addWidget(self.frame_102)


        self.horizontalLayout_26.addWidget(self.frame_127)


        self.verticalLayout_25.addWidget(self.frame_110)

        self.frame_103 = QFrame(self.page_WaitingForConfirm)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(0, 80))
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.pushButton_TxBscView = QPushButton(self.frame_103)
        self.pushButton_TxBscView.setObjectName(u"pushButton_TxBscView")
        self.pushButton_TxBscView.setMinimumSize(QSize(150, 15))
        self.pushButton_TxBscView.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_TxBscView.setBaseSize(QSize(60, 0))
        self.pushButton_TxBscView.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_55.addWidget(self.pushButton_TxBscView)

        self.lineEdit_Info_Confirmation = QLineEdit(self.frame_103)
        self.lineEdit_Info_Confirmation.setObjectName(u"lineEdit_Info_Confirmation")
        self.lineEdit_Info_Confirmation.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_Info_Confirmation.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_Info_Confirmation.setAlignment(Qt.AlignCenter)
        self.lineEdit_Info_Confirmation.setReadOnly(True)

        self.horizontalLayout_55.addWidget(self.lineEdit_Info_Confirmation)

        self.pushButton_back_To_Main = QPushButton(self.frame_103)
        self.pushButton_back_To_Main.setObjectName(u"pushButton_back_To_Main")
        self.pushButton_back_To_Main.setMinimumSize(QSize(100, 60))
        self.pushButton_back_To_Main.setMaximumSize(QSize(100, 16777215))
        self.pushButton_back_To_Main.setBaseSize(QSize(60, 0))
        self.pushButton_back_To_Main.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_55.addWidget(self.pushButton_back_To_Main)


        self.verticalLayout_25.addWidget(self.frame_103)

        self.stackedWidget.addWidget(self.page_WaitingForConfirm)
        self.page_addToken = QWidget()
        self.page_addToken.setObjectName(u"page_addToken")
        self.verticalLayout_8 = QVBoxLayout(self.page_addToken)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_30 = QFrame(self.page_addToken)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 120))
        self.frame_30.setMaximumSize(QSize(16777215, 130))
        self.frame_30.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border:0;\n"
"}\n"
"")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_34 = QFrame(self.frame_30)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"border:0;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.label_49 = QLabel(self.frame_34)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(290, 60, 141, 25))
        self.label_50 = QLabel(self.frame_34)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(0, 0, 391, 61))
        self.label_50.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")

        self.horizontalLayout_23.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_30)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"border:0;")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")

        self.horizontalLayout_23.addWidget(self.frame_35)


        self.verticalLayout_8.addWidget(self.frame_30)

        self.frame_12 = QFrame(self.page_addToken)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 35px;\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.frame_38 = QFrame(self.frame_12)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(150, 0))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.pushButton_back_Alltokens = QPushButton(self.frame_39)
        self.pushButton_back_Alltokens.setObjectName(u"pushButton_back_Alltokens")
        self.pushButton_back_Alltokens.setGeometry(QRect(50, 440, 101, 70))
        self.pushButton_back_Alltokens.setMinimumSize(QSize(60, 70))
        self.pushButton_back_Alltokens.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_68.addWidget(self.frame_39)

        self.frame_120 = QFrame(self.frame_38)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setMinimumSize(QSize(500, 500))
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_120)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_14 = QFrame(self.frame_120)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(50, 500))
        self.frame_14.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border: 6px solid rgb(33, 37, 43);\n"
"background-position: center;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_14)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_122 = QFrame(self.frame_14)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setMinimumSize(QSize(0, 70))
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.input_add_TokenAddresse = QLineEdit(self.frame_122)
        self.input_add_TokenAddresse.setObjectName(u"input_add_TokenAddresse")
        self.input_add_TokenAddresse.setGeometry(QRect(0, 30, 451, 41))
        self.input_add_TokenAddresse.setMinimumSize(QSize(0, 30))
        self.input_add_TokenAddresse.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color:rgb(220, 161, 1);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_add_TokenAddresse.setClearButtonEnabled(True)
        self.label_76 = QLabel(self.frame_122)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(0, -10, 261, 41))

        self.verticalLayout_31.addWidget(self.frame_122)

        self.frame_123 = QFrame(self.frame_14)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setMinimumSize(QSize(0, 70))
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.input_add_TokenName = QLineEdit(self.frame_123)
        self.input_add_TokenName.setObjectName(u"input_add_TokenName")
        self.input_add_TokenName.setGeometry(QRect(0, 30, 441, 41))
        self.input_add_TokenName.setMinimumSize(QSize(0, 30))
        self.input_add_TokenName.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color:rgb(220, 161, 1);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_add_TokenName.setClearButtonEnabled(True)
        self.label_77 = QLabel(self.frame_123)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(0, -10, 261, 41))

        self.verticalLayout_31.addWidget(self.frame_123)

        self.frame_124 = QFrame(self.frame_14)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setMinimumSize(QSize(0, 70))
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.input_add_TokenSymbol = QLineEdit(self.frame_124)
        self.input_add_TokenSymbol.setObjectName(u"input_add_TokenSymbol")
        self.input_add_TokenSymbol.setGeometry(QRect(0, 30, 441, 41))
        self.input_add_TokenSymbol.setMinimumSize(QSize(0, 30))
        self.input_add_TokenSymbol.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	color:rgb(220, 161, 1);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_add_TokenSymbol.setClearButtonEnabled(True)
        self.label_78 = QLabel(self.frame_124)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(0, -10, 261, 41))

        self.verticalLayout_31.addWidget(self.frame_124)

        self.frame_125 = QFrame(self.frame_14)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setMinimumSize(QSize(0, 70))
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.input_add_TokenDecimals = QLineEdit(self.frame_125)
        self.input_add_TokenDecimals.setObjectName(u"input_add_TokenDecimals")
        self.input_add_TokenDecimals.setGeometry(QRect(0, 30, 441, 41))
        self.input_add_TokenDecimals.setMinimumSize(QSize(0, 30))
        self.input_add_TokenDecimals.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	color:rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_add_TokenDecimals.setClearButtonEnabled(True)
        self.label_79 = QLabel(self.frame_125)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(0, -10, 261, 41))

        self.verticalLayout_31.addWidget(self.frame_125)

        self.frame_126 = QFrame(self.frame_14)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setMinimumSize(QSize(0, 70))
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.input_add_Token_IMGURL = QLineEdit(self.frame_126)
        self.input_add_Token_IMGURL.setObjectName(u"input_add_Token_IMGURL")
        self.input_add_Token_IMGURL.setGeometry(QRect(0, 30, 441, 41))
        self.input_add_Token_IMGURL.setMinimumSize(QSize(0, 30))
        self.input_add_Token_IMGURL.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	color:rgb(220, 161, 1);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_add_Token_IMGURL.setClearButtonEnabled(True)
        self.label_80 = QLabel(self.frame_126)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(0, -10, 341, 41))

        self.verticalLayout_31.addWidget(self.frame_126)


        self.verticalLayout_30.addWidget(self.frame_14)


        self.horizontalLayout_68.addWidget(self.frame_120)

        self.frame_119 = QFrame(self.frame_38)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.pushButton_save_token = QPushButton(self.frame_119)
        self.pushButton_save_token.setObjectName(u"pushButton_save_token")
        self.pushButton_save_token.setGeometry(QRect(60, 440, 116, 70))
        self.pushButton_save_token.setMinimumSize(QSize(0, 70))
        self.pushButton_save_token.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.label_add_Token_Error = QLabel(self.frame_119)
        self.label_add_Token_Error.setObjectName(u"label_add_Token_Error")
        self.label_add_Token_Error.setGeometry(QRect(30, 30, 171, 221))
        self.label_add_Token_Error.setStyleSheet(u"font: bold;\n"
"font-size: 18px;\n"
"color:rgb(170, 0, 0);\n"
"border-radius: 15px;\n"
"background-color: rgb(33, 37, 43);\n"
"qproperty-alignment: AlignCenter;")

        self.horizontalLayout_68.addWidget(self.frame_119)


        self.horizontalLayout_27.addWidget(self.frame_38)


        self.verticalLayout_8.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.page_addToken)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.gridLayout_4 = QGridLayout(self.page_home)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_40 = QFrame(self.page_home)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(16777215, 5))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_40, 2, 0, 1, 1)

        self.frame_29 = QFrame(self.page_home)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 300))
        self.frame_29.setMaximumSize(QSize(16777215, 16777215))
        self.frame_29.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius:25px;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_97 = QFrame(self.frame_29)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMinimumSize(QSize(500, 0))
        self.frame_97.setMaximumSize(QSize(500, 16777215))
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_97)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_116 = QFrame(self.frame_97)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setMaximumSize(QSize(450, 125))
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_116)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_22 = QFrame(self.frame_116)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 45))
        self.frame_22.setMaximumSize(QSize(450, 50))
        self.frame_22.setStyleSheet(u"font: bold;\n"
"font-size: 18px;\n"
"border-radius: 25px;\n"
"background-color: rgb(27, 29, 35);\n"
"background-position: center;\n"
"background-repeat: no-reperat;\n"
"\n"
"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_67 = QLabel(self.frame_22)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_16.addWidget(self.label_67)

        self.label_40 = QLabel(self.frame_22)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"background-color:rgba(255, 0, 0, 0);")

        self.horizontalLayout_16.addWidget(self.label_40)

        self.output_BNBPrice = QLineEdit(self.frame_22)
        self.output_BNBPrice.setObjectName(u"output_BNBPrice")
        self.output_BNBPrice.setEnabled(False)
        self.output_BNBPrice.setMinimumSize(QSize(0, 30))
        self.output_BNBPrice.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_BNBPrice.setReadOnly(True)
        self.output_BNBPrice.setClearButtonEnabled(False)

        self.horizontalLayout_16.addWidget(self.output_BNBPrice)


        self.verticalLayout_11.addWidget(self.frame_22)

        self.frame_21 = QFrame(self.frame_116)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 45))
        self.frame_21.setMaximumSize(QSize(450, 50))
        self.frame_21.setStyleSheet(u"font: bold;\n"
"font-size: 18px;\n"
"border-radius: 25px;\n"
"background-color: rgb(27, 29, 35);\n"
"background-position: center;\n"
"background-repeat: no-reperat;\n"
"\n"
"")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_68 = QLabel(self.frame_21)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_17.addWidget(self.label_68)

        self.label_39 = QLabel(self.frame_21)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"background-color:rgba(255, 0, 0, 0);")

        self.horizontalLayout_17.addWidget(self.label_39)

        self.output_TIGSPRICE = QLineEdit(self.frame_21)
        self.output_TIGSPRICE.setObjectName(u"output_TIGSPRICE")
        self.output_TIGSPRICE.setEnabled(False)
        self.output_TIGSPRICE.setMinimumSize(QSize(0, 30))
        self.output_TIGSPRICE.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_TIGSPRICE.setReadOnly(True)
        self.output_TIGSPRICE.setClearButtonEnabled(False)

        self.horizontalLayout_17.addWidget(self.output_TIGSPRICE)


        self.verticalLayout_11.addWidget(self.frame_21)


        self.verticalLayout_29.addWidget(self.frame_116)

        self.frame_36 = QFrame(self.frame_97)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_36)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_75 = QLabel(self.frame_37)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(250, 0))
        self.label_75.setStyleSheet(u"background-color:rgba(255, 0, 0, 0);")

        self.horizontalLayout_25.addWidget(self.label_75)

        self.pushButton_copy_self_address = QPushButton(self.frame_37)
        self.pushButton_copy_self_address.setObjectName(u"pushButton_copy_self_address")
        self.pushButton_copy_self_address.setMinimumSize(QSize(120, 50))
        self.pushButton_copy_self_address.setMaximumSize(QSize(120, 60))
        self.pushButton_copy_self_address.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 25px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_25.addWidget(self.pushButton_copy_self_address)


        self.verticalLayout_28.addWidget(self.frame_37)

        self.output_self_address = QLineEdit(self.frame_36)
        self.output_self_address.setObjectName(u"output_self_address")
        self.output_self_address.setEnabled(True)
        self.output_self_address.setMinimumSize(QSize(280, 45))
        self.output_self_address.setStyleSheet(u"QLineEdit {\n"
"	font-size: 17px;\n"
"	font: bold;\n"
"	color: rgb(220, 161, 1);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_self_address.setReadOnly(True)
        self.output_self_address.setClearButtonEnabled(False)

        self.verticalLayout_28.addWidget(self.output_self_address)


        self.verticalLayout_29.addWidget(self.frame_36)


        self.horizontalLayout_18.addWidget(self.frame_97)

        self.label_qrCode_self_address = QLabel(self.frame_29)
        self.label_qrCode_self_address.setObjectName(u"label_qrCode_self_address")
        self.label_qrCode_self_address.setStyleSheet(u"border-radius: 35px;\n"
"text-center:;")
        self.label_qrCode_self_address.setTextFormat(Qt.RichText)
        self.label_qrCode_self_address.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/angle-double-right-solid.png"))
        self.label_qrCode_self_address.setScaledContents(False)
        self.label_qrCode_self_address.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_qrCode_self_address)


        self.gridLayout_4.addWidget(self.frame_29, 3, 0, 1, 1)

        self.frame_17 = QFrame(self.page_home)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 100))
        self.frame_17.setStyleSheet(u"font: bold;\n"
"font-size: 22px;\n"
"border-radius: 40px;\n"
"background-color: rgb(39, 44, 54);\n"
"background-position: center;\n"
"background-repeat: no-reperat;\n"
"\n"
"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_32 = QLabel(self.frame_17)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(30, 0))
        self.label_32.setMaximumSize(QSize(50, 16777215))
        self.label_32.setStyleSheet(u"background-color:rgba(255, 0, 0, 0);")

        self.horizontalLayout_21.addWidget(self.label_32)

        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(64, 64))
        self.frame_18.setStyleSheet(u"background-color:rgba(255, 0, 0, 0);\n"
"background-image: url(:/Fontawsome/icons/fontawsome/bnb-logo64x64.png) ;\n"
"background-repeat: no-reperat;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_21.addWidget(self.frame_18)

        self.label_37 = QLabel(self.frame_17)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(250, 0))
        self.label_37.setStyleSheet(u"background-color:rgba(255, 0, 0, 0);")

        self.horizontalLayout_21.addWidget(self.label_37)

        self.output_BNBBalance = QLineEdit(self.frame_17)
        self.output_BNBBalance.setObjectName(u"output_BNBBalance")
        self.output_BNBBalance.setEnabled(True)
        self.output_BNBBalance.setMinimumSize(QSize(280, 30))
        self.output_BNBBalance.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_BNBBalance.setReadOnly(True)
        self.output_BNBBalance.setClearButtonEnabled(False)

        self.horizontalLayout_21.addWidget(self.output_BNBBalance)

        self.label_51 = QLabel(self.frame_17)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_21.addWidget(self.label_51)

        self.output_BNBBalance_in_usd = QLineEdit(self.frame_17)
        self.output_BNBBalance_in_usd.setObjectName(u"output_BNBBalance_in_usd")
        self.output_BNBBalance_in_usd.setEnabled(True)
        self.output_BNBBalance_in_usd.setMinimumSize(QSize(0, 30))
        self.output_BNBBalance_in_usd.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_BNBBalance_in_usd.setReadOnly(True)
        self.output_BNBBalance_in_usd.setClearButtonEnabled(False)

        self.horizontalLayout_21.addWidget(self.output_BNBBalance_in_usd)

        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(30, 0))
        self.label_13.setMaximumSize(QSize(50, 16777215))
        self.label_13.setStyleSheet(u"background-color:rgba(255, 0, 0, 0);")

        self.horizontalLayout_21.addWidget(self.label_13)


        self.gridLayout_4.addWidget(self.frame_17, 5, 0, 1, 1)

        self.frame_98 = QFrame(self.page_home)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMaximumSize(QSize(16777215, 10))
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_98, 8, 0, 1, 1)

        self.frame_31 = QFrame(self.page_home)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 120))
        self.frame_31.setMaximumSize(QSize(16777215, 130))
        self.frame_31.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border:0;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"border:0;")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.label_45 = QLabel(self.frame_32)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(140, 60, 211, 25))
        self.label_47 = QLabel(self.frame_32)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(0, 0, 391, 61))
        self.label_47.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")

        self.horizontalLayout_19.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_31)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"border:0;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_11 = QLabel(self.frame_33)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_20.addWidget(self.label_11)

        self.pushButton_TokenSite = QPushButton(self.frame_33)
        self.pushButton_TokenSite.setObjectName(u"pushButton_TokenSite")
        self.pushButton_TokenSite.setMinimumSize(QSize(180, 80))
        self.pushButton_TokenSite.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 25px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_20.addWidget(self.pushButton_TokenSite)


        self.horizontalLayout_19.addWidget(self.frame_33)


        self.gridLayout_4.addWidget(self.frame_31, 1, 0, 1, 1)

        self.frame_13 = QFrame(self.page_home)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 100))
        self.frame_13.setStyleSheet(u"font: bold;\n"
"font-size: 22px;\n"
"border-radius: 40px;\n"
"background-color: rgb(39, 44, 54);\n"
"background-position: center;\n"
"background-repeat: no-reperat;\n"
"\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_31 = QLabel(self.frame_13)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(30, 0))
        self.label_31.setMaximumSize(QSize(50, 16777215))
        self.label_31.setStyleSheet(u"background-color:rgba(255, 0, 0, 0);")

        self.horizontalLayout_22.addWidget(self.label_31)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(64, 64))
        self.frame_15.setStyleSheet(u"background-color:rgba(255, 0, 0, 0);\n"
"background-image: url(:/Fontawsome/icons/fontawsome/TIGS-64x64.png);\n"
"background-repeat: no-reperat;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22.addWidget(self.frame_15)

        self.label_28 = QLabel(self.frame_13)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(250, 0))
        self.label_28.setStyleSheet(u"background-color:rgba(255, 0, 0, 0);")

        self.horizontalLayout_22.addWidget(self.label_28)

        self.output_Tigs_balance = QLineEdit(self.frame_13)
        self.output_Tigs_balance.setObjectName(u"output_Tigs_balance")
        self.output_Tigs_balance.setEnabled(True)
        self.output_Tigs_balance.setMinimumSize(QSize(280, 30))
        self.output_Tigs_balance.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_Tigs_balance.setReadOnly(True)
        self.output_Tigs_balance.setClearButtonEnabled(False)

        self.horizontalLayout_22.addWidget(self.output_Tigs_balance)

        self.label_52 = QLabel(self.frame_13)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_22.addWidget(self.label_52)

        self.output_TigsBalance_in_usd = QLineEdit(self.frame_13)
        self.output_TigsBalance_in_usd.setObjectName(u"output_TigsBalance_in_usd")
        self.output_TigsBalance_in_usd.setEnabled(True)
        self.output_TigsBalance_in_usd.setMinimumSize(QSize(0, 30))
        self.output_TigsBalance_in_usd.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_TigsBalance_in_usd.setReadOnly(True)
        self.output_TigsBalance_in_usd.setClearButtonEnabled(False)

        self.horizontalLayout_22.addWidget(self.output_TigsBalance_in_usd)

        self.label_30 = QLabel(self.frame_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(30, 0))
        self.label_30.setMaximumSize(QSize(50, 16777215))
        self.label_30.setStyleSheet(u"background-color:rgba(255, 0, 0, 0);")

        self.horizontalLayout_22.addWidget(self.label_30)


        self.gridLayout_4.addWidget(self.frame_13, 7, 0, 1, 1)

        self.frame_101 = QFrame(self.page_home)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMaximumSize(QSize(16777215, 5))
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_101, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.page_TokenOverview = QWidget()
        self.page_TokenOverview.setObjectName(u"page_TokenOverview")
        self.verticalLayout_19 = QVBoxLayout(self.page_TokenOverview)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_109 = QFrame(self.page_TokenOverview)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMinimumSize(QSize(0, 120))
        self.frame_109.setMaximumSize(QSize(16777215, 130))
        self.frame_109.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border:0;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_109)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.frame_118 = QFrame(self.frame_109)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMinimumSize(QSize(443, 0))
        self.frame_118.setStyleSheet(u"border:0;")
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.label_74 = QLabel(self.frame_118)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(0, 0, 451, 61))
        self.label_74.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")
        self.label_69 = QLabel(self.frame_118)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(110, 60, 331, 25))

        self.horizontalLayout_56.addWidget(self.frame_118)

        self.frame_117 = QFrame(self.frame_109)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setStyleSheet(u"border:0;")
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_44 = QLabel(self.frame_117)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(150, 0))
        self.label_44.setMaximumSize(QSize(16777215, 16777215))
        self.label_44.setStyleSheet(u"background-color:rgba(255, 0, 0, 0);")

        self.horizontalLayout_57.addWidget(self.label_44)

        self.output_TotalTokenBalanceInUsd = QLineEdit(self.frame_117)
        self.output_TotalTokenBalanceInUsd.setObjectName(u"output_TotalTokenBalanceInUsd")
        self.output_TotalTokenBalanceInUsd.setEnabled(True)
        self.output_TotalTokenBalanceInUsd.setMinimumSize(QSize(0, 30))
        self.output_TotalTokenBalanceInUsd.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_TotalTokenBalanceInUsd.setReadOnly(True)
        self.output_TotalTokenBalanceInUsd.setClearButtonEnabled(False)

        self.horizontalLayout_57.addWidget(self.output_TotalTokenBalanceInUsd)

        self.pushButton_refresh_3 = QPushButton(self.frame_117)
        self.pushButton_refresh_3.setObjectName(u"pushButton_refresh_3")
        self.pushButton_refresh_3.setMinimumSize(QSize(120, 80))
        self.pushButton_refresh_3.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_57.addWidget(self.pushButton_refresh_3)


        self.horizontalLayout_56.addWidget(self.frame_117)


        self.verticalLayout_19.addWidget(self.frame_109)

        self.frame_113 = QFrame(self.page_TokenOverview)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border:0;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.tableWidget_AllActivTokens = QTableWidget(self.frame_113)
        if (self.tableWidget_AllActivTokens.columnCount() < 6):
            self.tableWidget_AllActivTokens.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget_AllActivTokens.rowCount() < 500):
            self.tableWidget_AllActivTokens.setRowCount(500)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(10, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(11, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(12, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(13, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(14, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setVerticalHeaderItem(15, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllActivTokens.setItem(0, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllActivTokens.setItem(0, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setItem(0, 2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_AllActivTokens.setItem(0, 3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllActivTokens.setItem(0, 4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllActivTokens.setItem(0, 5, __qtablewidgetitem27)
        self.tableWidget_AllActivTokens.setObjectName(u"tableWidget_AllActivTokens")
        sizePolicy.setHeightForWidth(self.tableWidget_AllActivTokens.sizePolicy().hasHeightForWidth())
        self.tableWidget_AllActivTokens.setSizePolicy(sizePolicy)
        self.tableWidget_AllActivTokens.setMinimumSize(QSize(0, 64))
        self.tableWidget_AllActivTokens.setBaseSize(QSize(0, 64))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.tableWidget_AllActivTokens.setPalette(palette1)
        self.tableWidget_AllActivTokens.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget_AllActivTokens.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_AllActivTokens.setFrameShape(QFrame.NoFrame)
        self.tableWidget_AllActivTokens.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_AllActivTokens.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_AllActivTokens.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_AllActivTokens.setAlternatingRowColors(False)
        self.tableWidget_AllActivTokens.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_AllActivTokens.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_AllActivTokens.setShowGrid(True)
        self.tableWidget_AllActivTokens.setGridStyle(Qt.SolidLine)
        self.tableWidget_AllActivTokens.setSortingEnabled(False)
        self.tableWidget_AllActivTokens.setRowCount(500)
        self.tableWidget_AllActivTokens.horizontalHeader().setVisible(False)
        self.tableWidget_AllActivTokens.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_AllActivTokens.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_AllActivTokens.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_AllActivTokens.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_AllActivTokens.verticalHeader().setVisible(False)
        self.tableWidget_AllActivTokens.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_AllActivTokens.verticalHeader().setMinimumSectionSize(40)
        self.tableWidget_AllActivTokens.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_AllActivTokens.verticalHeader().setHighlightSections(False)
        self.tableWidget_AllActivTokens.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_60.addWidget(self.tableWidget_AllActivTokens)


        self.verticalLayout_19.addWidget(self.frame_113)

        self.stackedWidget.addWidget(self.page_TokenOverview)
        self.page_Create_Account = QWidget()
        self.page_Create_Account.setObjectName(u"page_Create_Account")
        self.label_5 = QLabel(self.page_Create_Account)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 60, 481, 161))
        self.input_create_walletpw = QLineEdit(self.page_Create_Account)
        self.input_create_walletpw.setObjectName(u"input_create_walletpw")
        self.input_create_walletpw.setGeometry(QRect(320, 280, 461, 41))
        self.input_create_walletpw.setMinimumSize(QSize(0, 30))
        self.input_create_walletpw.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_create_walletpw.setEchoMode(QLineEdit.Password)
        self.input_create_walletpw.setClearButtonEnabled(True)
        self.input_create_walletname = QLineEdit(self.page_Create_Account)
        self.input_create_walletname.setObjectName(u"input_create_walletname")
        self.input_create_walletname.setGeometry(QRect(320, 200, 461, 41))
        self.input_create_walletname.setMinimumSize(QSize(0, 30))
        self.input_create_walletname.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_create_walletname.setClearButtonEnabled(True)
        self.label_6 = QLabel(self.page_Create_Account)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 200, 191, 41))
        self.label_7 = QLabel(self.page_Create_Account)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 280, 311, 41))
        self.pushButton_create_wallet = QPushButton(self.page_Create_Account)
        self.pushButton_create_wallet.setObjectName(u"pushButton_create_wallet")
        self.pushButton_create_wallet.setEnabled(True)
        self.pushButton_create_wallet.setGeometry(QRect(200, 500, 641, 91))
        self.pushButton_create_wallet.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 35px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_back_Login = QPushButton(self.page_Create_Account)
        self.pushButton_back_Login.setObjectName(u"pushButton_back_Login")
        self.pushButton_back_Login.setGeometry(QRect(10, 500, 141, 91))
        self.pushButton_back_Login.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	background-image: url(:/Fontawsome/icons/fontawsome/Back.png) ;\n"
"	border-radius: 35px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.label_21 = QLabel(self.page_Create_Account)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 20, 391, 61))
        self.label_21.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	image-norepeat;\n"
"}")
        self.widget_Save_your_Key = QWidget(self.page_Create_Account)
        self.widget_Save_your_Key.setObjectName(u"widget_Save_your_Key")
        self.widget_Save_your_Key.setEnabled(True)
        self.widget_Save_your_Key.setGeometry(QRect(30, 360, 801, 101))
        self.widget_Save_your_Key.setStyleSheet(u"QWidget {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 35px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"    }")
        self.label_Save_Your_Secret_Key = QLabel(self.widget_Save_your_Key)
        self.label_Save_Your_Secret_Key.setObjectName(u"label_Save_Your_Secret_Key")
        self.label_Save_Your_Secret_Key.setEnabled(True)
        self.label_Save_Your_Secret_Key.setGeometry(QRect(70, 0, 661, 41))
        self.textBrowser_skey = QTextBrowser(self.widget_Save_your_Key)
        self.textBrowser_skey.setObjectName(u"textBrowser_skey")
        self.textBrowser_skey.setEnabled(True)
        self.textBrowser_skey.setGeometry(QRect(25, 40, 671, 51))
        self.textBrowser_skey.setStyleSheet(u"color: rgb(0, 255, 0) ;")
        self.textBrowser_skey.setAutoFormatting(QTextEdit.AutoBulletList)
        self.textBrowser_skey.setUndoRedoEnabled(True)
        self.textBrowser_skey.setReadOnly(True)
        self.textBrowser_skey.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.textBrowser_skey.setOpenLinks(False)
        self.pushButton_Copy_SKEY = QPushButton(self.widget_Save_your_Key)
        self.pushButton_Copy_SKEY.setObjectName(u"pushButton_Copy_SKEY")
        self.pushButton_Copy_SKEY.setEnabled(True)
        self.pushButton_Copy_SKEY.setGeometry(QRect(710, 42, 71, 51))
        self.pushButton_Copy_SKEY.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 25px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.frame_111 = QFrame(self.page_Create_Account)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setGeometry(QRect(720, 0, 351, 381))
        self.frame_111.setStyleSheet(u"background-image: url(:/Fontawsome/icons/fontawsome/Trading_Tigers_Logo.png);\n"
"background-repeat: no-reperat;")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.stackedWidget.addWidget(self.page_Create_Account)
        self.page_EnableDisableTokens = QWidget()
        self.page_EnableDisableTokens.setObjectName(u"page_EnableDisableTokens")
        self.verticalLayout_26 = QVBoxLayout(self.page_EnableDisableTokens)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_68 = QFrame(self.page_EnableDisableTokens)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(0, 120))
        self.frame_68.setMaximumSize(QSize(16777215, 120))
        self.frame_68.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.frame_90 = QFrame(self.frame_68)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setStyleSheet(u"border:0;")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.label_72 = QLabel(self.frame_90)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(-10, -10, 401, 61))
        self.label_72.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")
        self.label_70 = QLabel(self.frame_90)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(280, 40, 261, 71))
        self.label_70.raise_()
        self.label_72.raise_()

        self.horizontalLayout_48.addWidget(self.frame_90)


        self.verticalLayout_26.addWidget(self.frame_68)

        self.frame_10 = QFrame(self.page_EnableDisableTokens)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"\n"
"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.tableWidget_AllTokensinDB = QTableWidget(self.frame_10)
        if (self.tableWidget_AllTokensinDB.columnCount() < 5):
            self.tableWidget_AllTokensinDB.setColumnCount(5)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        if (self.tableWidget_AllTokensinDB.rowCount() < 486):
            self.tableWidget_AllTokensinDB.setRowCount(486)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font3);
        self.tableWidget_AllTokensinDB.setVerticalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_AllTokensinDB.setVerticalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(0, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(0, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(0, 2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(0, 3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(0, 4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(1, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(1, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(1, 2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(1, 3, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(1, 4, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(2, 4, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(3, 4, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(4, 4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(5, 4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(6, 4, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(7, 4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(8, 4, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(9, 4, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(10, 4, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(11, 4, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(12, 4, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(13, 4, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(14, 4, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(15, 4, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(16, 4, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(17, 4, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(18, 4, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(19, 4, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(20, 4, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(21, 4, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(22, 4, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(23, 4, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(24, 4, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(25, 4, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(26, 4, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(27, 4, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(28, 4, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(29, 4, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(30, 4, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(31, 4, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(32, 4, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(33, 4, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(34, 4, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(35, 4, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(36, 4, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(37, 4, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(38, 4, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(39, 4, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(40, 4, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(41, 4, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(42, 4, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(43, 4, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(44, 4, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(45, 4, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(46, 4, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(47, 4, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(48, 4, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(50, 4, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_AllTokensinDB.setItem(51, 4, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_AllTokensinDB.setItem(485, 4, __qtablewidgetitem94)
        self.tableWidget_AllTokensinDB.setObjectName(u"tableWidget_AllTokensinDB")
        sizePolicy.setHeightForWidth(self.tableWidget_AllTokensinDB.sizePolicy().hasHeightForWidth())
        self.tableWidget_AllTokensinDB.setSizePolicy(sizePolicy)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush19 = QBrush(QColor(210, 210, 210, 128))
        brush19.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush19)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush20 = QBrush(QColor(210, 210, 210, 128))
        brush20.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush20)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush21 = QBrush(QColor(210, 210, 210, 128))
        brush21.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush21)
#endif
        self.tableWidget_AllTokensinDB.setPalette(palette2)
        self.tableWidget_AllTokensinDB.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid"
                        " rgb(44, 49, 60);\n"
"}\n"
"\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"\n"
"QHeaderView::section:horizontal{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_AllTokensinDB.setFrameShape(QFrame.NoFrame)
        self.tableWidget_AllTokensinDB.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_AllTokensinDB.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_AllTokensinDB.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_AllTokensinDB.setDragDropOverwriteMode(False)
        self.tableWidget_AllTokensinDB.setAlternatingRowColors(False)
        self.tableWidget_AllTokensinDB.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_AllTokensinDB.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_AllTokensinDB.setShowGrid(True)
        self.tableWidget_AllTokensinDB.setGridStyle(Qt.SolidLine)
        self.tableWidget_AllTokensinDB.setSortingEnabled(False)
        self.tableWidget_AllTokensinDB.setWordWrap(False)
        self.tableWidget_AllTokensinDB.setRowCount(486)
        self.tableWidget_AllTokensinDB.horizontalHeader().setVisible(False)
        self.tableWidget_AllTokensinDB.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_AllTokensinDB.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_AllTokensinDB.horizontalHeader().setHighlightSections(False)
        self.tableWidget_AllTokensinDB.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_AllTokensinDB.verticalHeader().setVisible(False)
        self.tableWidget_AllTokensinDB.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_AllTokensinDB.verticalHeader().setHighlightSections(False)
        self.tableWidget_AllTokensinDB.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_52.addWidget(self.tableWidget_AllTokensinDB, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_26.addWidget(self.frame_10)

        self.frame_73 = QFrame(self.page_EnableDisableTokens)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(0, 120))
        self.frame_73.setMaximumSize(QSize(16777215, 120))
        self.frame_73.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.frame_91 = QFrame(self.frame_73)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setStyleSheet(u"border:0;")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.pushButton_back_wallet = QPushButton(self.frame_91)
        self.pushButton_back_wallet.setObjectName(u"pushButton_back_wallet")
        self.pushButton_back_wallet.setMinimumSize(QSize(0, 80))
        self.pushButton_back_wallet.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/Fontawsome/icons/fontawsome/Back.png) ;\n"
"	font: bold;\n"
"	border-radius: 35px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_53.addWidget(self.pushButton_back_wallet)

        self.frame_96 = QFrame(self.frame_91)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setStyleSheet(u"border:0;")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_53.addWidget(self.frame_96)

        self.pushButton_toAddTokenOverview = QPushButton(self.frame_91)
        self.pushButton_toAddTokenOverview.setObjectName(u"pushButton_toAddTokenOverview")
        self.pushButton_toAddTokenOverview.setMinimumSize(QSize(0, 80))
        self.pushButton_toAddTokenOverview.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_53.addWidget(self.pushButton_toAddTokenOverview)


        self.horizontalLayout_49.addWidget(self.frame_91)


        self.verticalLayout_26.addWidget(self.frame_73)

        self.stackedWidget.addWidget(self.page_EnableDisableTokens)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_27 = QVBoxLayout(self.page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_92 = QFrame(self.page)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(0, 120))
        self.frame_92.setMaximumSize(QSize(16777215, 120))
        self.frame_92.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.frame_93 = QFrame(self.frame_92)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setStyleSheet(u"border:0;")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.label_73 = QLabel(self.frame_93)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(-10, -10, 401, 61))
        self.label_73.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")
        self.label_71 = QLabel(self.frame_93)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(290, 40, 171, 71))
        self.label_71.raise_()
        self.label_73.raise_()

        self.horizontalLayout_50.addWidget(self.frame_93)


        self.verticalLayout_27.addWidget(self.frame_92)

        self.frame_99 = QFrame(self.page)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)

        self.verticalLayout_27.addWidget(self.frame_99)

        self.frame_94 = QFrame(self.page)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(0, 120))
        self.frame_94.setMaximumSize(QSize(16777215, 120))
        self.frame_94.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_94)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.frame_95 = QFrame(self.frame_94)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setStyleSheet(u"border:0;")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.pushButton_back_To = QPushButton(self.frame_95)
        self.pushButton_back_To.setObjectName(u"pushButton_back_To")
        self.pushButton_back_To.setGeometry(QRect(730, 10, 132, 80))
        self.pushButton_back_To.setMinimumSize(QSize(0, 80))
        self.pushButton_back_To.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_back_Login_3 = QPushButton(self.frame_95)
        self.pushButton_back_Login_3.setObjectName(u"pushButton_back_Login_3")
        self.pushButton_back_Login_3.setGeometry(QRect(10, 10, 132, 80))
        self.pushButton_back_Login_3.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/Fontawsome/icons/fontawsome/Back.png) ;\n"
"	font: bold;\n"
"	border-radius: 35px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_51.addWidget(self.frame_95)


        self.verticalLayout_27.addWidget(self.frame_94)

        self.stackedWidget.addWidget(self.page)
        self.page_limitOrders = QWidget()
        self.page_limitOrders.setObjectName(u"page_limitOrders")
        self.frame_159 = QFrame(self.page_limitOrders)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setGeometry(QRect(0, 0, 991, 100))
        self.frame_159.setMinimumSize(QSize(0, 100))
        self.frame_159.setMaximumSize(QSize(16777215, 100))
        self.frame_159.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_159.setFrameShape(QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_159)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.frame_160 = QFrame(self.frame_159)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.label_115 = QLabel(self.frame_160)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setGeometry(QRect(300, 50, 161, 25))
        self.label_116 = QLabel(self.frame_160)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(0, 0, 391, 61))
        self.label_116.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")
        self.label_116.raise_()
        self.label_115.raise_()

        self.horizontalLayout_87.addWidget(self.frame_160)

        self.frame_167 = QFrame(self.frame_159)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setFrameShape(QFrame.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_167)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.label_117 = QLabel(self.frame_167)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_88.addWidget(self.label_117)

        self.comboBox_select_swap_LimitOrders = QComboBox(self.frame_167)
        self.comboBox_select_swap_LimitOrders.setObjectName(u"comboBox_select_swap_LimitOrders")
        self.comboBox_select_swap_LimitOrders.setMinimumSize(QSize(247, 0))
        self.comboBox_select_swap_LimitOrders.setStyleSheet(u"QComboBox {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 25px;\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	color: rgb(219, 160, 6);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")

        self.horizontalLayout_88.addWidget(self.comboBox_select_swap_LimitOrders)


        self.horizontalLayout_87.addWidget(self.frame_167)

        self.frame_170 = QFrame(self.page_limitOrders)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setGeometry(QRect(0, 569, 991, 121))
        self.frame_170.setMinimumSize(QSize(700, 120))
        self.frame_170.setMaximumSize(QSize(16777215, 140))
        self.frame_170.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_170.setFrameShape(QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_170)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.frame_171 = QFrame(self.frame_170)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setFrameShape(QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.frame_172 = QFrame(self.frame_171)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setGeometry(QRect(0, 50, 471, 61))
        self.frame_172.setFrameShape(QFrame.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Raised)
        self.label_128 = QLabel(self.frame_172)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setGeometry(QRect(10, 10, 120, 50))
        self.label_128.setMinimumSize(QSize(120, 50))
        self.frame_173 = QFrame(self.frame_172)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setGeometry(QRect(125, 10, 351, 51))
        self.frame_173.setMinimumSize(QSize(0, 45))
        self.frame_173.setFrameShape(QFrame.StyledPanel)
        self.frame_173.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_173)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.slider_GasGwei_limit = QSlider(self.frame_173)
        self.slider_GasGwei_limit.setObjectName(u"slider_GasGwei_limit")
        self.slider_GasGwei_limit.setMaximumSize(QSize(275, 16777215))
        self.slider_GasGwei_limit.setStyleSheet(u"color:rgb(220, 161, 1);")
        self.slider_GasGwei_limit.setMinimum(5)
        self.slider_GasGwei_limit.setMaximum(50)
        self.slider_GasGwei_limit.setValue(6)
        self.slider_GasGwei_limit.setOrientation(Qt.Horizontal)

        self.horizontalLayout_90.addWidget(self.slider_GasGwei_limit)

        self.output_GasGwei_limit = QLineEdit(self.frame_173)
        self.output_GasGwei_limit.setObjectName(u"output_GasGwei_limit")
        self.output_GasGwei_limit.setMaximumSize(QSize(100, 16777215))
        self.output_GasGwei_limit.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	border-radius: 14px;\n"
"	border: 5px solid rgb(33, 37, 43);\n"
"	color: rgb(220, 161, 1);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.output_GasGwei_limit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_90.addWidget(self.output_GasGwei_limit)

        self.frame_174 = QFrame(self.frame_171)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setGeometry(QRect(10, -10, 471, 61))
        self.frame_174.setFrameShape(QFrame.StyledPanel)
        self.frame_174.setFrameShadow(QFrame.Raised)
        self.label_129 = QLabel(self.frame_174)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setGeometry(QRect(10, 10, 150, 50))
        self.label_129.setMinimumSize(QSize(150, 50))
        self.frame_175 = QFrame(self.frame_174)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setGeometry(QRect(110, 10, 351, 51))
        self.frame_175.setMinimumSize(QSize(0, 45))
        self.frame_175.setFrameShape(QFrame.StyledPanel)
        self.frame_175.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_175)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.slider_Slippage_limit = QSlider(self.frame_175)
        self.slider_Slippage_limit.setObjectName(u"slider_Slippage_limit")
        self.slider_Slippage_limit.setMaximumSize(QSize(275, 16777215))
        self.slider_Slippage_limit.setStyleSheet(u"color:rgb(220, 161, 1);")
        self.slider_Slippage_limit.setMinimum(1)
        self.slider_Slippage_limit.setMaximum(50)
        self.slider_Slippage_limit.setValue(3)
        self.slider_Slippage_limit.setOrientation(Qt.Horizontal)

        self.horizontalLayout_91.addWidget(self.slider_Slippage_limit)

        self.output_Slippage_limit = QLineEdit(self.frame_175)
        self.output_Slippage_limit.setObjectName(u"output_Slippage_limit")
        self.output_Slippage_limit.setMaximumSize(QSize(100, 16777215))
        self.output_Slippage_limit.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	border-radius: 14px;\n"
"	border: 5px solid rgb(33, 37, 43);\n"
"	color: rgb(220, 161, 1);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.output_Slippage_limit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_91.addWidget(self.output_Slippage_limit)


        self.horizontalLayout_89.addWidget(self.frame_171)

        self.frame_176 = QFrame(self.frame_170)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setMinimumSize(QSize(350, 0))
        self.frame_176.setMaximumSize(QSize(16777215, 150))
        self.frame_176.setFrameShape(QFrame.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_176)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.pushButton__limit_approve_token = QPushButton(self.frame_176)
        self.pushButton__limit_approve_token.setObjectName(u"pushButton__limit_approve_token")
        self.pushButton__limit_approve_token.setEnabled(True)
        self.pushButton__limit_approve_token.setMinimumSize(QSize(100, 80))
        self.pushButton__limit_approve_token.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton__limit_approve_token.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 35px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_92.addWidget(self.pushButton__limit_approve_token)

        self.pushButton__limit_approve_tigs_toRouter = QPushButton(self.frame_176)
        self.pushButton__limit_approve_tigs_toRouter.setObjectName(u"pushButton__limit_approve_tigs_toRouter")
        self.pushButton__limit_approve_tigs_toRouter.setEnabled(True)
        self.pushButton__limit_approve_tigs_toRouter.setMinimumSize(QSize(100, 80))
        self.pushButton__limit_approve_tigs_toRouter.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton__limit_approve_tigs_toRouter.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 35px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_92.addWidget(self.pushButton__limit_approve_tigs_toRouter)

        self.pushButton_Confirm_LimitOrder = QPushButton(self.frame_176)
        self.pushButton_Confirm_LimitOrder.setObjectName(u"pushButton_Confirm_LimitOrder")
        self.pushButton_Confirm_LimitOrder.setEnabled(True)
        self.pushButton_Confirm_LimitOrder.setMinimumSize(QSize(100, 80))
        self.pushButton_Confirm_LimitOrder.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Confirm_LimitOrder.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 35px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_92.addWidget(self.pushButton_Confirm_LimitOrder)


        self.horizontalLayout_89.addWidget(self.frame_176)

        self.frame_168 = QFrame(self.page_limitOrders)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setGeometry(QRect(0, 110, 992, 450))
        self.frame_168.setMinimumSize(QSize(992, 450))
        self.frame_168.setMaximumSize(QSize(992, 500))
        self.frame_168.setFrameShape(QFrame.StyledPanel)
        self.frame_168.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_168)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.frame_169 = QFrame(self.frame_168)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setMaximumSize(QSize(500, 500))
        self.frame_169.setStyleSheet(u"QFrame{\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_169.setFrameShape(QFrame.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_169)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_178 = QFrame(self.frame_169)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setMinimumSize(QSize(0, 50))
        self.frame_178.setMaximumSize(QSize(16777215, 50))
        self.frame_178.setStyleSheet(u"border-radius: 0px;\n"
"border: 0px solid;")
        self.frame_178.setFrameShape(QFrame.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Raised)
        self.pushButton_limit_BuyOrder = QPushButton(self.frame_178)
        self.pushButton_limit_BuyOrder.setObjectName(u"pushButton_limit_BuyOrder")
        self.pushButton_limit_BuyOrder.setEnabled(True)
        self.pushButton_limit_BuyOrder.setGeometry(QRect(50, 0, 181, 50))
        self.pushButton_limit_BuyOrder.setMinimumSize(QSize(100, 50))
        self.pushButton_limit_BuyOrder.setMaximumSize(QSize(16777215, 50))
        self.pushButton_limit_BuyOrder.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(0, 170, 0);\n"
"	border-top-left-radius: 25px;\n"
"	border-bottom-left-radius	:25px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_limit_SellOrder = QPushButton(self.frame_178)
        self.pushButton_limit_SellOrder.setObjectName(u"pushButton_limit_SellOrder")
        self.pushButton_limit_SellOrder.setEnabled(True)
        self.pushButton_limit_SellOrder.setGeometry(QRect(220, 0, 181, 50))
        self.pushButton_limit_SellOrder.setMinimumSize(QSize(100, 50))
        self.pushButton_limit_SellOrder.setMaximumSize(QSize(16777215, 50))
        self.pushButton_limit_SellOrder.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(170, 0, 0);\n"
"	border-top-right-radius: 25px;\n"
"	border-bottom-right-radius	:25px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_36.addWidget(self.frame_178)

        self.stackedWidget_limitOrders = QStackedWidget(self.frame_169)
        self.stackedWidget_limitOrders.setObjectName(u"stackedWidget_limitOrders")
        self.stackedWidget_limitOrders.setMaximumSize(QSize(500, 16777215))
        self.stackedWidget_limitOrders.setStyleSheet(u"")
        self.stackedWidget_limitOrders.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget_limitOrders.setFrameShadow(QFrame.Raised)
        self.stackedWidget_Page_LimitBuy = QWidget()
        self.stackedWidget_Page_LimitBuy.setObjectName(u"stackedWidget_Page_LimitBuy")
        self.frame_180 = QFrame(self.stackedWidget_Page_LimitBuy)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setGeometry(QRect(10, 10, 421, 81))
        self.frame_180.setStyleSheet(u"border:0;")
        self.frame_180.setFrameShape(QFrame.StyledPanel)
        self.frame_180.setFrameShadow(QFrame.Raised)
        self.pushButton__limitBuy_UseBUSD = QPushButton(self.frame_180)
        self.pushButton__limitBuy_UseBUSD.setObjectName(u"pushButton__limitBuy_UseBUSD")
        self.pushButton__limitBuy_UseBUSD.setEnabled(True)
        self.pushButton__limitBuy_UseBUSD.setGeometry(QRect(270, 0, 101, 30))
        self.pushButton__limitBuy_UseBUSD.setMinimumSize(QSize(75, 30))
        self.pushButton__limitBuy_UseBUSD.setMaximumSize(QSize(16777215, 40))
        self.pushButton__limitBuy_UseBUSD.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius	:15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton__limitBuy_UseBNB = QPushButton(self.frame_180)
        self.pushButton__limitBuy_UseBNB.setObjectName(u"pushButton__limitBuy_UseBNB")
        self.pushButton__limitBuy_UseBNB.setEnabled(True)
        self.pushButton__limitBuy_UseBNB.setGeometry(QRect(180, 0, 91, 30))
        self.pushButton__limitBuy_UseBNB.setMinimumSize(QSize(75, 30))
        self.pushButton__limitBuy_UseBNB.setMaximumSize(QSize(16777215, 40))
        self.pushButton__limitBuy_UseBNB.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius	:15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.label_118 = QLabel(self.frame_180)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(60, 0, 141, 31))
        self.label_118.setStyleSheet(u"background-color:0;")
        self.frame_181 = QFrame(self.frame_180)
        self.frame_181.setObjectName(u"frame_181")
        self.frame_181.setGeometry(QRect(60, 0, 311, 80))
        self.frame_181.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_181.setFrameShape(QFrame.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Raised)
        self.lineEdit_limit_BuyFrom_Amount = QLineEdit(self.frame_181)
        self.lineEdit_limit_BuyFrom_Amount.setObjectName(u"lineEdit_limit_BuyFrom_Amount")
        self.lineEdit_limit_BuyFrom_Amount.setGeometry(QRect(0, 30, 311, 41))
        self.lineEdit_limit_BuyFrom_Amount.setMinimumSize(QSize(100, 0))
        self.lineEdit_limit_BuyFrom_Amount.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_limit_BuyFrom_Amount.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	color: rgb(219, 160, 6);\n"
"}")
        self.lineEdit_limit_BuyFrom_Amount.setAlignment(Qt.AlignCenter)
        self.lineEdit_limit_BuyFrom_Amount.setClearButtonEnabled(True)
        self.frame_181.raise_()
        self.pushButton__limitBuy_UseBUSD.raise_()
        self.pushButton__limitBuy_UseBNB.raise_()
        self.label_118.raise_()
        self.comboBox_LimitOrder_to_Asset = QComboBox(self.stackedWidget_Page_LimitBuy)
        self.comboBox_LimitOrder_to_Asset.setObjectName(u"comboBox_LimitOrder_to_Asset")
        self.comboBox_LimitOrder_to_Asset.setGeometry(QRect(80, 120, 301, 51))
        self.comboBox_LimitOrder_to_Asset.setMinimumSize(QSize(247, 0))
        self.comboBox_LimitOrder_to_Asset.setStyleSheet(u"QComboBox {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 25px;\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	color: rgb(219, 160, 6);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.label_121 = QLabel(self.stackedWidget_Page_LimitBuy)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(150, 90, 161, 25))
        self.label_121.setStyleSheet(u"font: bold;\n"
"font-size: 22px;\n"
"border-radius: 0px;\n"
"border: 0px solid rgb(33, 37, 43);\n"
"color: rgb(219, 160, 6);")
        self.label_122 = QLabel(self.stackedWidget_Page_LimitBuy)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setGeometry(QRect(150, 180, 161, 25))
        self.label_122.setStyleSheet(u"font: bold;\n"
"font-size: 22px;\n"
"border-radius: 0px;\n"
"border: 0px solid rgb(33, 37, 43);\n"
"color: rgb(219, 160, 6);")
        self.frame_186 = QFrame(self.stackedWidget_Page_LimitBuy)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setGeometry(QRect(10, 220, 421, 81))
        self.frame_186.setStyleSheet(u"border:0;")
        self.frame_186.setFrameShape(QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Raised)
        self.label_123 = QLabel(self.frame_186)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setGeometry(QRect(50, 0, 181, 31))
        self.label_123.setStyleSheet(u"background-color:0;")
        self.frame_187 = QFrame(self.frame_186)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setGeometry(QRect(60, 0, 311, 80))
        self.frame_187.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)
        self.lineEdit_limit_BuyTo_Amount = QLineEdit(self.frame_187)
        self.lineEdit_limit_BuyTo_Amount.setObjectName(u"lineEdit_limit_BuyTo_Amount")
        self.lineEdit_limit_BuyTo_Amount.setGeometry(QRect(10, 30, 291, 41))
        self.lineEdit_limit_BuyTo_Amount.setMinimumSize(QSize(100, 0))
        self.lineEdit_limit_BuyTo_Amount.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_limit_BuyTo_Amount.setStyleSheet(u"\n"
"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	color: rgb(219, 160, 6);\n"
"}")
        self.lineEdit_limit_BuyTo_Amount.setAlignment(Qt.AlignCenter)
        self.lineEdit_limit_BuyTo_Amount.setClearButtonEnabled(True)
        self.frame_187.raise_()
        self.label_123.raise_()
        self.stackedWidget_limitOrders.addWidget(self.stackedWidget_Page_LimitBuy)
        self.stackedWidget_Page_LimitSell = QWidget()
        self.stackedWidget_Page_LimitSell.setObjectName(u"stackedWidget_Page_LimitSell")
        self.frame_184 = QFrame(self.stackedWidget_Page_LimitSell)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setGeometry(QRect(10, 210, 431, 81))
        self.frame_184.setStyleSheet(u"border:0;")
        self.frame_184.setFrameShape(QFrame.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Raised)
        self.pushButton__limitBuy_UseBUSD_3 = QPushButton(self.frame_184)
        self.pushButton__limitBuy_UseBUSD_3.setObjectName(u"pushButton__limitBuy_UseBUSD_3")
        self.pushButton__limitBuy_UseBUSD_3.setEnabled(True)
        self.pushButton__limitBuy_UseBUSD_3.setGeometry(QRect(300, 0, 101, 30))
        self.pushButton__limitBuy_UseBUSD_3.setMinimumSize(QSize(75, 30))
        self.pushButton__limitBuy_UseBUSD_3.setMaximumSize(QSize(16777215, 40))
        self.pushButton__limitBuy_UseBUSD_3.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-top-right-radius: 15px;\n"
"	border-bottom-right-radius	:15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton__limitBuy_UseBNB_4 = QPushButton(self.frame_184)
        self.pushButton__limitBuy_UseBNB_4.setObjectName(u"pushButton__limitBuy_UseBNB_4")
        self.pushButton__limitBuy_UseBNB_4.setEnabled(True)
        self.pushButton__limitBuy_UseBNB_4.setGeometry(QRect(210, 0, 91, 30))
        self.pushButton__limitBuy_UseBNB_4.setMinimumSize(QSize(75, 30))
        self.pushButton__limitBuy_UseBNB_4.setMaximumSize(QSize(16777215, 40))
        self.pushButton__limitBuy_UseBNB_4.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-top-left-radius: 15px;\n"
"	border-bottom-left-radius	:15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.label_120 = QLabel(self.frame_184)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setGeometry(QRect(30, 0, 181, 31))
        self.label_120.setStyleSheet(u"background-color:0;")
        self.frame_185 = QFrame(self.frame_184)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setGeometry(QRect(30, 0, 371, 80))
        self.frame_185.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_185.setFrameShape(QFrame.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Raised)
        self.lineEdit_limit_to_Amount = QLineEdit(self.frame_185)
        self.lineEdit_limit_to_Amount.setObjectName(u"lineEdit_limit_to_Amount")
        self.lineEdit_limit_to_Amount.setGeometry(QRect(20, 30, 320, 41))
        self.lineEdit_limit_to_Amount.setMinimumSize(QSize(100, 0))
        self.lineEdit_limit_to_Amount.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_limit_to_Amount.setStyleSheet(u"\n"
"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	color: rgb(219, 160, 6);\n"
"}")
        self.lineEdit_limit_to_Amount.setAlignment(Qt.AlignCenter)
        self.lineEdit_limit_to_Amount.setClearButtonEnabled(True)
        self.frame_185.raise_()
        self.label_120.raise_()
        self.pushButton__limitBuy_UseBNB_4.raise_()
        self.pushButton__limitBuy_UseBUSD_3.raise_()
        self.frame_188 = QFrame(self.stackedWidget_Page_LimitSell)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setGeometry(QRect(20, 100, 421, 81))
        self.frame_188.setStyleSheet(u"border:0;")
        self.frame_188.setFrameShape(QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Raised)
        self.label_124 = QLabel(self.frame_188)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setGeometry(QRect(60, 0, 181, 31))
        self.label_124.setStyleSheet(u"background-color:0;")
        self.frame_190 = QFrame(self.frame_188)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setGeometry(QRect(60, 0, 311, 80))
        self.frame_190.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)
        self.lineEdit_limit_BuyTo_Amount_3 = QLineEdit(self.frame_190)
        self.lineEdit_limit_BuyTo_Amount_3.setObjectName(u"lineEdit_limit_BuyTo_Amount_3")
        self.lineEdit_limit_BuyTo_Amount_3.setGeometry(QRect(10, 30, 291, 41))
        self.lineEdit_limit_BuyTo_Amount_3.setMinimumSize(QSize(100, 0))
        self.lineEdit_limit_BuyTo_Amount_3.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_limit_BuyTo_Amount_3.setStyleSheet(u"\n"
"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	color: rgb(219, 160, 6);\n"
"}")
        self.lineEdit_limit_BuyTo_Amount_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_limit_BuyTo_Amount_3.setClearButtonEnabled(True)
        self.frame_190.raise_()
        self.label_124.raise_()
        self.comboBox_LimitOrder_to_Asset_2 = QComboBox(self.stackedWidget_Page_LimitSell)
        self.comboBox_LimitOrder_to_Asset_2.setObjectName(u"comboBox_LimitOrder_to_Asset_2")
        self.comboBox_LimitOrder_to_Asset_2.setGeometry(QRect(10, 30, 247, 51))
        self.comboBox_LimitOrder_to_Asset_2.setMinimumSize(QSize(247, 0))
        self.comboBox_LimitOrder_to_Asset_2.setStyleSheet(u"QComboBox {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 25px;\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	color: rgb(219, 160, 6);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.lineEdit_limit_BuyTo_Amount_4 = QLineEdit(self.stackedWidget_Page_LimitSell)
        self.lineEdit_limit_BuyTo_Amount_4.setObjectName(u"lineEdit_limit_BuyTo_Amount_4")
        self.lineEdit_limit_BuyTo_Amount_4.setGeometry(QRect(270, 30, 171, 51))
        self.lineEdit_limit_BuyTo_Amount_4.setMinimumSize(QSize(100, 0))
        self.lineEdit_limit_BuyTo_Amount_4.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_limit_BuyTo_Amount_4.setStyleSheet(u"\n"
"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 14px;\n"
"	color: rgb(219, 160, 6);\n"
"	border-radius: 20px;\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"}\n"
"")
        self.lineEdit_limit_BuyTo_Amount_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_limit_BuyTo_Amount_4.setClearButtonEnabled(True)
        self.stackedWidget_limitOrders.addWidget(self.stackedWidget_Page_LimitSell)

        self.verticalLayout_36.addWidget(self.stackedWidget_limitOrders)


        self.horizontalLayout_93.addWidget(self.frame_169)

        self.frame_177 = QFrame(self.frame_168)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setStyleSheet(u"QFrame{\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_177.setFrameShape(QFrame.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Raised)
        self.pushButton__limitBuy_UseBNB_2 = QPushButton(self.frame_177)
        self.pushButton__limitBuy_UseBNB_2.setObjectName(u"pushButton__limitBuy_UseBNB_2")
        self.pushButton__limitBuy_UseBNB_2.setEnabled(True)
        self.pushButton__limitBuy_UseBNB_2.setGeometry(QRect(0, 0, 461, 34))
        self.pushButton__limitBuy_UseBNB_2.setMinimumSize(QSize(75, 30))
        self.pushButton__limitBuy_UseBNB_2.setMaximumSize(QSize(16777215, 40))
        self.pushButton__limitBuy_UseBNB_2.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-top-right-radius: 15px;\n"
"	border-top-left-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.tableWidget_OpenLimitOrders = QTableWidget(self.frame_177)
        if (self.tableWidget_OpenLimitOrders.columnCount() < 4):
            self.tableWidget_OpenLimitOrders.setColumnCount(4)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setHorizontalHeaderItem(0, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setHorizontalHeaderItem(1, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setHorizontalHeaderItem(2, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setHorizontalHeaderItem(3, __qtablewidgetitem98)
        if (self.tableWidget_OpenLimitOrders.rowCount() < 16):
            self.tableWidget_OpenLimitOrders.setRowCount(16)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setFont(font3);
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(0, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(1, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(2, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(3, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(4, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(5, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(6, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(7, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(8, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(9, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(10, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(11, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(12, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(13, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(14, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setVerticalHeaderItem(15, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setItem(0, 0, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setItem(0, 1, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setItem(0, 2, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_OpenLimitOrders.setItem(0, 3, __qtablewidgetitem118)
        self.tableWidget_OpenLimitOrders.setObjectName(u"tableWidget_OpenLimitOrders")
        self.tableWidget_OpenLimitOrders.setGeometry(QRect(10, 40, 441, 381))
        sizePolicy.setHeightForWidth(self.tableWidget_OpenLimitOrders.sizePolicy().hasHeightForWidth())
        self.tableWidget_OpenLimitOrders.setSizePolicy(sizePolicy)
        palette3 = QPalette()
        brush22 = QBrush(QColor(220, 161, 1, 255))
        brush22.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush22)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush22)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush22)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush23 = QBrush(QColor(220, 161, 1, 128))
        brush23.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush23)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush22)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush22)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush22)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush24 = QBrush(QColor(220, 161, 1, 128))
        brush24.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush24)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush22)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush22)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush22)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush25 = QBrush(QColor(220, 161, 1, 128))
        brush25.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush25)
#endif
        self.tableWidget_OpenLimitOrders.setPalette(palette3)
        self.tableWidget_OpenLimitOrders.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"	font-size: 14px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 0px solid rgb(33, 37, 43);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border"
                        "-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_OpenLimitOrders.setFrameShape(QFrame.NoFrame)
        self.tableWidget_OpenLimitOrders.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_OpenLimitOrders.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_OpenLimitOrders.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_OpenLimitOrders.setAlternatingRowColors(False)
        self.tableWidget_OpenLimitOrders.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_OpenLimitOrders.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_OpenLimitOrders.setShowGrid(True)
        self.tableWidget_OpenLimitOrders.setGridStyle(Qt.SolidLine)
        self.tableWidget_OpenLimitOrders.setSortingEnabled(False)
        self.tableWidget_OpenLimitOrders.horizontalHeader().setVisible(False)
        self.tableWidget_OpenLimitOrders.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_OpenLimitOrders.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_OpenLimitOrders.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_OpenLimitOrders.verticalHeader().setVisible(False)
        self.tableWidget_OpenLimitOrders.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_OpenLimitOrders.verticalHeader().setHighlightSections(False)
        self.tableWidget_OpenLimitOrders.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_93.addWidget(self.frame_177)

        self.stackedWidget.addWidget(self.page_limitOrders)
        self.page_swapping = QWidget()
        self.page_swapping.setObjectName(u"page_swapping")
        self.frame_7 = QFrame(self.page_swapping)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(9, 0, 981, 100))
        self.frame_7.setMinimumSize(QSize(0, 100))
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_28 = QFrame(self.frame_7)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"border:0;")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.label_35 = QLabel(self.frame_28)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(310, 50, 161, 25))
        self.label_34 = QLabel(self.frame_28)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(0, 0, 391, 61))
        self.label_34.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")
        self.label_34.raise_()
        self.label_35.raise_()

        self.horizontalLayout_9.addWidget(self.frame_28)

        self.frame_24 = QFrame(self.frame_7)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"border:0;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_26 = QLabel(self.frame_24)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"color: rgb(219, 160, 6);\n"
"border:0;")

        self.horizontalLayout_11.addWidget(self.label_26)

        self.comboBox_select_swap = QComboBox(self.frame_24)
        self.comboBox_select_swap.setObjectName(u"comboBox_select_swap")
        self.comboBox_select_swap.setMinimumSize(QSize(247, 0))
        self.comboBox_select_swap.setStyleSheet(u"QComboBox {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 25px;\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	color: rgb(219, 160, 6);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.comboBox_select_swap)


        self.horizontalLayout_9.addWidget(self.frame_24)

        self.frame_6 = QFrame(self.page_swapping)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(9, 110, 982, 150))
        self.frame_6.setMinimumSize(QSize(0, 150))
        self.frame_6.setMaximumSize(QSize(16777215, 160))
        self.frame_6.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_Swap_from_BalanceInUSD = QLineEdit(self.frame_6)
        self.lineEdit_Swap_from_BalanceInUSD.setObjectName(u"lineEdit_Swap_from_BalanceInUSD")
        self.lineEdit_Swap_from_BalanceInUSD.setMinimumSize(QSize(150, 0))
        self.lineEdit_Swap_from_BalanceInUSD.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_Swap_from_BalanceInUSD.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_Swap_from_BalanceInUSD.setAlignment(Qt.AlignCenter)
        self.lineEdit_Swap_from_BalanceInUSD.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_Swap_from_BalanceInUSD, 0, 8, 1, 1)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.lineEdit_Swap_from_AssetBalance = QLineEdit(self.frame_6)
        self.lineEdit_Swap_from_AssetBalance.setObjectName(u"lineEdit_Swap_from_AssetBalance")
        self.lineEdit_Swap_from_AssetBalance.setMinimumSize(QSize(250, 0))
        self.lineEdit_Swap_from_AssetBalance.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_Swap_from_AssetBalance.setAlignment(Qt.AlignCenter)
        self.lineEdit_Swap_from_AssetBalance.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_Swap_from_AssetBalance, 0, 5, 1, 2)

        self.label_38 = QLabel(self.frame_6)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"color: ;")

        self.gridLayout_2.addWidget(self.label_38, 1, 0, 1, 1)

        self.lineEdit_Swap_from_Amount = QLineEdit(self.frame_6)
        self.lineEdit_Swap_from_Amount.setObjectName(u"lineEdit_Swap_from_Amount")
        self.lineEdit_Swap_from_Amount.setMinimumSize(QSize(300, 0))
        self.lineEdit_Swap_from_Amount.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_Swap_from_Amount.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_Swap_from_Amount.setAlignment(Qt.AlignCenter)
        self.lineEdit_Swap_from_Amount.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.lineEdit_Swap_from_Amount, 1, 1, 1, 1)

        self.label_46 = QLabel(self.frame_6)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(50, 16777215))
        self.label_46.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.gridLayout_2.addWidget(self.label_46, 1, 5, 1, 1)

        self.comboBox_swap_from_ASSET = QComboBox(self.frame_6)
        self.comboBox_swap_from_ASSET.setObjectName(u"comboBox_swap_from_ASSET")
        self.comboBox_swap_from_ASSET.setMinimumSize(QSize(250, 0))
        self.comboBox_swap_from_ASSET.setMaximumSize(QSize(250, 16777215))
        self.comboBox_swap_from_ASSET.setAutoFillBackground(False)
        self.comboBox_swap_from_ASSET.setStyleSheet(u"QComboBox {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(219, 160, 6) ;\n"
"	border-radius: 25px;\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.comboBox_swap_from_ASSET, 0, 1, 1, 1)

        self.lineEdit_Swap_from_AmountInUSD = QLineEdit(self.frame_6)
        self.lineEdit_Swap_from_AmountInUSD.setObjectName(u"lineEdit_Swap_from_AmountInUSD")
        self.lineEdit_Swap_from_AmountInUSD.setMinimumSize(QSize(180, 0))
        self.lineEdit_Swap_from_AmountInUSD.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_Swap_from_AmountInUSD.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_Swap_from_AmountInUSD.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_Swap_from_AmountInUSD, 1, 6, 1, 1)

        self.label_87 = QLabel(self.frame_6)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.gridLayout_2.addWidget(self.label_87, 0, 7, 1, 1)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.label_2, 0, 3, 1, 1)

        self.lineEdit_Swap_from_Amount.raise_()
        self.label_9.raise_()
        self.lineEdit_Swap_from_BalanceInUSD.raise_()
        self.label_38.raise_()
        self.label_87.raise_()
        self.lineEdit_Swap_from_AssetBalance.raise_()
        self.label_2.raise_()
        self.comboBox_swap_from_ASSET.raise_()
        self.lineEdit_Swap_from_AmountInUSD.raise_()
        self.label_46.raise_()
        self.frame_2 = QFrame(self.page_swapping)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(9, 270, 982, 160))
        self.frame_2.setMinimumSize(QSize(0, 160))
        self.frame_2.setMaximumSize(QSize(16777215, 160))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_swap_to_ASSET = QComboBox(self.frame_2)
        self.comboBox_swap_to_ASSET.setObjectName(u"comboBox_swap_to_ASSET")
        self.comboBox_swap_to_ASSET.setMinimumSize(QSize(250, 0))
        self.comboBox_swap_to_ASSET.setMaximumSize(QSize(250, 16777215))
        self.comboBox_swap_to_ASSET.setStyleSheet(u"QComboBox {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(219, 160, 6) ;\n"
"	border-radius: 25px;\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QComboBox:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.comboBox_swap_to_ASSET, 1, 1, 1, 1)

        self.lineEdit_Swap_to_BalanceInUSD = QLineEdit(self.frame_2)
        self.lineEdit_Swap_to_BalanceInUSD.setObjectName(u"lineEdit_Swap_to_BalanceInUSD")
        self.lineEdit_Swap_to_BalanceInUSD.setMinimumSize(QSize(150, 0))
        self.lineEdit_Swap_to_BalanceInUSD.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_Swap_to_BalanceInUSD.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_Swap_to_BalanceInUSD.setAlignment(Qt.AlignCenter)
        self.lineEdit_Swap_to_BalanceInUSD.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_Swap_to_BalanceInUSD, 1, 7, 1, 1)

        self.lineEdit_Swap_to_Amount = QLineEdit(self.frame_2)
        self.lineEdit_Swap_to_Amount.setObjectName(u"lineEdit_Swap_to_Amount")
        self.lineEdit_Swap_to_Amount.setMinimumSize(QSize(300, 0))
        self.lineEdit_Swap_to_Amount.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_Swap_to_Amount.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_Swap_to_Amount.setAlignment(Qt.AlignCenter)
        self.lineEdit_Swap_to_Amount.setReadOnly(False)
        self.lineEdit_Swap_to_Amount.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_Swap_to_Amount, 3, 1, 1, 1)

        self.label_86 = QLabel(self.frame_2)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.gridLayout.addWidget(self.label_86, 1, 6, 1, 1)

        self.label_41 = QLabel(self.frame_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_41, 3, 0, 1, 1)

        self.label_48 = QLabel(self.frame_2)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.gridLayout.addWidget(self.label_48, 3, 4, 1, 1)

        self.label_27 = QLabel(self.frame_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_27, 1, 3, 1, 1)

        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_23, 1, 0, 1, 1)

        self.lineEdit_Swap_to_AssetBalance = QLineEdit(self.frame_2)
        self.lineEdit_Swap_to_AssetBalance.setObjectName(u"lineEdit_Swap_to_AssetBalance")
        self.lineEdit_Swap_to_AssetBalance.setMinimumSize(QSize(250, 0))
        self.lineEdit_Swap_to_AssetBalance.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_Swap_to_AssetBalance.setAlignment(Qt.AlignCenter)
        self.lineEdit_Swap_to_AssetBalance.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_Swap_to_AssetBalance, 1, 4, 1, 2)

        self.lineEdit_Swap_to_AmountInUSD = QLineEdit(self.frame_2)
        self.lineEdit_Swap_to_AmountInUSD.setObjectName(u"lineEdit_Swap_to_AmountInUSD")
        self.lineEdit_Swap_to_AmountInUSD.setMinimumSize(QSize(180, 0))
        self.lineEdit_Swap_to_AmountInUSD.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_Swap_to_AmountInUSD.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_Swap_to_AmountInUSD.setAlignment(Qt.AlignCenter)
        self.lineEdit_Swap_to_AmountInUSD.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_Swap_to_AmountInUSD, 3, 5, 1, 1)

        self.label_23.raise_()
        self.lineEdit_Swap_to_AssetBalance.raise_()
        self.label_86.raise_()
        self.label_27.raise_()
        self.lineEdit_Swap_to_Amount.raise_()
        self.lineEdit_Swap_to_BalanceInUSD.raise_()
        self.label_41.raise_()
        self.comboBox_swap_to_ASSET.raise_()
        self.lineEdit_Swap_to_AmountInUSD.raise_()
        self.label_48.raise_()
        self.frame_128 = QFrame(self.page_swapping)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setGeometry(QRect(9, 440, 982, 112))
        self.frame_128.setMinimumSize(QSize(0, 112))
        self.frame_128.setMaximumSize(QSize(982, 950))
        self.frame_128.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_128)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalSpacer = QSpacerItem(33, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer)

        self.frame_SwapWay = QFrame(self.frame_128)
        self.frame_SwapWay.setObjectName(u"frame_SwapWay")
        self.frame_SwapWay.setMinimumSize(QSize(350, 100))
        self.frame_SwapWay.setStyleSheet(u"border:0;")
        self.frame_SwapWay.setFrameShape(QFrame.StyledPanel)
        self.frame_SwapWay.setFrameShadow(QFrame.Raised)
        self.label_96 = QLabel(self.frame_SwapWay)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(-10, 0, 241, 23))
        self.label_96.setMinimumSize(QSize(40, 20))
        self.label_96.setMaximumSize(QSize(16777215, 23))
        self.label_96.setStyleSheet(u"color: rgb(220, 161, 1);\n"
"")
        self.label_SwapWayA = QLabel(self.frame_SwapWay)
        self.label_SwapWayA.setObjectName(u"label_SwapWayA")
        self.label_SwapWayA.setGeometry(QRect(10, 30, 64, 64))
        self.label_SwapWayA.setMinimumSize(QSize(64, 64))
        self.label_SwapWayA.setMaximumSize(QSize(64, 64))
        self.label_SwapWayA.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))
        self.label_SwapWayB = QLabel(self.frame_SwapWay)
        self.label_SwapWayB.setObjectName(u"label_SwapWayB")
        self.label_SwapWayB.setGeometry(QRect(140, 30, 64, 64))
        self.label_SwapWayB.setMinimumSize(QSize(64, 64))
        self.label_SwapWayB.setMaximumSize(QSize(64, 64))
        self.label_SwapWayB.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))
        self.label_SwapWayC = QLabel(self.frame_SwapWay)
        self.label_SwapWayC.setObjectName(u"label_SwapWayC")
        self.label_SwapWayC.setGeometry(QRect(270, 30, 64, 64))
        self.label_SwapWayC.setMinimumSize(QSize(64, 64))
        self.label_SwapWayC.setMaximumSize(QSize(64, 64))
        self.label_SwapWayC.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))
        self.frame_130 = QFrame(self.frame_SwapWay)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setGeometry(QRect(90, 50, 30, 30))
        self.frame_130.setMaximumSize(QSize(30, 30))
        self.frame_130.setStyleSheet(u"background-image: url(:/Fontawsome/icons/fontawsome/angel-double25x25.png);")
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.frame_SwapWayC = QFrame(self.frame_SwapWay)
        self.frame_SwapWayC.setObjectName(u"frame_SwapWayC")
        self.frame_SwapWayC.setGeometry(QRect(220, 50, 30, 30))
        self.frame_SwapWayC.setMaximumSize(QSize(30, 30))
        self.frame_SwapWayC.setStyleSheet(u"background-image: url(:/Fontawsome/icons/fontawsome/angel-double25x25.png);")
        self.frame_SwapWayC.setFrameShape(QFrame.StyledPanel)
        self.frame_SwapWayC.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_69.addWidget(self.frame_SwapWay)

        self.horizontalSpacer_2 = QSpacerItem(43, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer_2)

        self.frame_InputTokenInfos = QFrame(self.frame_128)
        self.frame_InputTokenInfos.setObjectName(u"frame_InputTokenInfos")
        self.frame_InputTokenInfos.setMinimumSize(QSize(230, 90))
        self.frame_InputTokenInfos.setMaximumSize(QSize(16777215, 231))
        self.frame_InputTokenInfos.setStyleSheet(u"border:0;")
        self.frame_InputTokenInfos.setFrameShape(QFrame.StyledPanel)
        self.frame_InputTokenInfos.setFrameShadow(QFrame.Raised)
        self.label_93 = QLabel(self.frame_InputTokenInfos)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(-10, -10, 241, 40))
        self.label_93.setMinimumSize(QSize(40, 40))
        self.label_93.setStyleSheet(u"color: rgb(220, 161, 1);\n"
"text-decoration: underline;")
        self.label_94 = QLabel(self.frame_InputTokenInfos)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(10, 30, 101, 28))
        self.label_94.setMinimumSize(QSize(40, 27))
        self.label_94.setStyleSheet(u"")
        self.label_95 = QLabel(self.frame_InputTokenInfos)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(0, 60, 121, 28))
        self.label_95.setMinimumSize(QSize(50, 27))
        self.label_95.setStyleSheet(u"")
        self.lineEdit_InputToken_BuyTax = QLineEdit(self.frame_InputTokenInfos)
        self.lineEdit_InputToken_BuyTax.setObjectName(u"lineEdit_InputToken_BuyTax")
        self.lineEdit_InputToken_BuyTax.setGeometry(QRect(110, 30, 91, 28))
        self.lineEdit_InputToken_BuyTax.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	border-radius: 14px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_InputToken_BuyTax.setAlignment(Qt.AlignCenter)
        self.lineEdit_InputToken_SellTax = QLineEdit(self.frame_InputTokenInfos)
        self.lineEdit_InputToken_SellTax.setObjectName(u"lineEdit_InputToken_SellTax")
        self.lineEdit_InputToken_SellTax.setGeometry(QRect(110, 60, 91, 28))
        self.lineEdit_InputToken_SellTax.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	border-radius: 14px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_InputToken_SellTax.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.frame_InputTokenInfos)

        self.horizontalSpacer_4 = QSpacerItem(14, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer_4)

        self.frame_OutPutTokenInfos = QFrame(self.frame_128)
        self.frame_OutPutTokenInfos.setObjectName(u"frame_OutPutTokenInfos")
        self.frame_OutPutTokenInfos.setMinimumSize(QSize(231, 90))
        self.frame_OutPutTokenInfos.setMaximumSize(QSize(231, 90))
        self.frame_OutPutTokenInfos.setStyleSheet(u"border:0;")
        self.frame_OutPutTokenInfos.setFrameShape(QFrame.StyledPanel)
        self.frame_OutPutTokenInfos.setFrameShadow(QFrame.Raised)
        self.label_90 = QLabel(self.frame_OutPutTokenInfos)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(-10, -10, 241, 40))
        self.label_90.setMinimumSize(QSize(40, 40))
        self.label_90.setStyleSheet(u"color: rgb(220, 161, 1);\n"
"text-decoration: underline;")
        self.label_91 = QLabel(self.frame_OutPutTokenInfos)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(10, 30, 101, 28))
        self.label_91.setMinimumSize(QSize(40, 27))
        self.label_91.setStyleSheet(u"")
        self.label_92 = QLabel(self.frame_OutPutTokenInfos)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(0, 60, 121, 28))
        self.label_92.setMinimumSize(QSize(50, 27))
        self.label_92.setStyleSheet(u"")
        self.lineEdit_OutputToken_BuyTax = QLineEdit(self.frame_OutPutTokenInfos)
        self.lineEdit_OutputToken_BuyTax.setObjectName(u"lineEdit_OutputToken_BuyTax")
        self.lineEdit_OutputToken_BuyTax.setGeometry(QRect(110, 30, 91, 28))
        self.lineEdit_OutputToken_BuyTax.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	border-radius: 14px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_OutputToken_BuyTax.setAlignment(Qt.AlignCenter)
        self.lineEdit_OutputToken_SellTax = QLineEdit(self.frame_OutPutTokenInfos)
        self.lineEdit_OutputToken_SellTax.setObjectName(u"lineEdit_OutputToken_SellTax")
        self.lineEdit_OutputToken_SellTax.setGeometry(QRect(110, 60, 91, 28))
        self.lineEdit_OutputToken_SellTax.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	border-radius: 14px;\n"
"	color: rgb(220, 161, 1);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_OutputToken_SellTax.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.frame_OutPutTokenInfos)

        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer_3)

        self.frame_23 = QFrame(self.page_swapping)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(9, 570, 981, 140))
        self.frame_23.setMinimumSize(QSize(700, 120))
        self.frame_23.setMaximumSize(QSize(16777215, 140))
        self.frame_23.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.frame_27 = QFrame(self.frame_23)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"border:0;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.frame_25 = QFrame(self.frame_27)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(0, 50, 471, 61))
        self.frame_25.setStyleSheet(u"border:0;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.label_43 = QLabel(self.frame_25)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(10, 10, 120, 50))
        self.label_43.setMinimumSize(QSize(120, 50))
        self.frame_81 = QFrame(self.frame_25)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setGeometry(QRect(125, 10, 351, 51))
        self.frame_81.setMinimumSize(QSize(0, 45))
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.slider_GasGwei_Swap = QSlider(self.frame_81)
        self.slider_GasGwei_Swap.setObjectName(u"slider_GasGwei_Swap")
        self.slider_GasGwei_Swap.setMaximumSize(QSize(275, 16777215))
        self.slider_GasGwei_Swap.setStyleSheet(u"color:rgb(220, 161, 1);")
        self.slider_GasGwei_Swap.setMinimum(5)
        self.slider_GasGwei_Swap.setMaximum(50)
        self.slider_GasGwei_Swap.setValue(6)
        self.slider_GasGwei_Swap.setOrientation(Qt.Horizontal)

        self.horizontalLayout_59.addWidget(self.slider_GasGwei_Swap)

        self.output_GasGwei_Swap = QLineEdit(self.frame_81)
        self.output_GasGwei_Swap.setObjectName(u"output_GasGwei_Swap")
        self.output_GasGwei_Swap.setMaximumSize(QSize(100, 16777215))
        self.output_GasGwei_Swap.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	border-radius: 14px;\n"
"	border: 5px solid rgb(33, 37, 43);\n"
"	color: rgb(220, 161, 1);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.output_GasGwei_Swap.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.output_GasGwei_Swap)

        self.frame_26 = QFrame(self.frame_27)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(10, -10, 471, 61))
        self.frame_26.setStyleSheet(u"border:0;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.label_85 = QLabel(self.frame_26)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(10, 10, 150, 50))
        self.label_85.setMinimumSize(QSize(150, 50))
        self.frame_82 = QFrame(self.frame_26)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setGeometry(QRect(110, 10, 351, 51))
        self.frame_82.setMinimumSize(QSize(0, 45))
        self.frame_82.setStyleSheet(u"border:0;")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.slider_Slippage_Swap = QSlider(self.frame_82)
        self.slider_Slippage_Swap.setObjectName(u"slider_Slippage_Swap")
        self.slider_Slippage_Swap.setMaximumSize(QSize(275, 16777215))
        self.slider_Slippage_Swap.setStyleSheet(u"color:rgb(220, 161, 1);")
        self.slider_Slippage_Swap.setMinimum(1)
        self.slider_Slippage_Swap.setMaximum(50)
        self.slider_Slippage_Swap.setValue(3)
        self.slider_Slippage_Swap.setOrientation(Qt.Horizontal)

        self.horizontalLayout_70.addWidget(self.slider_Slippage_Swap)

        self.output_Slippage_Swap = QLineEdit(self.frame_82)
        self.output_Slippage_Swap.setObjectName(u"output_Slippage_Swap")
        self.output_Slippage_Swap.setMaximumSize(QSize(100, 16777215))
        self.output_Slippage_Swap.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	border-radius: 14px;\n"
"	border: 5px solid rgb(33, 37, 43);\n"
"	color: rgb(220, 161, 1);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.output_Slippage_Swap.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_70.addWidget(self.output_Slippage_Swap)


        self.horizontalLayout_62.addWidget(self.frame_27)

        self.frame_87 = QFrame(self.frame_23)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setMinimumSize(QSize(350, 0))
        self.frame_87.setMaximumSize(QSize(16777215, 150))
        self.frame_87.setStyleSheet(u"border:0;")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_approve_token = QPushButton(self.frame_87)
        self.pushButton_approve_token.setObjectName(u"pushButton_approve_token")
        self.pushButton_approve_token.setEnabled(True)
        self.pushButton_approve_token.setMinimumSize(QSize(100, 80))
        self.pushButton_approve_token.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_approve_token.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 35px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_15.addWidget(self.pushButton_approve_token)

        self.pushButton_Confirm_Swap = QPushButton(self.frame_87)
        self.pushButton_Confirm_Swap.setObjectName(u"pushButton_Confirm_Swap")
        self.pushButton_Confirm_Swap.setEnabled(True)
        self.pushButton_Confirm_Swap.setMinimumSize(QSize(100, 80))
        self.pushButton_Confirm_Swap.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Confirm_Swap.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 35px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_15.addWidget(self.pushButton_Confirm_Swap)


        self.horizontalLayout_62.addWidget(self.frame_87)

        self.pushButton_Swap_changeInputTokenToOutputToken = QPushButton(self.page_swapping)
        self.pushButton_Swap_changeInputTokenToOutputToken.setObjectName(u"pushButton_Swap_changeInputTokenToOutputToken")
        self.pushButton_Swap_changeInputTokenToOutputToken.setGeometry(QRect(240, 240, 50, 50))
        self.pushButton_Swap_changeInputTokenToOutputToken.setMinimumSize(QSize(50, 50))
        self.pushButton_Swap_changeInputTokenToOutputToken.setMaximumSize(QSize(50, 50))
        self.pushButton_Swap_changeInputTokenToOutputToken.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 24%;\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/ChangeInputToken45x45.png);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	border: 8px solid rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 6px solid  rgb(220, 161, 1);\n"
"}")
        self.lineEdit_Swap_Error = QLineEdit(self.page_swapping)
        self.lineEdit_Swap_Error.setObjectName(u"lineEdit_Swap_Error")
        self.lineEdit_Swap_Error.setGeometry(QRect(140, 540, 691, 41))
        self.lineEdit_Swap_Error.setMinimumSize(QSize(0, 0))
        self.lineEdit_Swap_Error.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_Swap_Error.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(170, 0, 0);\n"
"	background-color: rgb(39, 44, 54);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_Swap_Error.setAlignment(Qt.AlignCenter)
        self.lineEdit_Swap_Error.setReadOnly(False)
        self.lineEdit_Swap_Error.setClearButtonEnabled(True)
        self.stackedWidget.addWidget(self.page_swapping)
        self.frame_6.raise_()
        self.frame_2.raise_()
        self.frame_7.raise_()
        self.frame_128.raise_()
        self.frame_23.raise_()
        self.pushButton_Swap_changeInputTokenToOutputToken.raise_()
        self.lineEdit_Swap_Error.raise_()
        self.page_swapping_Confirm = QWidget()
        self.page_swapping_Confirm.setObjectName(u"page_swapping_Confirm")
        self.verticalLayout_33 = QVBoxLayout(self.page_swapping_Confirm)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_129 = QFrame(self.page_swapping_Confirm)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setMinimumSize(QSize(0, 120))
        self.frame_129.setMaximumSize(QSize(16777215, 130))
        self.frame_129.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_129)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.frame_131 = QFrame(self.frame_129)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setStyleSheet(u"border:0;")
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.label_88 = QLabel(self.frame_131)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(230, 60, 191, 25))
        self.label_89 = QLabel(self.frame_131)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(0, 0, 391, 61))
        self.label_89.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")

        self.horizontalLayout_58.addWidget(self.frame_131)

        self.frame_132 = QFrame(self.frame_129)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setStyleSheet(u"border:0;")
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_132)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")

        self.horizontalLayout_58.addWidget(self.frame_132)


        self.verticalLayout_33.addWidget(self.frame_129)

        self.frame_133 = QFrame(self.page_swapping_Confirm)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border-radius: 60px;\n"
"}	")
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_133)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.frame_134 = QFrame(self.frame_133)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setStyleSheet(u"\n"
"	background-color:rgba(255, 0, 0, 0);")
        self.frame_134.setFrameShape(QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_72.addWidget(self.frame_134)

        self.frame_135 = QFrame(self.frame_133)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_135)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_136 = QFrame(self.frame_135)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_136)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_42 = QLabel(self.frame_136)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_13.addWidget(self.label_42)

        self.label_swap_inputToken = QLabel(self.frame_136)
        self.label_swap_inputToken.setObjectName(u"label_swap_inputToken")
        self.label_swap_inputToken.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_13.addWidget(self.label_swap_inputToken)

        self.frame_143 = QFrame(self.frame_136)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setMaximumSize(QSize(30, 30))
        self.frame_143.setStyleSheet(u"background-image: url(:/Fontawsome/icons/fontawsome/angel-double25x25.png);")
        self.frame_143.setFrameShape(QFrame.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_143)

        self.frame_149 = QFrame(self.frame_136)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setMinimumSize(QSize(20, 0))
        self.frame_149.setMaximumSize(QSize(50, 16777215))
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_149)

        self.label_swap_outputToken = QLabel(self.frame_136)
        self.label_swap_outputToken.setObjectName(u"label_swap_outputToken")
        self.label_swap_outputToken.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_13.addWidget(self.label_swap_outputToken)


        self.verticalLayout_7.addWidget(self.frame_136)

        self.frame_137 = QFrame(self.frame_135)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setLayoutDirection(Qt.LeftToRight)
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_137)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_105 = QLabel(self.frame_137)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_14.addWidget(self.label_105)

        self.label_SwapWayA_confirm = QLabel(self.frame_137)
        self.label_SwapWayA_confirm.setObjectName(u"label_SwapWayA_confirm")
        self.label_SwapWayA_confirm.setMinimumSize(QSize(64, 64))
        self.label_SwapWayA_confirm.setMaximumSize(QSize(64, 64))
        self.label_SwapWayA_confirm.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_14.addWidget(self.label_SwapWayA_confirm)

        self.frame_138 = QFrame(self.frame_137)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setMaximumSize(QSize(30, 30))
        self.frame_138.setStyleSheet(u"background-image: url(:/Fontawsome/icons/fontawsome/angel-double25x25.png);")
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.frame_138)

        self.label_SwapWayB_confirm = QLabel(self.frame_137)
        self.label_SwapWayB_confirm.setObjectName(u"label_SwapWayB_confirm")
        self.label_SwapWayB_confirm.setMinimumSize(QSize(64, 64))
        self.label_SwapWayB_confirm.setMaximumSize(QSize(64, 64))
        self.label_SwapWayB_confirm.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_14.addWidget(self.label_SwapWayB_confirm)

        self.frame_SwapWayC_2 = QFrame(self.frame_137)
        self.frame_SwapWayC_2.setObjectName(u"frame_SwapWayC_2")
        self.frame_SwapWayC_2.setMaximumSize(QSize(30, 30))
        self.frame_SwapWayC_2.setStyleSheet(u"background-image: url(:/Fontawsome/icons/fontawsome/angel-double25x25.png);")
        self.frame_SwapWayC_2.setFrameShape(QFrame.StyledPanel)
        self.frame_SwapWayC_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.frame_SwapWayC_2)

        self.label_SwapWayC_confirm = QLabel(self.frame_137)
        self.label_SwapWayC_confirm.setObjectName(u"label_SwapWayC_confirm")
        self.label_SwapWayC_confirm.setMinimumSize(QSize(64, 64))
        self.label_SwapWayC_confirm.setMaximumSize(QSize(64, 64))
        self.label_SwapWayC_confirm.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_14.addWidget(self.label_SwapWayC_confirm)

        self.frame_SwapWayC_3 = QFrame(self.frame_137)
        self.frame_SwapWayC_3.setObjectName(u"frame_SwapWayC_3")
        self.frame_SwapWayC_3.setMaximumSize(QSize(30, 30))
        self.frame_SwapWayC_3.setStyleSheet(u"background-image: url(:/Fontawsome/icons/fontawsome/angel-double25x25.png);")
        self.frame_SwapWayC_3.setFrameShape(QFrame.StyledPanel)
        self.frame_SwapWayC_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.frame_SwapWayC_3)

        self.label_SwapWayD_confirm = QLabel(self.frame_137)
        self.label_SwapWayD_confirm.setObjectName(u"label_SwapWayD_confirm")
        self.label_SwapWayD_confirm.setMinimumSize(QSize(64, 64))
        self.label_SwapWayD_confirm.setMaximumSize(QSize(64, 64))
        self.label_SwapWayD_confirm.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_14.addWidget(self.label_SwapWayD_confirm)


        self.verticalLayout_7.addWidget(self.frame_137)

        self.frame_139 = QFrame(self.frame_135)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_139)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_97 = QLabel(self.frame_139)
        self.label_97.setObjectName(u"label_97")

        self.horizontalLayout_74.addWidget(self.label_97)

        self.frame_140 = QFrame(self.frame_139)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setMinimumSize(QSize(100, 0))
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.label_102 = QLabel(self.frame_140)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(10, -10, 87, 82))

        self.horizontalLayout_74.addWidget(self.frame_140)

        self.output_swapspendAmount = QLineEdit(self.frame_139)
        self.output_swapspendAmount.setObjectName(u"output_swapspendAmount")
        self.output_swapspendAmount.setEnabled(True)
        self.output_swapspendAmount.setMinimumSize(QSize(0, 30))
        self.output_swapspendAmount.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_swapspendAmount.setReadOnly(True)
        self.output_swapspendAmount.setClearButtonEnabled(False)

        self.horizontalLayout_74.addWidget(self.output_swapspendAmount)

        self.frame_141 = QFrame(self.frame_139)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setMinimumSize(QSize(200, 0))
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_141)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_98 = QLabel(self.frame_141)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(0, 0))
        self.label_98.setMaximumSize(QSize(35, 16777215))
        self.label_98.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_75.addWidget(self.label_98)

        self.output_swapspendAmountUSD = QLineEdit(self.frame_141)
        self.output_swapspendAmountUSD.setObjectName(u"output_swapspendAmountUSD")
        self.output_swapspendAmountUSD.setEnabled(True)
        self.output_swapspendAmountUSD.setMinimumSize(QSize(150, 30))
        self.output_swapspendAmountUSD.setMaximumSize(QSize(150, 16777215))
        self.output_swapspendAmountUSD.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_swapspendAmountUSD.setReadOnly(True)
        self.output_swapspendAmountUSD.setClearButtonEnabled(False)

        self.horizontalLayout_75.addWidget(self.output_swapspendAmountUSD)


        self.horizontalLayout_74.addWidget(self.frame_141)

        self.label_TokenAmountInUsdt_2 = QLabel(self.frame_139)
        self.label_TokenAmountInUsdt_2.setObjectName(u"label_TokenAmountInUsdt_2")

        self.horizontalLayout_74.addWidget(self.label_TokenAmountInUsdt_2)


        self.verticalLayout_7.addWidget(self.frame_139)

        self.frame_142 = QFrame(self.frame_135)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_142)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_103 = QLabel(self.frame_142)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_73.addWidget(self.label_103)

        self.frame_144 = QFrame(self.frame_142)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setMinimumSize(QSize(0, 0))
        self.frame_144.setMaximumSize(QSize(380, 16777215))
        self.frame_144.setFrameShape(QFrame.StyledPanel)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.output_swapminreceivedAmount = QLineEdit(self.frame_144)
        self.output_swapminreceivedAmount.setObjectName(u"output_swapminreceivedAmount")
        self.output_swapminreceivedAmount.setEnabled(True)
        self.output_swapminreceivedAmount.setGeometry(QRect(10, 10, 337, 41))
        self.output_swapminreceivedAmount.setMinimumSize(QSize(0, 30))
        self.output_swapminreceivedAmount.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_swapminreceivedAmount.setReadOnly(True)
        self.output_swapminreceivedAmount.setClearButtonEnabled(False)

        self.horizontalLayout_73.addWidget(self.frame_144)

        self.label_104 = QLabel(self.frame_142)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMinimumSize(QSize(0, 0))
        self.label_104.setMaximumSize(QSize(35, 16777215))
        self.label_104.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_73.addWidget(self.label_104)

        self.output_swapminreceivedAmountUSD = QLineEdit(self.frame_142)
        self.output_swapminreceivedAmountUSD.setObjectName(u"output_swapminreceivedAmountUSD")
        self.output_swapminreceivedAmountUSD.setEnabled(True)
        self.output_swapminreceivedAmountUSD.setMinimumSize(QSize(150, 30))
        self.output_swapminreceivedAmountUSD.setMaximumSize(QSize(150, 16777215))
        self.output_swapminreceivedAmountUSD.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_swapminreceivedAmountUSD.setReadOnly(True)
        self.output_swapminreceivedAmountUSD.setClearButtonEnabled(False)

        self.horizontalLayout_73.addWidget(self.output_swapminreceivedAmountUSD)


        self.verticalLayout_7.addWidget(self.frame_142)

        self.frame_145 = QFrame(self.frame_135)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setFrameShape(QFrame.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_145)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_100 = QLabel(self.frame_145)
        self.label_100.setObjectName(u"label_100")

        self.horizontalLayout_77.addWidget(self.label_100)

        self.output_swap_GasBNB = QLineEdit(self.frame_145)
        self.output_swap_GasBNB.setObjectName(u"output_swap_GasBNB")
        self.output_swap_GasBNB.setEnabled(True)
        self.output_swap_GasBNB.setMinimumSize(QSize(250, 30))
        self.output_swap_GasBNB.setMaximumSize(QSize(100, 16777215))
        self.output_swap_GasBNB.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_swap_GasBNB.setReadOnly(True)
        self.output_swap_GasBNB.setClearButtonEnabled(False)

        self.horizontalLayout_77.addWidget(self.output_swap_GasBNB)

        self.label_send_TokenName_4 = QLabel(self.frame_145)
        self.label_send_TokenName_4.setObjectName(u"label_send_TokenName_4")
        self.label_send_TokenName_4.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_77.addWidget(self.label_send_TokenName_4)

        self.label_101 = QLabel(self.frame_145)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMinimumSize(QSize(0, 0))
        self.label_101.setMaximumSize(QSize(35, 16777215))
        self.label_101.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_77.addWidget(self.label_101)

        self.label_send_Gas_3 = QLabel(self.frame_145)
        self.label_send_Gas_3.setObjectName(u"label_send_Gas_3")
        self.label_send_Gas_3.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_77.addWidget(self.label_send_Gas_3)

        self.output_swap_GasUSD = QLineEdit(self.frame_145)
        self.output_swap_GasUSD.setObjectName(u"output_swap_GasUSD")
        self.output_swap_GasUSD.setEnabled(True)
        self.output_swap_GasUSD.setMinimumSize(QSize(120, 30))
        self.output_swap_GasUSD.setMaximumSize(QSize(100, 16777215))
        self.output_swap_GasUSD.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_swap_GasUSD.setReadOnly(True)
        self.output_swap_GasUSD.setClearButtonEnabled(False)

        self.horizontalLayout_77.addWidget(self.output_swap_GasUSD)

        self.label_send_Gas_4 = QLabel(self.frame_145)
        self.label_send_Gas_4.setObjectName(u"label_send_Gas_4")
        self.label_send_Gas_4.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_77.addWidget(self.label_send_Gas_4)


        self.verticalLayout_7.addWidget(self.frame_145)

        self.frame_146 = QFrame(self.frame_135)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setFrameShape(QFrame.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_146)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.pushButton_Cancel_SwapConfirm = QPushButton(self.frame_146)
        self.pushButton_Cancel_SwapConfirm.setObjectName(u"pushButton_Cancel_SwapConfirm")
        self.pushButton_Cancel_SwapConfirm.setMinimumSize(QSize(0, 60))
        self.pushButton_Cancel_SwapConfirm.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	color:rgb(170, 0, 0);\n"
"	font-size:15px;\n"
"	border-radius: 25px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_78.addWidget(self.pushButton_Cancel_SwapConfirm)

        self.pushButton_SwapConfirm = QPushButton(self.frame_146)
        self.pushButton_SwapConfirm.setObjectName(u"pushButton_SwapConfirm")
        self.pushButton_SwapConfirm.setMinimumSize(QSize(0, 60))
        self.pushButton_SwapConfirm.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size:15px;\n"
"	color: rgb(85, 170, 0);\n"
"	border-radius: 25px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_78.addWidget(self.pushButton_SwapConfirm)


        self.verticalLayout_7.addWidget(self.frame_146)


        self.horizontalLayout_72.addWidget(self.frame_135)

        self.frame_147 = QFrame(self.frame_133)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setStyleSheet(u"\n"
"	background-color:rgba(255, 0, 0, 0);")
        self.frame_147.setFrameShape(QFrame.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_72.addWidget(self.frame_147)


        self.verticalLayout_33.addWidget(self.frame_133)

        self.stackedWidget.addWidget(self.page_swapping_Confirm)
        self.page_approve_Confirm = QWidget()
        self.page_approve_Confirm.setObjectName(u"page_approve_Confirm")
        self.verticalLayout_35 = QVBoxLayout(self.page_approve_Confirm)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_148 = QFrame(self.page_approve_Confirm)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setMinimumSize(QSize(0, 120))
        self.frame_148.setMaximumSize(QSize(16777215, 130))
        self.frame_148.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"")
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_148)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.frame_150 = QFrame(self.frame_148)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setStyleSheet(u"border:0;")
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.label_99 = QLabel(self.frame_150)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(230, 60, 191, 25))
        self.label_106 = QLabel(self.frame_150)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setGeometry(QRect(0, 0, 391, 61))
        self.label_106.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")

        self.horizontalLayout_76.addWidget(self.frame_150)

        self.frame_151 = QFrame(self.frame_148)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setStyleSheet(u"border:0;")
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_151)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")

        self.horizontalLayout_76.addWidget(self.frame_151)


        self.verticalLayout_35.addWidget(self.frame_148)

        self.frame_152 = QFrame(self.page_approve_Confirm)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border-radius: 60px;\n"
"}	")
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_152)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.frame_153 = QFrame(self.frame_152)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setStyleSheet(u"\n"
"	background-color:rgba(255, 0, 0, 0);")
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_80.addWidget(self.frame_153)

        self.frame_154 = QFrame(self.frame_152)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_154)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_155 = QFrame(self.frame_154)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_155)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_107 = QLabel(self.frame_155)
        self.label_107.setObjectName(u"label_107")

        self.horizontalLayout_81.addWidget(self.label_107)

        self.label_approve_TokenName = QLabel(self.frame_155)
        self.label_approve_TokenName.setObjectName(u"label_approve_TokenName")
        self.label_approve_TokenName.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_81.addWidget(self.label_approve_TokenName)

        self.frame_156 = QFrame(self.frame_155)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setFrameShape(QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Raised)
        self.label_approv_tokenLogo = QLabel(self.frame_156)
        self.label_approv_tokenLogo.setObjectName(u"label_approv_tokenLogo")
        self.label_approv_tokenLogo.setGeometry(QRect(70, 20, 64, 64))
        self.label_approv_tokenLogo.setMinimumSize(QSize(64, 64))
        self.label_approv_tokenLogo.setMaximumSize(QSize(64, 64))
        self.label_approv_tokenLogo.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_81.addWidget(self.frame_156)

        self.frame_157 = QFrame(self.frame_155)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_81.addWidget(self.frame_157)


        self.verticalLayout_34.addWidget(self.frame_155)

        self.frame_161 = QFrame(self.frame_154)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_161)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.label_110 = QLabel(self.frame_161)
        self.label_110.setObjectName(u"label_110")

        self.horizontalLayout_84.addWidget(self.label_110)

        self.frame_162 = QFrame(self.frame_161)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setMinimumSize(QSize(160, 0))
        self.frame_162.setFrameShape(QFrame.StyledPanel)
        self.frame_162.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_84.addWidget(self.frame_162)

        self.output_approve_Address = QLineEdit(self.frame_161)
        self.output_approve_Address.setObjectName(u"output_approve_Address")
        self.output_approve_Address.setEnabled(True)
        self.output_approve_Address.setMinimumSize(QSize(420, 30))
        self.output_approve_Address.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_approve_Address.setReadOnly(True)
        self.output_approve_Address.setClearButtonEnabled(False)

        self.horizontalLayout_84.addWidget(self.output_approve_Address)

        self.frame_163 = QFrame(self.frame_161)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setMinimumSize(QSize(0, 0))
        self.frame_163.setFrameShape(QFrame.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_84.addWidget(self.frame_163)

        self.label_send_Receiver_2 = QLabel(self.frame_161)
        self.label_send_Receiver_2.setObjectName(u"label_send_Receiver_2")
        self.label_send_Receiver_2.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_84.addWidget(self.label_send_Receiver_2)


        self.verticalLayout_34.addWidget(self.frame_161)

        self.frame_164 = QFrame(self.frame_154)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setFrameShape(QFrame.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_164)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_111 = QLabel(self.frame_164)
        self.label_111.setObjectName(u"label_111")

        self.horizontalLayout_85.addWidget(self.label_111)

        self.output_approve_GasBNB = QLineEdit(self.frame_164)
        self.output_approve_GasBNB.setObjectName(u"output_approve_GasBNB")
        self.output_approve_GasBNB.setEnabled(True)
        self.output_approve_GasBNB.setMinimumSize(QSize(250, 30))
        self.output_approve_GasBNB.setMaximumSize(QSize(100, 16777215))
        self.output_approve_GasBNB.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_approve_GasBNB.setReadOnly(True)
        self.output_approve_GasBNB.setClearButtonEnabled(False)

        self.horizontalLayout_85.addWidget(self.output_approve_GasBNB)

        self.label_send_TokenName_5 = QLabel(self.frame_164)
        self.label_send_TokenName_5.setObjectName(u"label_send_TokenName_5")
        self.label_send_TokenName_5.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_85.addWidget(self.label_send_TokenName_5)

        self.label_112 = QLabel(self.frame_164)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setMinimumSize(QSize(0, 0))
        self.label_112.setMaximumSize(QSize(35, 16777215))
        self.label_112.setPixmap(QPixmap(u":/Fontawsome/icons/fontawsome/dtilde34x20.png"))

        self.horizontalLayout_85.addWidget(self.label_112)

        self.label_send_Gas_5 = QLabel(self.frame_164)
        self.label_send_Gas_5.setObjectName(u"label_send_Gas_5")
        self.label_send_Gas_5.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_85.addWidget(self.label_send_Gas_5)

        self.output_approve_FeeUSD = QLineEdit(self.frame_164)
        self.output_approve_FeeUSD.setObjectName(u"output_approve_FeeUSD")
        self.output_approve_FeeUSD.setEnabled(True)
        self.output_approve_FeeUSD.setMinimumSize(QSize(20, 30))
        self.output_approve_FeeUSD.setMaximumSize(QSize(150, 16777215))
        self.output_approve_FeeUSD.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color: rgb(219, 160, 6);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.output_approve_FeeUSD.setReadOnly(True)
        self.output_approve_FeeUSD.setClearButtonEnabled(False)

        self.horizontalLayout_85.addWidget(self.output_approve_FeeUSD)

        self.label_send_Gas_6 = QLabel(self.frame_164)
        self.label_send_Gas_6.setObjectName(u"label_send_Gas_6")
        self.label_send_Gas_6.setStyleSheet(u"color: rgb(219, 160, 6);")

        self.horizontalLayout_85.addWidget(self.label_send_Gas_6)


        self.verticalLayout_34.addWidget(self.frame_164)

        self.frame_165 = QFrame(self.frame_154)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setFrameShape(QFrame.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_165)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.pushButton_approve_cancel = QPushButton(self.frame_165)
        self.pushButton_approve_cancel.setObjectName(u"pushButton_approve_cancel")
        self.pushButton_approve_cancel.setMinimumSize(QSize(0, 60))
        self.pushButton_approve_cancel.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	color:rgb(170, 0, 0);\n"
"	font-size:15px;\n"
"	border-radius: 25px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_86.addWidget(self.pushButton_approve_cancel)

        self.pushButton_approve_Confirm = QPushButton(self.frame_165)
        self.pushButton_approve_Confirm.setObjectName(u"pushButton_approve_Confirm")
        self.pushButton_approve_Confirm.setMinimumSize(QSize(0, 60))
        self.pushButton_approve_Confirm.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size:15px;\n"
"	color: rgb(85, 170, 0);\n"
"	border-radius: 25px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_86.addWidget(self.pushButton_approve_Confirm)


        self.verticalLayout_34.addWidget(self.frame_165)


        self.horizontalLayout_80.addWidget(self.frame_154)

        self.frame_166 = QFrame(self.frame_152)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setStyleSheet(u"\n"
"	background-color:rgba(255, 0, 0, 0);")
        self.frame_166.setFrameShape(QFrame.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_80.addWidget(self.frame_166)


        self.verticalLayout_35.addWidget(self.frame_152)

        self.stackedWidget.addWidget(self.page_approve_Confirm)
        self.page_import_Secret_Key = QWidget()
        self.page_import_Secret_Key.setObjectName(u"page_import_Secret_Key")
        self.pushButton_import_wallet = QPushButton(self.page_import_Secret_Key)
        self.pushButton_import_wallet.setObjectName(u"pushButton_import_wallet")
        self.pushButton_import_wallet.setGeometry(QRect(210, 500, 641, 91))
        self.pushButton_import_wallet.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 35px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_back_Login_2 = QPushButton(self.page_import_Secret_Key)
        self.pushButton_back_Login_2.setObjectName(u"pushButton_back_Login_2")
        self.pushButton_back_Login_2.setGeometry(QRect(20, 500, 141, 91))
        self.pushButton_back_Login_2.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/Fontawsome/icons/fontawsome/Back.png) ;\n"
"	font: bold;\n"
"	border-radius: 35px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.input_import_walletname = QLineEdit(self.page_import_Secret_Key)
        self.input_import_walletname.setObjectName(u"input_import_walletname")
        self.input_import_walletname.setGeometry(QRect(320, 180, 461, 41))
        self.input_import_walletname.setMinimumSize(QSize(0, 30))
        self.input_import_walletname.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_import_walletname.setClearButtonEnabled(True)
        self.label_17 = QLabel(self.page_import_Secret_Key)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 250, 311, 41))
        self.input_import_walletpw = QLineEdit(self.page_import_Secret_Key)
        self.input_import_walletpw.setObjectName(u"input_import_walletpw")
        self.input_import_walletpw.setGeometry(QRect(320, 250, 461, 41))
        self.input_import_walletpw.setMinimumSize(QSize(0, 30))
        self.input_import_walletpw.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_import_walletpw.setEchoMode(QLineEdit.Password)
        self.input_import_walletpw.setClearButtonEnabled(True)
        self.label_18 = QLabel(self.page_import_Secret_Key)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 180, 191, 41))
        self.label_19 = QLabel(self.page_import_Secret_Key)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(50, 320, 311, 41))
        self.label_8 = QLabel(self.page_import_Secret_Key)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(190, 60, 241, 71))
        self.label_20 = QLabel(self.page_import_Secret_Key)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 10, 461, 91))
        self.label_20.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_imported_replay = QFrame(self.page_import_Secret_Key)
        self.frame_imported_replay.setObjectName(u"frame_imported_replay")
        self.frame_imported_replay.setEnabled(False)
        self.frame_imported_replay.setGeometry(QRect(30, 400, 851, 71))
        self.frame_imported_replay.setStyleSheet(u"QWidget {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	border-radius: 25px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"    }")
        self.frame_imported_replay.setFrameShape(QFrame.StyledPanel)
        self.frame_imported_replay.setFrameShadow(QFrame.Raised)
        self.label_22 = QLabel(self.frame_imported_replay)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(60, 20, 201, 51))
        self.textBrowser_imported_address = QTextBrowser(self.frame_imported_replay)
        self.textBrowser_imported_address.setObjectName(u"textBrowser_imported_address")
        self.textBrowser_imported_address.setGeometry(QRect(280, 30, 561, 31))
        self.label_25 = QLabel(self.frame_imported_replay)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(320, 5, 211, 31))
        self.label_25.setStyleSheet(u"color: rgb(19, 150, 16) ;")
        self.frame_16 = QFrame(self.frame_imported_replay)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(300, -40, 461, 51))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_Invalid_key = QFrame(self.page_import_Secret_Key)
        self.frame_Invalid_key.setObjectName(u"frame_Invalid_key")
        self.frame_Invalid_key.setEnabled(True)
        self.frame_Invalid_key.setGeometry(QRect(320, 320, 461, 61))
        self.frame_Invalid_key.setStyleSheet(u"font-size:24px;\n"
"background-color: rgb(130, 0, 0);\n"
"border: 6px solid rgb(33, 37, 43);\n"
"border-radius: 25px;\n"
"padding-left: 10px;\n"
"")
        self.frame_Invalid_key.setFrameShape(QFrame.StyledPanel)
        self.frame_Invalid_key.setFrameShadow(QFrame.Raised)
        self.label_29 = QLabel(self.frame_Invalid_key)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(150, 30, 161, 31))
        self.label_29.setStyleSheet(u"background-color:rgba(0, 255, 0, 0);\n"
"border: 0 px solid rgb(33, 37, 43);")
        self.input_import_key = QLineEdit(self.page_import_Secret_Key)
        self.input_import_key.setObjectName(u"input_import_key")
        self.input_import_key.setEnabled(True)
        self.input_import_key.setGeometry(QRect(320, 320, 461, 41))
        self.input_import_key.setMinimumSize(QSize(0, 30))
        self.input_import_key.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_import_key.setInputMask(u"")
        self.input_import_key.setText(u"")
        self.input_import_key.setEchoMode(QLineEdit.Password)
        self.input_import_key.setClearButtonEnabled(True)
        self.frame_112 = QFrame(self.page_import_Secret_Key)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setGeometry(QRect(740, 10, 341, 411))
        self.frame_112.setStyleSheet(u"background-image: url(:/Fontawsome/icons/fontawsome/Trading_Tigers_Logo.png);\n"
"background-repeat: no-reperat;")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.stackedWidget.addWidget(self.page_import_Secret_Key)
        self.frame_Invalid_key.raise_()
        self.pushButton_import_wallet.raise_()
        self.pushButton_back_Login_2.raise_()
        self.input_import_walletname.raise_()
        self.label_17.raise_()
        self.input_import_walletpw.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_8.raise_()
        self.label_20.raise_()
        self.frame_imported_replay.raise_()
        self.input_import_key.raise_()
        self.frame_112.raise_()
        self.page_transactions = QWidget()
        self.page_transactions.setObjectName(u"page_transactions")
        self.verticalLayout_6 = QVBoxLayout(self.page_transactions)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_transactions)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_6.addWidget(self.frame)

        self.frame_5 = QFrame(self.page_transactions)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 100))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_24 = QLabel(self.frame_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(0, 0, 401, 71))
        self.label_24.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")
        self.label_36 = QLabel(self.frame_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(220, 30, 261, 71))

        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.page_transactions)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_transactions = QTableWidget(self.frame_3)
        if (self.tableWidget_transactions.columnCount() < 7):
            self.tableWidget_transactions.setColumnCount(7)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_transactions.setHorizontalHeaderItem(0, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_transactions.setHorizontalHeaderItem(1, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_transactions.setHorizontalHeaderItem(2, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_transactions.setHorizontalHeaderItem(3, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_transactions.setHorizontalHeaderItem(4, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_transactions.setHorizontalHeaderItem(5, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_transactions.setHorizontalHeaderItem(6, __qtablewidgetitem125)
        if (self.tableWidget_transactions.rowCount() < 16):
            self.tableWidget_transactions.setRowCount(16)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setFont(font3);
        self.tableWidget_transactions.setVerticalHeaderItem(0, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(1, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(2, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(3, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(4, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(5, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(6, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(7, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(8, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(9, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(10, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(11, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(12, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(13, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(14, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget_transactions.setVerticalHeaderItem(15, __qtablewidgetitem141)
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        __qtablewidgetitem142 = QTableWidgetItem()
        __qtablewidgetitem142.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem142.setFont(font4);
        self.tableWidget_transactions.setItem(0, 0, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        __qtablewidgetitem143.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem143.setFont(font4);
        self.tableWidget_transactions.setItem(0, 1, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        __qtablewidgetitem144.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem144.setFont(font4);
        self.tableWidget_transactions.setItem(0, 2, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        __qtablewidgetitem145.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem145.setFont(font4);
        self.tableWidget_transactions.setItem(0, 3, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        __qtablewidgetitem146.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem146.setFont(font4);
        self.tableWidget_transactions.setItem(0, 4, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        __qtablewidgetitem147.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem147.setFont(font4);
        self.tableWidget_transactions.setItem(0, 5, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        __qtablewidgetitem148.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem148.setFont(font4);
        self.tableWidget_transactions.setItem(0, 6, __qtablewidgetitem148)
        self.tableWidget_transactions.setObjectName(u"tableWidget_transactions")
        sizePolicy.setHeightForWidth(self.tableWidget_transactions.sizePolicy().hasHeightForWidth())
        self.tableWidget_transactions.setSizePolicy(sizePolicy)
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush26 = QBrush(QColor(210, 210, 210, 128))
        brush26.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush26)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush27 = QBrush(QColor(210, 210, 210, 128))
        brush27.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush27)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush28 = QBrush(QColor(210, 210, 210, 128))
        brush28.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush28)
#endif
        self.tableWidget_transactions.setPalette(palette4)
        self.tableWidget_transactions.setMouseTracking(True)
        self.tableWidget_transactions.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_transactions.setFrameShape(QFrame.NoFrame)
        self.tableWidget_transactions.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_transactions.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_transactions.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_transactions.setDragEnabled(True)
        self.tableWidget_transactions.setDragDropMode(QAbstractItemView.DragOnly)
        self.tableWidget_transactions.setDefaultDropAction(Qt.CopyAction)
        self.tableWidget_transactions.setAlternatingRowColors(False)
        self.tableWidget_transactions.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_transactions.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_transactions.setShowGrid(True)
        self.tableWidget_transactions.setGridStyle(Qt.SolidLine)
        self.tableWidget_transactions.setSortingEnabled(False)
        self.tableWidget_transactions.horizontalHeader().setVisible(False)
        self.tableWidget_transactions.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_transactions.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_transactions.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_transactions.verticalHeader().setVisible(False)
        self.tableWidget_transactions.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_transactions.verticalHeader().setHighlightSections(False)
        self.tableWidget_transactions.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_12.addWidget(self.tableWidget_transactions)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_transactions)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_24 = QVBoxLayout(self.page_settings)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_83 = QFrame(self.page_settings)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(0, 52))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_83)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, -10, 221, 71))
        self.label_14 = QLabel(self.frame_83)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 0, 381, 61))
        self.label_14.setStyleSheet(u"QLabel {\n"
"	background-image:url(:/Fontawsome/icons/fontawsome/TradingTigers.png);\n"
"	background-repeat: no-reperat;\n"
"}")

        self.verticalLayout_24.addWidget(self.frame_83)

        self.frame_84 = QFrame(self.page_settings)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(0, 460))
        self.frame_84.setMaximumSize(QSize(16777215, 480))
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(-1, 0, -1, 0)
        self.stackedWidget_158 = QStackedWidget(self.frame_84)
        self.stackedWidget_158.setObjectName(u"stackedWidget_158")
        self.stackedWidget_158.setMinimumSize(QSize(400, 400))
        self.stackedWidget_158.setMaximumSize(QSize(400, 16777215))
        self.stackedWidget_158.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget_158.setFrameShadow(QFrame.Raised)
        self.stackedWidget_158Page1 = QWidget()
        self.stackedWidget_158Page1.setObjectName(u"stackedWidget_158Page1")
        self.frame_add_Provider = QFrame(self.stackedWidget_158Page1)
        self.frame_add_Provider.setObjectName(u"frame_add_Provider")
        self.frame_add_Provider.setGeometry(QRect(10, 20, 391, 431))
        self.frame_add_Provider.setStyleSheet(u"QFrame {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	background-color: rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border-radius: 60px;\n"
"}	")
        self.frame_add_Provider.setFrameShape(QFrame.StyledPanel)
        self.frame_add_Provider.setFrameShadow(QFrame.Raised)
        self.label_109 = QLabel(self.frame_add_Provider)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setGeometry(QRect(80, 20, 255, 30))
        self.label_109.setStyleSheet(u"color: rgb(220, 161, 1);")
        self.pushButton_add_ProviderSubmit = QPushButton(self.frame_add_Provider)
        self.pushButton_add_ProviderSubmit.setObjectName(u"pushButton_add_ProviderSubmit")
        self.pushButton_add_ProviderSubmit.setEnabled(True)
        self.pushButton_add_ProviderSubmit.setGeometry(QRect(220, 370, 131, 41))
        self.pushButton_add_ProviderSubmit.setMinimumSize(QSize(0, 20))
        self.pushButton_add_ProviderSubmit.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.label_113 = QLabel(self.frame_add_Provider)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(60, 70, 261, 41))
        self.input_add_ProviderName = QLineEdit(self.frame_add_Provider)
        self.input_add_ProviderName.setObjectName(u"input_add_ProviderName")
        self.input_add_ProviderName.setGeometry(QRect(10, 120, 371, 41))
        self.input_add_ProviderName.setMinimumSize(QSize(0, 30))
        self.input_add_ProviderName.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color:rgb(220, 161, 1);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_add_ProviderName.setClearButtonEnabled(True)
        self.input_add_ProviderURL = QLineEdit(self.frame_add_Provider)
        self.input_add_ProviderURL.setObjectName(u"input_add_ProviderURL")
        self.input_add_ProviderURL.setGeometry(QRect(10, 230, 371, 41))
        self.input_add_ProviderURL.setMinimumSize(QSize(0, 30))
        self.input_add_ProviderURL.setStyleSheet(u"QLineEdit {\n"
"	font-size: 24px;\n"
"	color:rgb(220, 161, 1);\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 15px;\n"
"	border: 5px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_add_ProviderURL.setClearButtonEnabled(True)
        self.label_114 = QLabel(self.frame_add_Provider)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setGeometry(QRect(60, 180, 261, 41))
        self.pushButton_add_ProviderCancel = QPushButton(self.frame_add_Provider)
        self.pushButton_add_ProviderCancel.setObjectName(u"pushButton_add_ProviderCancel")
        self.pushButton_add_ProviderCancel.setEnabled(True)
        self.pushButton_add_ProviderCancel.setGeometry(QRect(40, 370, 131, 41))
        self.pushButton_add_ProviderCancel.setMinimumSize(QSize(0, 20))
        self.pushButton_add_ProviderCancel.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_add_provider_Error = QLineEdit(self.frame_add_Provider)
        self.lineEdit_add_provider_Error.setObjectName(u"lineEdit_add_provider_Error")
        self.lineEdit_add_provider_Error.setGeometry(QRect(10, 310, 351, 40))
        self.lineEdit_add_provider_Error.setMinimumSize(QSize(0, 40))
        self.lineEdit_add_provider_Error.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_add_provider_Error.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 22px;\n"
"	border-radius: 20px;\n"
"	color: rgb(255, 8, 0);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_add_provider_Error.setAlignment(Qt.AlignCenter)
        self.lineEdit_add_provider_Error.setDragEnabled(True)
        self.lineEdit_add_provider_Error.setReadOnly(True)
        self.stackedWidget_158.addWidget(self.stackedWidget_158Page1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_158.addWidget(self.page_2)

        self.horizontalLayout_82.addWidget(self.stackedWidget_158)

        self.frame_121 = QFrame(self.frame_84)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setMinimumSize(QSize(400, 350))
        self.frame_121.setMaximumSize(QSize(166666, 480))
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_121)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_85 = QFrame(self.frame_121)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMaximumSize(QSize(16777215, 50))
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.label_108 = QLabel(self.frame_85)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setStyleSheet(u"color: rgb(220, 161, 1);")

        self.horizontalLayout_83.addWidget(self.label_108)

        self.pushButton_Add_NewProvider = QPushButton(self.frame_85)
        self.pushButton_Add_NewProvider.setObjectName(u"pushButton_Add_NewProvider")
        self.pushButton_Add_NewProvider.setEnabled(True)
        self.pushButton_Add_NewProvider.setMinimumSize(QSize(0, 20))
        self.pushButton_Add_NewProvider.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_83.addWidget(self.pushButton_Add_NewProvider)


        self.verticalLayout_32.addWidget(self.frame_85)

        self.frame_89 = QFrame(self.frame_121)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.tableWidget_Provider_Options = QTableWidget(self.frame_89)
        if (self.tableWidget_Provider_Options.columnCount() < 6):
            self.tableWidget_Provider_Options.setColumnCount(6)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setHorizontalHeaderItem(0, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setHorizontalHeaderItem(1, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setHorizontalHeaderItem(2, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setHorizontalHeaderItem(3, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setHorizontalHeaderItem(4, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setHorizontalHeaderItem(5, __qtablewidgetitem154)
        if (self.tableWidget_Provider_Options.rowCount() < 16):
            self.tableWidget_Provider_Options.setRowCount(16)
        __qtablewidgetitem155 = QTableWidgetItem()
        __qtablewidgetitem155.setFont(font3);
        self.tableWidget_Provider_Options.setVerticalHeaderItem(0, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(1, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(2, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(3, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(4, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(5, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(6, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(7, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(8, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(9, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(10, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(11, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(12, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(13, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(14, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        self.tableWidget_Provider_Options.setVerticalHeaderItem(15, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        __qtablewidgetitem171.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem171.setFont(font4);
        self.tableWidget_Provider_Options.setItem(0, 0, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        __qtablewidgetitem172.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem172.setFont(font4);
        self.tableWidget_Provider_Options.setItem(0, 1, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        __qtablewidgetitem173.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem173.setFont(font4);
        self.tableWidget_Provider_Options.setItem(0, 2, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        __qtablewidgetitem174.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem174.setFont(font4);
        self.tableWidget_Provider_Options.setItem(0, 3, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        __qtablewidgetitem175.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem175.setFont(font4);
        self.tableWidget_Provider_Options.setItem(0, 4, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        __qtablewidgetitem176.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem176.setFont(font4);
        self.tableWidget_Provider_Options.setItem(0, 5, __qtablewidgetitem176)
        self.tableWidget_Provider_Options.setObjectName(u"tableWidget_Provider_Options")
        sizePolicy.setHeightForWidth(self.tableWidget_Provider_Options.sizePolicy().hasHeightForWidth())
        self.tableWidget_Provider_Options.setSizePolicy(sizePolicy)
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush29 = QBrush(QColor(210, 210, 210, 128))
        brush29.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush29)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush30 = QBrush(QColor(210, 210, 210, 128))
        brush30.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush30)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush31 = QBrush(QColor(210, 210, 210, 128))
        brush31.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush31)
#endif
        self.tableWidget_Provider_Options.setPalette(palette5)
        self.tableWidget_Provider_Options.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget_Provider_Options.setFrameShape(QFrame.NoFrame)
        self.tableWidget_Provider_Options.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_Provider_Options.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_Provider_Options.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_Provider_Options.setAlternatingRowColors(False)
        self.tableWidget_Provider_Options.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_Provider_Options.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_Provider_Options.setShowGrid(True)
        self.tableWidget_Provider_Options.setGridStyle(Qt.SolidLine)
        self.tableWidget_Provider_Options.setSortingEnabled(False)
        self.tableWidget_Provider_Options.horizontalHeader().setVisible(False)
        self.tableWidget_Provider_Options.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Provider_Options.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_Provider_Options.horizontalHeader().setHighlightSections(False)
        self.tableWidget_Provider_Options.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_Provider_Options.verticalHeader().setVisible(False)
        self.tableWidget_Provider_Options.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Provider_Options.verticalHeader().setHighlightSections(False)
        self.tableWidget_Provider_Options.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_54.addWidget(self.tableWidget_Provider_Options)


        self.verticalLayout_32.addWidget(self.frame_89)


        self.horizontalLayout_82.addWidget(self.frame_121)


        self.verticalLayout_24.addWidget(self.frame_84)

        self.frame_show_PrivKey = QFrame(self.page_settings)
        self.frame_show_PrivKey.setObjectName(u"frame_show_PrivKey")
        self.frame_show_PrivKey.setMinimumSize(QSize(0, 30))
        self.frame_show_PrivKey.setMaximumSize(QSize(16777215, 40))
        self.frame_show_PrivKey.setFrameShape(QFrame.StyledPanel)
        self.frame_show_PrivKey.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_show_PrivKey)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(-1, 0, -1, 0)
        self.lineEdit_Secret_Key = QLineEdit(self.frame_show_PrivKey)
        self.lineEdit_Secret_Key.setObjectName(u"lineEdit_Secret_Key")
        self.lineEdit_Secret_Key.setMinimumSize(QSize(0, 35))
        self.lineEdit_Secret_Key.setMaximumSize(QSize(600, 16777215))
        self.lineEdit_Secret_Key.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_Secret_Key.setStyleSheet(u"QLineEdit {\n"
"	font: bold;\n"
"	font-size: 20px;\n"
"	border-radius: 15px;\n"
"	color: rgb(255, 8, 0);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QLineEdit:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QLineEdit:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.lineEdit_Secret_Key.setAlignment(Qt.AlignCenter)
        self.lineEdit_Secret_Key.setDragEnabled(True)
        self.lineEdit_Secret_Key.setReadOnly(True)
        self.lineEdit_Secret_Key.setClearButtonEnabled(False)

        self.horizontalLayout_95.addWidget(self.lineEdit_Secret_Key)

        self.frame_182 = QFrame(self.frame_show_PrivKey)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setMinimumSize(QSize(0, 40))
        self.frame_182.setFrameShape(QFrame.StyledPanel)
        self.frame_182.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_182)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(-1, 0, -1, 0)
        self.pushButton_copy_PrivateKey = QPushButton(self.frame_182)
        self.pushButton_copy_PrivateKey.setObjectName(u"pushButton_copy_PrivateKey")
        self.pushButton_copy_PrivateKey.setEnabled(True)
        self.pushButton_copy_PrivateKey.setMinimumSize(QSize(0, 35))
        self.pushButton_copy_PrivateKey.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_94.addWidget(self.pushButton_copy_PrivateKey)

        self.pushButton_Hide_PrivKeyframe = QPushButton(self.frame_182)
        self.pushButton_Hide_PrivKeyframe.setObjectName(u"pushButton_Hide_PrivKeyframe")
        self.pushButton_Hide_PrivKeyframe.setEnabled(True)
        self.pushButton_Hide_PrivKeyframe.setMinimumSize(QSize(0, 35))
        self.pushButton_Hide_PrivKeyframe.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 16px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_94.addWidget(self.pushButton_Hide_PrivKeyframe)


        self.horizontalLayout_95.addWidget(self.frame_182)


        self.verticalLayout_24.addWidget(self.frame_show_PrivKey)

        self.frame_86 = QFrame(self.page_settings)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMaximumSize(QSize(16777215, 100))
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_88 = QFrame(self.frame_86)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.pushButton_Export_Private_Key = QPushButton(self.frame_88)
        self.pushButton_Export_Private_Key.setObjectName(u"pushButton_Export_Private_Key")
        self.pushButton_Export_Private_Key.setEnabled(True)
        self.pushButton_Export_Private_Key.setMinimumSize(QSize(0, 80))
        self.pushButton_Export_Private_Key.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_47.addWidget(self.pushButton_Export_Private_Key)

        self.pushButton_EnableDisableTokens = QPushButton(self.frame_88)
        self.pushButton_EnableDisableTokens.setObjectName(u"pushButton_EnableDisableTokens")
        self.pushButton_EnableDisableTokens.setMinimumSize(QSize(0, 80))
        self.pushButton_EnableDisableTokens.setStyleSheet(u"QPushButton {\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: rgb(220, 161, 1);\n"
"	border-radius: 15px;\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 6px solid rgb(33, 37, 43);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(39, 44, 54);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_47.addWidget(self.pushButton_EnableDisableTokens)


        self.horizontalLayout_46.addWidget(self.frame_88)


        self.verticalLayout_24.addWidget(self.frame_86)

        self.stackedWidget.addWidget(self.page_settings)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setMaximumSize(QSize(190, 16777215))
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_Connected = QLabel(self.frame_label_bottom)
        self.label_Connected.setObjectName(u"label_Connected")

        self.horizontalLayout_7.addWidget(self.label_Connected)

        self.label_16 = QLabel(self.frame_label_bottom)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_7.addWidget(self.label_16)

        self.label_15 = QLabel(self.frame_label_bottom)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_15)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font3)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_57.setBuddy(self.comboBox_swap_from_ASSET)
        self.label_58.setBuddy(self.lineEdit_Swap_from_AssetBalance)
        self.label_56.setBuddy(self.lineEdit_Swap_from_Amount)
        self.label_59.setBuddy(self.lineEdit_Swap_from_Amount)
        self.label_40.setBuddy(self.output_BNBPrice)
        self.label_39.setBuddy(self.output_TIGSPRICE)
        self.label_75.setBuddy(self.output_TIGSPRICE)
        self.label_37.setBuddy(self.output_BNBBalance)
        self.label_28.setBuddy(self.output_Tigs_balance)
        self.label_44.setBuddy(self.output_BNBBalance)
        self.label_117.setBuddy(self.comboBox_select_swap)
        self.label_26.setBuddy(self.comboBox_select_swap)
        self.label_9.setBuddy(self.comboBox_swap_from_ASSET)
        self.label_38.setBuddy(self.lineEdit_Swap_from_Amount)
        self.label_2.setBuddy(self.lineEdit_Swap_from_AssetBalance)
        self.label_41.setBuddy(self.lineEdit_Swap_to_Amount)
        self.label_27.setBuddy(self.lineEdit_Swap_from_AssetBalance)
        self.label_23.setBuddy(self.comboBox_swap_to_ASSET)
        self.label_96.setBuddy(self.comboBox_swap_to_ASSET)
        self.label_93.setBuddy(self.comboBox_swap_to_ASSET)
        self.label_94.setBuddy(self.comboBox_swap_to_ASSET)
        self.label_95.setBuddy(self.comboBox_swap_to_ASSET)
        self.label_90.setBuddy(self.comboBox_swap_to_ASSET)
        self.label_91.setBuddy(self.comboBox_swap_to_ASSET)
        self.label_92.setBuddy(self.comboBox_swap_to_ASSET)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.btn_minimize, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)
        self.pushButton_Unlock_Wallet.setDefault(True)
        self.stackedWidget_limitOrders.setCurrentIndex(1)
        self.stackedWidget_158.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_12.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_clean.setText("")
        self.label_TIGS_balanceAlivibe.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\"/></p></body></html>", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| UNLOCK WALLET", None))
        self.pushButton_LoggoutEverywere.setText(QCoreApplication.translate("MainWindow", u"LogOut", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Binance smart chain DeFi &amp; Swap Wallet</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">Select your Wallet</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.comboBox_Accounts.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Select your Account!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.comboBox_Accounts.setCurrentText("")
        self.pushButton_Create_Wallet.setText(QCoreApplication.translate("MainWindow", u"Create Wallet", None))
        self.pushButton_Import_Wallet.setText(QCoreApplication.translate("MainWindow", u"Import Wallet", None))
        self.input_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_wrong_password.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#dba006;\">Wrong password!</span></p></body></html>", None))
        self.pushButton_Unlock_Wallet.setText(QCoreApplication.translate("MainWindow", u"Unlock Wallet", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Send BNB or BEP20 Tokens</span></p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Send</span></p></body></html>", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:17pt;\">Balance</span></p></body></html>", None))
        self.lineEdit_SendAsset_Balance.setText(QCoreApplication.translate("MainWindow", u"0.000000000", None))
        self.label_60.setText("")
        self.lineEdit_SendBalanceUSD.setText(QCoreApplication.translate("MainWindow", u"0.0 $", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">Amount</span></p></body></html>", None))
        self.lineEdit_SendAmount.setText("")
        self.lineEdit_SendAmount.setPlaceholderText("")
        self.label_55.setText("")
        self.lineEdit_SendAmountUSD.setText(QCoreApplication.translate("MainWindow", u"0.0 $", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">\n"
"Receiver address</span></p></body></html>", None))
        self.lineEdit_send_receiver.setText("")
        self.lineEdit_Send_InfoField.setText(QCoreApplication.translate("MainWindow", u"hi", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Gas Gwei</span></p></body></html>", None))
        self.lineEdit_gasSendGwei.setText(QCoreApplication.translate("MainWindow", u"6 Gwei", None))
        self.btn_Send_BNBTOKEN.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Confirm Sending</p></body></html>", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_send_TokenName.setText(QCoreApplication.translate("MainWindow", u"TokenName", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.output_send_TokenAmount.setText(QCoreApplication.translate("MainWindow", u"0.00000000000000", None))
        self.output_send_TokenAmount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_81.setText("")
        self.output_send_TokenUSD_2.setText(QCoreApplication.translate("MainWindow", u"0.00  $", None))
        self.output_send_TokenUSD_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_TokenAmountInUsdt.setText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.output_send_rece.setText(QCoreApplication.translate("MainWindow", u"0x0000000000000000000000000000000000000000", None))
        self.output_send_rece.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_send_Receiver.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Gas", None))
        self.output_send_TokenGasBNB.setText(QCoreApplication.translate("MainWindow", u"0.0000000000", None))
        self.output_send_TokenGasBNB.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_send_TokenName_2.setText(QCoreApplication.translate("MainWindow", u"BNB", None))
        self.label_82.setText("")
        self.label_send_Gas_2.setText("")
        self.output_send_FeeUSD.setText(QCoreApplication.translate("MainWindow", u"0.00  $", None))
        self.output_send_FeeUSD.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_send_Gas.setText("")
        self.pushButton_TXCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_SendConfirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Waiting for confirmation</p></body></html>", None))
        self.label_Waiting_Confirm.setText("")
        self.pushButton_TxBscView.setText(QCoreApplication.translate("MainWindow", u"View BscScan", None))
        self.lineEdit_Info_Confirmation.setText(QCoreApplication.translate("MainWindow", u"Waiting...", None))
        self.lineEdit_Info_Confirmation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Waiting...", None))
        self.pushButton_back_To_Main.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Add Token</span></p><p><br/></p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.pushButton_back_Alltokens.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.input_add_TokenAddresse.setText("")
        self.input_add_TokenAddresse.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Token Address", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Input Token Address:</p></body></html>", None))
        self.input_add_TokenName.setText("")
        self.input_add_TokenName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Token Name", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Token Name:</p></body></html>", None))
        self.input_add_TokenSymbol.setText("")
        self.input_add_TokenSymbol.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Token Symbol", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Token Symbol:</p></body></html>", None))
        self.input_add_TokenDecimals.setText("")
        self.input_add_TokenDecimals.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Token Decimals", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Token Decimals:</p></body></html>", None))
        self.input_add_Token_IMGURL.setText("")
        self.input_add_Token_IMGURL.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Token IMG URL", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>(Optional) Token IMG URL:</p></body></html>", None))
        self.pushButton_save_token.setText(QCoreApplication.translate("MainWindow", u"Save Token", None))
        self.label_add_Token_Error.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:400;\">TextLabel</span></p></body></html>", None))
        self.label_67.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#dba006;\">Binance Coin Price :</span></p><p><span style=\" font-size:16pt;\"><br/></span></p></body></html>", None))
        self.output_BNBPrice.setText(QCoreApplication.translate("MainWindow", u"0.00  $", None))
        self.output_BNBPrice.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_68.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#dba006;\">Trading Tigers Price :</span></p><p><br/></p></body></html>", None))
        self.output_TIGSPRICE.setText(QCoreApplication.translate("MainWindow", u"0.00  $", None))
        self.output_TIGSPRICE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Your BSC Address:</span></p></body></html>", None))
        self.pushButton_copy_self_address.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.output_self_address.setText(QCoreApplication.translate("MainWindow", u"address", None))
        self.output_self_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"address", None))
        self.label_qrCode_self_address.setText("")
        self.label_32.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; color:#dba006;\">Binance Coin Balance:</span></p></body></html>", None))
        self.output_BNBBalance.setText(QCoreApplication.translate("MainWindow", u"0.0000000000 BNB", None))
        self.output_BNBBalance.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_51.setText("")
        self.output_BNBBalance_in_usd.setText(QCoreApplication.translate("MainWindow", u"0.00  $", None))
        self.output_BNBBalance_in_usd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_13.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Wallet overview</span></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_11.setText("")
        self.pushButton_TokenSite.setText(QCoreApplication.translate("MainWindow", u"Token Overview", None))
        self.label_31.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; color:#dba006;\">TIGS Token Balance:</span></p></body></html>", None))
        self.output_Tigs_balance.setText(QCoreApplication.translate("MainWindow", u"0.0000000000 TIGS", None))
        self.output_Tigs_balance.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_52.setText("")
        self.output_TigsBalance_in_usd.setText(QCoreApplication.translate("MainWindow", u"0.00 $", None))
        self.output_TigsBalance_in_usd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_30.setText("")
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">BEP20 Token balance overview</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; color:#dba006;\">Total balance:</span></p></body></html>", None))
        self.output_TotalTokenBalanceInUsd.setText(QCoreApplication.translate("MainWindow", u"0.00  $", None))
        self.output_TotalTokenBalanceInUsd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.pushButton_refresh_3.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        ___qtablewidgetitem = self.tableWidget_AllActivTokens.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget_AllActivTokens.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget_AllActivTokens.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Neue Spalte", None));
        ___qtablewidgetitem3 = self.tableWidget_AllActivTokens.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"2.1", None));
        ___qtablewidgetitem4 = self.tableWidget_AllActivTokens.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem5 = self.tableWidget_AllActivTokens.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem6 = self.tableWidget_AllActivTokens.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget_AllActivTokens.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget_AllActivTokens.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget_AllActivTokens.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget_AllActivTokens.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget_AllActivTokens.verticalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget_AllActivTokens.verticalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget_AllActivTokens.verticalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget_AllActivTokens.verticalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget_AllActivTokens.verticalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget_AllActivTokens.verticalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget_AllActivTokens.verticalHeaderItem(11)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget_AllActivTokens.verticalHeaderItem(12)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget_AllActivTokens.verticalHeaderItem(13)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.tableWidget_AllActivTokens.verticalHeaderItem(14)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.tableWidget_AllActivTokens.verticalHeaderItem(15)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget_AllActivTokens.isSortingEnabled()
        self.tableWidget_AllActivTokens.setSortingEnabled(False)
        ___qtablewidgetitem22 = self.tableWidget_AllActivTokens.item(0, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"IMG", None));
        ___qtablewidgetitem23 = self.tableWidget_AllActivTokens.item(0, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Symbol", None));
        ___qtablewidgetitem24 = self.tableWidget_AllActivTokens.item(0, 2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem25 = self.tableWidget_AllActivTokens.item(0, 3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"USD Price", None));
        ___qtablewidgetitem26 = self.tableWidget_AllActivTokens.item(0, 4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Balance", None));
        ___qtablewidgetitem27 = self.tableWidget_AllActivTokens.item(0, 5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Balance in USD", None));
        self.tableWidget_AllActivTokens.setSortingEnabled(__sortingEnabled)

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Create New Wallet</span></p></body></html>", None))
        self.input_create_walletpw.setText("")
        self.input_create_walletpw.setPlaceholderText(QCoreApplication.translate("MainWindow", u"set Wallet Password", None))
        self.input_create_walletname.setText("")
        self.input_create_walletname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Wallet Name</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Wallet Password</span></p></body></html>", None))
        self.pushButton_create_wallet.setText(QCoreApplication.translate("MainWindow", u"Create Wallet", None))
        self.pushButton_back_Login.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_Save_Your_Secret_Key.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:17pt; color:#dba006;\">Save Your Secret Key! Its needed to restore your wallet!</span></p></body></html>", None))
        self.textBrowser_skey.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Secret key", None))
        self.pushButton_Copy_SKEY.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Tokens</span></p></body></html>", None))
        ___qtablewidgetitem28 = self.tableWidget_AllTokensinDB.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem29 = self.tableWidget_AllTokensinDB.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem30 = self.tableWidget_AllTokensinDB.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem31 = self.tableWidget_AllTokensinDB.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem32 = self.tableWidget_AllTokensinDB.horizontalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem33 = self.tableWidget_AllTokensinDB.verticalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.tableWidget_AllTokensinDB.verticalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.tableWidget_AllTokensinDB.isSortingEnabled()
        self.tableWidget_AllTokensinDB.setSortingEnabled(False)
        ___qtablewidgetitem35 = self.tableWidget_AllTokensinDB.item(0, 0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"IMG", None));
        ___qtablewidgetitem36 = self.tableWidget_AllTokensinDB.item(0, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Symbol", None));
        ___qtablewidgetitem37 = self.tableWidget_AllTokensinDB.item(0, 2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem38 = self.tableWidget_AllTokensinDB.item(0, 3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Activ", None));
        ___qtablewidgetitem39 = self.tableWidget_AllTokensinDB.item(0, 4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Remove", None));
        self.tableWidget_AllTokensinDB.setSortingEnabled(__sortingEnabled1)

        self.pushButton_back_wallet.setText("")
        self.pushButton_toAddTokenOverview.setText(QCoreApplication.translate("MainWindow", u"Add Token", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">add Token</span></p></body></html>", None))
        self.pushButton_back_To.setText(QCoreApplication.translate("MainWindow", u"Add Token", None))
        self.pushButton_back_Login_3.setText("")
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Limit Orders</span></p></body></html>", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Swap</span></p></body></html>", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:17pt;\">Gas</span></p></body></html>", None))
        self.output_GasGwei_limit.setText(QCoreApplication.translate("MainWindow", u"6 Gwei", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Slippage", None))
        self.output_Slippage_limit.setText(QCoreApplication.translate("MainWindow", u"3 %", None))
        self.pushButton__limit_approve_token.setText(QCoreApplication.translate("MainWindow", u"Approve", None))
        self.pushButton__limit_approve_tigs_toRouter.setText(QCoreApplication.translate("MainWindow", u"Approve TIGS", None))
        self.pushButton_Confirm_LimitOrder.setText(QCoreApplication.translate("MainWindow", u"Create\n"
"LimitOrder", None))
        self.pushButton_limit_BuyOrder.setText(QCoreApplication.translate("MainWindow", u"Limit Buy", None))
        self.pushButton_limit_SellOrder.setText(QCoreApplication.translate("MainWindow", u"Limit Sell", None))
        self.pushButton__limitBuy_UseBUSD.setText(QCoreApplication.translate("MainWindow", u"BUSD", None))
        self.pushButton__limitBuy_UseBNB.setText(QCoreApplication.translate("MainWindow", u"BNB", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#dca101;\">Amount</span></p></body></html>", None))
        self.lineEdit_limit_BuyFrom_Amount.setText("")
        self.lineEdit_limit_BuyFrom_Amount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">to</span></p></body></html>", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">MinOutput</span></p></body></html>", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#dca101;\">Target Output</span></p></body></html>", None))
        self.lineEdit_limit_BuyTo_Amount.setText("")
        self.lineEdit_limit_BuyTo_Amount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton__limitBuy_UseBUSD_3.setText(QCoreApplication.translate("MainWindow", u"BUSD", None))
        self.pushButton__limitBuy_UseBNB_4.setText(QCoreApplication.translate("MainWindow", u"BNB", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#dca101;\">Target OutPut</span></p></body></html>", None))
        self.lineEdit_limit_to_Amount.setText("")
        self.lineEdit_limit_to_Amount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#dca101;\">Input Amounts</span></p></body></html>", None))
        self.lineEdit_limit_BuyTo_Amount_3.setText("")
        self.lineEdit_limit_BuyTo_Amount_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.lineEdit_limit_BuyTo_Amount_4.setText("")
        self.lineEdit_limit_BuyTo_Amount_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton__limitBuy_UseBNB_2.setText(QCoreApplication.translate("MainWindow", u"Open Limit Orders", None))
        ___qtablewidgetitem40 = self.tableWidget_OpenLimitOrders.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem41 = self.tableWidget_OpenLimitOrders.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem42 = self.tableWidget_OpenLimitOrders.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem43 = self.tableWidget_OpenLimitOrders.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem44 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem45 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem46 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem47 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem48 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(4)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem49 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(5)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem50 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(6)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem51 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(7)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem52 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(8)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem53 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(9)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem54 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(10)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem55 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(11)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem56 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(12)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem57 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(13)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem58 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(14)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem59 = self.tableWidget_OpenLimitOrders.verticalHeaderItem(15)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.tableWidget_OpenLimitOrders.isSortingEnabled()
        self.tableWidget_OpenLimitOrders.setSortingEnabled(False)
        ___qtablewidgetitem60 = self.tableWidget_OpenLimitOrders.item(0, 0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Target Output", None));
        ___qtablewidgetitem61 = self.tableWidget_OpenLimitOrders.item(0, 1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Input Amount", None));
        ___qtablewidgetitem62 = self.tableWidget_OpenLimitOrders.item(0, 2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Current Output", None));
        ___qtablewidgetitem63 = self.tableWidget_OpenLimitOrders.item(0, 3)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Price Impact", None));
        self.tableWidget_OpenLimitOrders.setSortingEnabled(__sortingEnabled2)

        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Swapping</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Swap</span></p></body></html>", None))
        self.lineEdit_Swap_from_BalanceInUSD.setText(QCoreApplication.translate("MainWindow", u"0.0 $", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">Pay</span></p></body></html>", None))
        self.lineEdit_Swap_from_AssetBalance.setText(QCoreApplication.translate("MainWindow", u"0.00000", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">Amount</span></p></body></html>", None))
        self.lineEdit_Swap_from_Amount.setText("")
        self.label_46.setText("")
        self.lineEdit_Swap_from_AmountInUSD.setText(QCoreApplication.translate("MainWindow", u"0.0 $", None))
        self.label_87.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:17pt;\">Balance:</span></p></body></html>", None))
        self.lineEdit_Swap_to_BalanceInUSD.setText(QCoreApplication.translate("MainWindow", u"0.0 $", None))
        self.label_86.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">Amount</span></p></body></html>", None))
        self.label_48.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:17pt;\">Balance:</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">Receive</span></p></body></html>", None))
        self.lineEdit_Swap_to_AssetBalance.setText(QCoreApplication.translate("MainWindow", u"0.00000", None))
        self.lineEdit_Swap_to_AmountInUSD.setText(QCoreApplication.translate("MainWindow", u"0.00 $", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Swap Way:</span></p></body></html>", None))
        self.label_SwapWayA.setText("")
        self.label_SwapWayB.setText("")
        self.label_SwapWayC.setText("")
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Input Token Infos:</span></p></body></html>", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Buy Tax:</span></p></body></html>", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Sell Tax:</span></p></body></html>", None))
        self.lineEdit_InputToken_BuyTax.setText(QCoreApplication.translate("MainWindow", u"0 %", None))
        self.lineEdit_InputToken_SellTax.setText(QCoreApplication.translate("MainWindow", u"0 %", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Output Token Infos:</span></p></body></html>", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Buy Tax:</span></p></body></html>", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Sell Tax:</span></p></body></html>", None))
        self.lineEdit_OutputToken_BuyTax.setText(QCoreApplication.translate("MainWindow", u"0 %", None))
        self.lineEdit_OutputToken_SellTax.setText(QCoreApplication.translate("MainWindow", u"0 %", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:17pt;\">Gas</span></p></body></html>", None))
        self.output_GasGwei_Swap.setText(QCoreApplication.translate("MainWindow", u"6 Gwei", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Slippage", None))
        self.output_Slippage_Swap.setText(QCoreApplication.translate("MainWindow", u"3 %", None))
        self.pushButton_approve_token.setText(QCoreApplication.translate("MainWindow", u"Approve", None))
        self.pushButton_Confirm_Swap.setText(QCoreApplication.translate("MainWindow", u"Swap", None))
        self.pushButton_Swap_changeInputTokenToOutputToken.setText("")
        self.lineEdit_Swap_Error.setText(QCoreApplication.translate("MainWindow", u"dasfds", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Confirm Swap</p></body></html>", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Swap", None))
        self.label_swap_inputToken.setText(QCoreApplication.translate("MainWindow", u"TokenName", None))
        self.label_swap_outputToken.setText(QCoreApplication.translate("MainWindow", u"TokenName", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Way", None))
        self.label_SwapWayA_confirm.setText("")
        self.label_SwapWayB_confirm.setText("")
        self.label_SwapWayC_confirm.setText("")
        self.label_SwapWayD_confirm.setText("")
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.output_swapspendAmount.setText(QCoreApplication.translate("MainWindow", u"0.00000000000000", None))
        self.output_swapspendAmount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_98.setText("")
        self.output_swapspendAmountUSD.setText(QCoreApplication.translate("MainWindow", u"0.00  $", None))
        self.output_swapspendAmountUSD.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_TokenAmountInUsdt_2.setText("")
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Amount Min received", None))
        self.output_swapminreceivedAmount.setText(QCoreApplication.translate("MainWindow", u"0.00000000000000", None))
        self.output_swapminreceivedAmount.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_104.setText("")
        self.output_swapminreceivedAmountUSD.setText(QCoreApplication.translate("MainWindow", u"0.00  $", None))
        self.output_swapminreceivedAmountUSD.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Gas", None))
        self.output_swap_GasBNB.setText(QCoreApplication.translate("MainWindow", u"0.0000000000", None))
        self.output_swap_GasBNB.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_send_TokenName_4.setText(QCoreApplication.translate("MainWindow", u"BNB", None))
        self.label_101.setText("")
        self.label_send_Gas_3.setText("")
        self.output_swap_GasUSD.setText(QCoreApplication.translate("MainWindow", u"0.00  $", None))
        self.output_swap_GasUSD.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_send_Gas_4.setText("")
        self.pushButton_Cancel_SwapConfirm.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_SwapConfirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Confirm Approve</p></body></html>", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Approve", None))
        self.label_approve_TokenName.setText(QCoreApplication.translate("MainWindow", u"TokenName", None))
        self.label_approv_tokenLogo.setText("")
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.output_approve_Address.setText(QCoreApplication.translate("MainWindow", u"0x0000000000000000000000000000000000000000", None))
        self.output_approve_Address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_send_Receiver_2.setText("")
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Gas", None))
        self.output_approve_GasBNB.setText(QCoreApplication.translate("MainWindow", u"0.0000000000", None))
        self.output_approve_GasBNB.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_send_TokenName_5.setText(QCoreApplication.translate("MainWindow", u"BNB", None))
        self.label_112.setText("")
        self.label_send_Gas_5.setText("")
        self.output_approve_FeeUSD.setText(QCoreApplication.translate("MainWindow", u"0.00  $", None))
        self.output_approve_FeeUSD.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wallet Name", None))
        self.label_send_Gas_6.setText("")
        self.pushButton_approve_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_approve_Confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.pushButton_import_wallet.setText(QCoreApplication.translate("MainWindow", u"Import Wallet", None))
        self.pushButton_back_Login_2.setText("")
        self.input_import_walletname.setText("")
        self.input_import_walletname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Set your Wallet Name", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Wallet Password</span></p></body></html>", None))
        self.input_import_walletpw.setText("")
        self.input_import_walletpw.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Set a Strong Password", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Wallet Name</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt;\">Private key</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Import Wallet</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:15pt; color:#dba006;\">Imported address:</span></p></body></html>", None))
        self.textBrowser_imported_address.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:18px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:18px; color:#ffffff;\">0x0...</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.label_25.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Successfully imported!</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span >Successfully imported!</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dba006;\">Invalid Secret Key!</span></p></body></html>", None))
        self.input_import_key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input Privat Key or Secret Key", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Transaction History</span></p></body></html>", None))
        ___qtablewidgetitem64 = self.tableWidget_transactions.horizontalHeaderItem(0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem65 = self.tableWidget_transactions.horizontalHeaderItem(1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem66 = self.tableWidget_transactions.horizontalHeaderItem(2)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem67 = self.tableWidget_transactions.horizontalHeaderItem(3)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem68 = self.tableWidget_transactions.horizontalHeaderItem(4)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem69 = self.tableWidget_transactions.horizontalHeaderItem(5)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem70 = self.tableWidget_transactions.horizontalHeaderItem(6)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Neue Spalte", None));
        ___qtablewidgetitem71 = self.tableWidget_transactions.verticalHeaderItem(0)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem72 = self.tableWidget_transactions.verticalHeaderItem(1)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem73 = self.tableWidget_transactions.verticalHeaderItem(2)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem74 = self.tableWidget_transactions.verticalHeaderItem(3)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem75 = self.tableWidget_transactions.verticalHeaderItem(4)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem76 = self.tableWidget_transactions.verticalHeaderItem(5)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem77 = self.tableWidget_transactions.verticalHeaderItem(6)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem78 = self.tableWidget_transactions.verticalHeaderItem(7)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem79 = self.tableWidget_transactions.verticalHeaderItem(8)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem80 = self.tableWidget_transactions.verticalHeaderItem(9)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem81 = self.tableWidget_transactions.verticalHeaderItem(10)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem82 = self.tableWidget_transactions.verticalHeaderItem(11)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem83 = self.tableWidget_transactions.verticalHeaderItem(12)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem84 = self.tableWidget_transactions.verticalHeaderItem(13)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem85 = self.tableWidget_transactions.verticalHeaderItem(14)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem86 = self.tableWidget_transactions.verticalHeaderItem(15)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled3 = self.tableWidget_transactions.isSortingEnabled()
        self.tableWidget_transactions.setSortingEnabled(False)
        ___qtablewidgetitem87 = self.tableWidget_transactions.item(0, 0)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"TimeStamp", None));
        ___qtablewidgetitem88 = self.tableWidget_transactions.item(0, 1)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Confirms", None));
        ___qtablewidgetitem89 = self.tableWidget_transactions.item(0, 2)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Block", None));
        ___qtablewidgetitem90 = self.tableWidget_transactions.item(0, 3)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem91 = self.tableWidget_transactions.item(0, 4)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Fee", None));
        ___qtablewidgetitem92 = self.tableWidget_transactions.item(0, 5)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"TX", None));
        ___qtablewidgetitem93 = self.tableWidget_transactions.item(0, 6)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"BscScan.com", None));
        self.tableWidget_transactions.setSortingEnabled(__sortingEnabled3)

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Settings</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Add New Provider</span></p></body></html>", None))
        self.pushButton_add_ProviderSubmit.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">Name</span></p></body></html>", None))
        self.input_add_ProviderName.setText("")
        self.input_add_ProviderName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.input_add_ProviderURL.setText("")
        self.input_add_ProviderURL.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HTTPS:// or WSS://", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">URL</span></p></body></html>", None))
        self.pushButton_add_ProviderCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.lineEdit_add_provider_Error.setText(QCoreApplication.translate("MainWindow", u"hi", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Provider Options</span></p></body></html>", None))
        self.pushButton_Add_NewProvider.setText(QCoreApplication.translate("MainWindow", u"Add Provider", None))
        ___qtablewidgetitem94 = self.tableWidget_Provider_Options.horizontalHeaderItem(0)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem95 = self.tableWidget_Provider_Options.horizontalHeaderItem(1)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem96 = self.tableWidget_Provider_Options.horizontalHeaderItem(2)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem97 = self.tableWidget_Provider_Options.horizontalHeaderItem(3)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem98 = self.tableWidget_Provider_Options.horizontalHeaderItem(4)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem99 = self.tableWidget_Provider_Options.horizontalHeaderItem(5)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem100 = self.tableWidget_Provider_Options.verticalHeaderItem(0)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem101 = self.tableWidget_Provider_Options.verticalHeaderItem(1)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem102 = self.tableWidget_Provider_Options.verticalHeaderItem(2)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem103 = self.tableWidget_Provider_Options.verticalHeaderItem(3)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem104 = self.tableWidget_Provider_Options.verticalHeaderItem(4)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem105 = self.tableWidget_Provider_Options.verticalHeaderItem(5)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem106 = self.tableWidget_Provider_Options.verticalHeaderItem(6)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem107 = self.tableWidget_Provider_Options.verticalHeaderItem(7)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem108 = self.tableWidget_Provider_Options.verticalHeaderItem(8)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem109 = self.tableWidget_Provider_Options.verticalHeaderItem(9)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem110 = self.tableWidget_Provider_Options.verticalHeaderItem(10)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem111 = self.tableWidget_Provider_Options.verticalHeaderItem(11)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem112 = self.tableWidget_Provider_Options.verticalHeaderItem(12)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem113 = self.tableWidget_Provider_Options.verticalHeaderItem(13)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem114 = self.tableWidget_Provider_Options.verticalHeaderItem(14)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem115 = self.tableWidget_Provider_Options.verticalHeaderItem(15)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled4 = self.tableWidget_Provider_Options.isSortingEnabled()
        self.tableWidget_Provider_Options.setSortingEnabled(False)
        ___qtablewidgetitem116 = self.tableWidget_Provider_Options.item(0, 0)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"Use", None));
        ___qtablewidgetitem117 = self.tableWidget_Provider_Options.item(0, 1)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem118 = self.tableWidget_Provider_Options.item(0, 2)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"ProviderURL", None));
        ___qtablewidgetitem119 = self.tableWidget_Provider_Options.item(0, 3)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"BlockHigh", None));
        ___qtablewidgetitem120 = self.tableWidget_Provider_Options.item(0, 4)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"Speed", None));
        ___qtablewidgetitem121 = self.tableWidget_Provider_Options.item(0, 5)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"Delete", None));
        self.tableWidget_Provider_Options.setSortingEnabled(__sortingEnabled4)

        self.lineEdit_Secret_Key.setText(QCoreApplication.translate("MainWindow", u"hi", None))
        self.pushButton_copy_PrivateKey.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.pushButton_Hide_PrivKeyframe.setText(QCoreApplication.translate("MainWindow", u"close", None))
        self.pushButton_Export_Private_Key.setText(QCoreApplication.translate("MainWindow", u"Show Private Key", None))
        self.pushButton_EnableDisableTokens.setText(QCoreApplication.translate("MainWindow", u"Set Tokens", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Connected to Binance Smart Chain: </p></body></html>", None))
        self.label_Connected.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.label_16.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TIGS Token DeFi & Swap Wallet", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v2.0", None))
    # retranslateUi

