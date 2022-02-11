from main import *

index = 1
class Sidebar(MainWindow):
    def slideMenu(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_left_menu.width() 
            maxExtend = maxWidth
            standard = 70
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)
 
    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(index),self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 90))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        bt_standard = (
    """
    QPushButton {
        background-image: ICON_REPLACE;
        font:bold;
        font-size:14px;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 17px solid rgb(27, 29, 35);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 60px;
    }
    QPushButton[Active=true] {
        background-image: ICON_REPLACE;
        background-position: left center;
        font:bold;
        font-size:14px;
        background-repeat: no-repeat;
        border: none;
        border-left: 17px solid rgb(27, 29, 35);
        border-right: 5px solid rgb(44, 49, 60);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 60px;
    }
    QPushButton:hover {
        background-color: rgb(33, 37, 43);
        border-left: 20px solid rgb(33, 37, 43);
    }
    QPushButton:pressed {
        background-color: rgb(85, 170, 255);
        border-left: 20px solid rgb(85, 170, 255);
    }
    """
    )
        button.setStyleSheet(bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)
        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    def clearMenu(self):
        while self.ui.layout_menus.count():
            child = self.ui.layout_menus.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        while self.ui.layout_menu_bottom.count():
            child = self.ui.layout_menu_bottom.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(44, 49, 60); }")
        return select

    def deselectMenu(getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(44, 49, 60); }", "")
        return deselect

    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(Sidebar.selectMenu(w.styleSheet()))

    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(Sidebar.deselectMenu(w.styleSheet()))


    def labelPage(self, text):
        self.ui.label_top_info_2.setText(text.upper())


    def LoadFeatures(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.close())



    #some style returns
    def getRedStyleTokenTax():
        return u"""QLineEdit {
                	font: bold;
                	font-size: 16px;
                	border-radius: 14px;
                	color:rgb(170, 0, 0);
                	border: 6px solid rgb(33, 37, 43);
                	background-position: center;
                	background-repeat: no-reperat;
                }
                QLineEdit:hover {
                	background-color: rgb(39, 44, 54);
                }
                QLineEdit:pressed {	
                	background-color: rgb(85, 170, 255);
                }"""

    def getResetStyleTokenTax():
        return u"""
        QLineEdit {
        	font: bold;
        	font-size: 16px;
        	border-radius: 14px;
        	color: rgb(220, 161, 1);
        	border: 6px solid rgb(33, 37, 43);
        	background-position: center;
        	background-repeat: no-reperat;
        }
        QLineEdit:hover {
        	background-color: rgb(39, 44, 54);
        }
        QLineEdit:pressed {	
        	background-color: rgb(85, 170, 255);
        }"""
        