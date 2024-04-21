from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QIcon,
                           QPixmap)
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QPushButton, QSizePolicy,
                               QStackedWidget, QVBoxLayout, QWidget)
from imgs import Images_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(832, 511)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/Main/Auburn_logo.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"@font-face{\n"
"			font-family: NovaFlat;\n"
"			src: url(:/fonts/Nova_Flat/NovaFlat-Regular.ttf) format(\"truetype\");\n"
"}\n"
"*{\n"
"color: #fff;\n"
"font-family: NovaFlat;\n"
"font-size: 12px;\n"
"border: nine;\n"
"background: none;\n"
"}\n"
"\n"
"QWidget{\n"
"	background-color: rgb(45, 46, 76);\n"
"}\n"
"\n"
"left_menu_widget, #major_company_cloud_breaches, #us_major_cloud_breaches, \n"
"#russian_major_cloud_breaches, #china_major_cloud_breaches, #uk_major_cloud_breaches, #stackedWidget QFrame\n"
"{\n"
"background-color: rgb(50, 68, 85);\n"
"}\n"
"#frame_2, #frame_9{\n"
"	background-color: rgb(33, 35, 49);\n"
"}\n"
"\n"
"#frame_4 QPushButton{\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"background-color: rgba(33, 42, 51, 100);\n"
"}\n"
"#header_nav QPushButton{\n"
"background-color: rgb(54, 66, 147);\n"
"border-radius: 15px;\n"
"\n"
"}\n"
"#header_nav QPushButton:hover{\n"
"background-color: rgb(120, 157, 186);\n"
"}\n"
"\n"
"#left_menu_widget QPushButton:hover{\n"
"background-color:rgb(120, 157, 186);"
                        "\n"
"}\n"
"\n"
"#header_menu_nav QPushButton:hover{\n"
"background-color:rgb(120, 157, 186);\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_widget = QWidget(self.centralwidget)
        self.left_menu_widget.setObjectName(u"left_menu_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_menu_widget.sizePolicy().hasHeightForWidth())
        self.left_menu_widget.setSizePolicy(sizePolicy1)
        self.left_menu_widget.setMinimumSize(QSize(0, 0))
        self.left_menu_widget.setMaximumSize(QSize(16777215, 11677215))
        self.left_menu_widget.setStyleSheet(u"#left_menu_widget{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.left_menu_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.left_menu_widget)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(0, 52))
        self.frame_6.setMaximumSize(QSize(16777215, 41))
        self.frame_6.setStyleSheet(u"#frame_6, #label, #label_15{\n"
"background-color: rgb(54, 66, 147);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QSize(36, 36))
        self.label_15.setMaximumSize(QSize(36, 36))
        self.label_15.setPixmap(QPixmap(u":/Buttons/analysis.png"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_15)

        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.left_menu_widget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 306))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.company_cloud_breaches_button = QPushButton(self.frame_3)
        self.company_cloud_breaches_button.setObjectName(u"company_cloud_breaches_button")
        self.company_cloud_breaches_button.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.company_cloud_breaches_button.sizePolicy().hasHeightForWidth())
        self.company_cloud_breaches_button.setSizePolicy(sizePolicy2)
        self.company_cloud_breaches_button.setMaximumSize(QSize(16777215, 33))
        self.company_cloud_breaches_button.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/cloud.png", QSize(), QIcon.Normal, QIcon.Off)
        self.company_cloud_breaches_button.setIcon(icon1)
        self.company_cloud_breaches_button.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.company_cloud_breaches_button)

        self.us_cloud_breaches_button = QPushButton(self.frame_3)
        self.us_cloud_breaches_button.setObjectName(u"us_cloud_breaches_button")
        sizePolicy2.setHeightForWidth(self.us_cloud_breaches_button.sizePolicy().hasHeightForWidth())
        self.us_cloud_breaches_button.setSizePolicy(sizePolicy2)
        self.us_cloud_breaches_button.setMaximumSize(QSize(16777215, 33))
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/icons8-united-states-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.us_cloud_breaches_button.setIcon(icon2)
        self.us_cloud_breaches_button.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.us_cloud_breaches_button)

        self.russian_cloud_breaches_button = QPushButton(self.frame_3)
        self.russian_cloud_breaches_button.setObjectName(u"russian_cloud_breaches_button")
        sizePolicy2.setHeightForWidth(self.russian_cloud_breaches_button.sizePolicy().hasHeightForWidth())
        self.russian_cloud_breaches_button.setSizePolicy(sizePolicy2)
        self.russian_cloud_breaches_button.setMaximumSize(QSize(16777215, 33))
        icon3 = QIcon()
        icon3.addFile(u":/Buttons/icons8-russia-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.russian_cloud_breaches_button.setIcon(icon3)
        self.russian_cloud_breaches_button.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.russian_cloud_breaches_button)

        self.china_cloud_breaches_button = QPushButton(self.frame_3)
        self.china_cloud_breaches_button.setObjectName(u"china_cloud_breaches_button")
        sizePolicy2.setHeightForWidth(self.china_cloud_breaches_button.sizePolicy().hasHeightForWidth())
        self.china_cloud_breaches_button.setSizePolicy(sizePolicy2)
        self.china_cloud_breaches_button.setMaximumSize(QSize(16777215, 33))
        icon4 = QIcon()
        icon4.addFile(u":/Buttons/icons8-china-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.china_cloud_breaches_button.setIcon(icon4)
        self.china_cloud_breaches_button.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.china_cloud_breaches_button)

        self.uk_cloud_breaches_button = QPushButton(self.frame_3)
        self.uk_cloud_breaches_button.setObjectName(u"uk_cloud_breaches_button")
        sizePolicy2.setHeightForWidth(self.uk_cloud_breaches_button.sizePolicy().hasHeightForWidth())
        self.uk_cloud_breaches_button.setSizePolicy(sizePolicy2)
        self.uk_cloud_breaches_button.setMaximumSize(QSize(16777215, 33))
        icon5 = QIcon()
        icon5.addFile(u":/Buttons/icons8-united-kingdom-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.uk_cloud_breaches_button.setIcon(icon5)
        self.uk_cloud_breaches_button.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.uk_cloud_breaches_button)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.left_menu_widget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMaximumSize(QSize(16777215, 54))
        self.frame_4.setStyleSheet(u"#frame_4, #label_16, #label_2{\n"
"	background-color: rgb(54, 66, 147);\n"
"}\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 0, 6, 0)
        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(26, 29))
        self.label_16.setPixmap(QPixmap(u":/Buttons/python-logo-only.png"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_16)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(265, 25))

        self.horizontalLayout_8.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.left_menu_widget)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setStyleSheet(u"#frame_5, QLabel{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 4, -1, -1)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.left_menu_widget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777214))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 1, -1, -1)
        self.header_frame = QFrame(self.frame_2)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy3.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy3)
        self.header_frame.setMinimumSize(QSize(600, 0))
        self.header_frame.setMaximumSize(QSize(16777215, 232))
        self.header_frame.setStyleSheet(u"#frame_7{\n"
"background-color: rgb(54, 66, 147);\n"
"}")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.header_menu_nav = QFrame(self.header_frame)
        self.header_menu_nav.setObjectName(u"header_menu_nav")
        self.header_menu_nav.setMinimumSize(QSize(109, 0))
        self.header_menu_nav.setMaximumSize(QSize(152, 249))
        self.header_menu_nav.setStyleSheet(u"#header_menu_nav, QPushButton{\n"
"background-color: rgb(54, 66, 147);\n"
"}\n"
"\n"
"#header_menu_nav QPushButton:hover{\n"
"background-color:rgb(120, 170, 186);\n"
"}")
        self.header_menu_nav.setFrameShape(QFrame.StyledPanel)
        self.header_menu_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_menu_nav)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu_button = QPushButton(self.header_menu_nav)
        self.menu_button.setObjectName(u"menu_button")
        sizePolicy1.setHeightForWidth(self.menu_button.sizePolicy().hasHeightForWidth())
        self.menu_button.setSizePolicy(sizePolicy1)
        self.menu_button.setMaximumSize(QSize(28, 127))
        self.menu_button.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/Buttons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(icon6)
        self.menu_button.setIconSize(QSize(46, 21))

        self.horizontalLayout_4.addWidget(self.menu_button)

        self.label_7 = QLabel(self.header_menu_nav)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(96, 0))
        self.label_7.setMaximumSize(QSize(113, 16777215))
        self.label_7.setStyleSheet(u"#label_7{\n"
"background-color: rgb(54, 66, 147);\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_7)


        self.horizontalLayout_3.addWidget(self.header_menu_nav)

        self.title_bar = QFrame(self.header_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setStyleSheet(u"#title_bar{\n"
"background-color: rgb(54, 66, 147);\n"
"}")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.title_bar)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"#label_8{\n"
"background-color: rgb(54, 66, 147);\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_8)


        self.horizontalLayout_3.addWidget(self.title_bar)

        self.header_nav = QFrame(self.header_frame)
        self.header_nav.setObjectName(u"header_nav")
        sizePolicy.setHeightForWidth(self.header_nav.sizePolicy().hasHeightForWidth())
        self.header_nav.setSizePolicy(sizePolicy)
        self.header_nav.setMinimumSize(QSize(106, 0))
        self.header_nav.setMaximumSize(QSize(148, 16777215))
        self.header_nav.setStyleSheet(u"#header_nav{\n"
"background-color: rgb(54, 66, 147);\n"
"}")
        self.header_nav.setFrameShape(QFrame.StyledPanel)
        self.header_nav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.header_nav)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.minimize_window_button = QPushButton(self.header_nav)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setMinimumSize(QSize(30, 30))
        self.minimize_window_button.setMaximumSize(QSize(30, 30))
        self.minimize_window_button.setStyleSheet(u"#pushButton8{\n"
"background-color: rgb(54, 66, 147);\n"
"	border-color: rgb(97, 165, 255);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/Buttons/minus-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon7)
        self.minimize_window_button.setIconSize(QSize(23, 23))

        self.horizontalLayout_6.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.header_nav)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setMaximumSize(QSize(30, 30))
        icon8 = QIcon()
        icon8.addFile(u":/Buttons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon8)
        self.restore_window_button.setIconSize(QSize(23, 23))

        self.horizontalLayout_6.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.header_nav)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMaximumSize(QSize(30, 30))
        icon9 = QIcon()
        icon9.addFile(u":/Buttons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon9)
        self.close_window_button.setIconSize(QSize(29, 29))

        self.horizontalLayout_6.addWidget(self.close_window_button)


        self.horizontalLayout_3.addWidget(self.header_nav)


        self.verticalLayout_4.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setStyleSheet(u"#frame_8{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.major_company_cloud_breaches = QWidget()
        self.major_company_cloud_breaches.setObjectName(u"major_company_cloud_breaches")
        self.verticalLayout_6 = QVBoxLayout(self.major_company_cloud_breaches)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_16 = QFrame(self.major_company_cloud_breaches)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_10, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.major_company_cloud_breaches)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_17)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_18, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.major_company_cloud_breaches)
        self.us_major_cloud_breaches = QWidget()
        self.us_major_cloud_breaches.setObjectName(u"us_major_cloud_breaches")
        self.verticalLayout_7 = QVBoxLayout(self.us_major_cloud_breaches)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_19 = QFrame(self.us_major_cloud_breaches)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.frame_19)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_11, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.frame_19, 0, Qt.AlignTop)

        self.frame_20 = QFrame(self.us_major_cloud_breaches)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy1.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy1)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_20)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_21, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.us_major_cloud_breaches)
        self.russian_major_cloud_breaches = QWidget()
        self.russian_major_cloud_breaches.setObjectName(u"russian_major_cloud_breaches")
        self.verticalLayout_8 = QVBoxLayout(self.russian_major_cloud_breaches)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_22 = QFrame(self.russian_major_cloud_breaches)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.frame_22)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_12, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_22, 0, Qt.AlignTop)

        self.frame_23 = QFrame(self.russian_major_cloud_breaches)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy1.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy1)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_23)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_24, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_23)

        self.stackedWidget.addWidget(self.russian_major_cloud_breaches)
        self.china_major_cloud_breaches = QWidget()
        self.china_major_cloud_breaches.setObjectName(u"china_major_cloud_breaches")
        self.china_major_cloud_breaches.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.china_major_cloud_breaches)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_25 = QFrame(self.china_major_cloud_breaches)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.frame_25)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_13, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_25, 0, Qt.AlignTop)

        self.frame_26 = QFrame(self.china_major_cloud_breaches)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy1.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy1)
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_26)

        self.stackedWidget.addWidget(self.china_major_cloud_breaches)
        self.uk_major_cloud_breaches = QWidget()
        self.uk_major_cloud_breaches.setObjectName(u"uk_major_cloud_breaches")
        self.verticalLayout_10 = QVBoxLayout(self.uk_major_cloud_breaches)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_28 = QFrame(self.uk_major_cloud_breaches)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"#frame_28{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_28)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_14 = QLabel(self.frame_28)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"#label_14{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_14, 0, Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_28, 0, Qt.AlignTop)

        self.frame_27 = QFrame(self.uk_major_cloud_breaches)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy1.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy1)
        self.frame_27.setStyleSheet(u"#frame_27{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_27)

        self.stackedWidget.addWidget(self.uk_major_cloud_breaches)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 200))
        self.frame_9.setStyleSheet(u"#frame_13{\n"
"background-color: rgb(50, 68, 85);\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 9, -1, 4)
        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setStyleSheet(u"#frame_13{\n"
"	background-color: rgb(33, 35, 49);\n"
"\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)
        self.label_9.setStyleSheet(u"#label_9{\n"
"	background-color: rgb(33, 35, 49);\n"
"}")
        self.label_9.setScaledContents(False)

        self.horizontalLayout_9.addWidget(self.label_9)


        self.horizontalLayout_7.addWidget(self.frame_13)


        self.verticalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_15.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"  CHART DATA", None))
        self.company_cloud_breaches_button.setText(QCoreApplication.translate("MainWindow", u" Major Company Breaches", None))
        self.us_cloud_breaches_button.setText(QCoreApplication.translate("MainWindow", u"  U.S Cyber Crimes Data", None))
        self.russian_cloud_breaches_button.setText(QCoreApplication.translate("MainWindow", u"Russian Cyber Crimes Data", None))
        self.china_cloud_breaches_button.setText(QCoreApplication.translate("MainWindow", u"China Cyber Crimes Data", None))
        self.uk_cloud_breaches_button.setText(QCoreApplication.translate("MainWindow", u"U.K. Cyber Crimes Data", None))
        self.label_16.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"  Engineering 1100 Final Project", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Jacob Sprouse", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"James Allison", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Francis Collopy", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Huayadian Sun", None))
        self.menu_button.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Major Company Cloud Breaches", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"U.S. Major Cloud Breaches", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Russian Major Cloud Breaches", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"China Major Cloud Breaches", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"U.K. Major Cloud Breaches", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Auburn University", None))
    # retranslateUi

