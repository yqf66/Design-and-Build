# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSplitter, QVBoxLayout, QWidget)
import resources_rc

class Ui_window(object):
    def setupUi(self, window):
        if not window.objectName():  # 窗口window
            window.setObjectName(u"window")
        window.resize(1220, 725)
        self.Main_QW = QWidget(window)
        self.Main_QW.setObjectName(u"Main_QW")
        self.verticalLayout = QVBoxLayout(self.Main_QW)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Main_QF = QFrame(self.Main_QW)
        self.Main_QF.setObjectName(u"Main_QF")
        self.Main_QF.setStyleSheet(u"QFrame#Main_QF{\n"   # 这部分代码是一个样式表，用于设置名为 Main_QF 的 QFrame 部件的外观和样式。样式表的主要作用是定义如何渲染该部件，包括背景颜色、边框样式和圆角。
"	background-color: black;\n"
"border:0px solid red;\n"
"border-radius:0\n"
"}")
        self.main_qframe = QHBoxLayout(self.Main_QF)
        self.main_qframe.setSpacing(0)
        self.main_qframe.setObjectName(u"main_qframe")
        self.main_qframe.setContentsMargins(0, 0, 0, 0)
        self.RightMenuBg = QFrame(self.Main_QF)  # QFrame 部件，它将用作左侧菜单的背景。
        self.RightMenuBg.setObjectName(u"RightMenuBg")
        self.RightMenuBg.setMinimumSize(QSize(68, 0))
        self.RightMenuBg.setMaximumSize(QSize(68, 16777215))
        self.RightMenuBg.setStyleSheet(u"QFrame#RightMenuBg{\n"  # 创建了一个水平布局管理器   设置左侧菜单的背景的样式表。
"	background-color: rgba(255, 255, 255,0);\n"  #左边的边框
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.RightMenuBg.setFrameShape(QFrame.NoFrame)
        self.RightMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.RightMenuBg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.start_button = QPushButton(self.RightMenuBg)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setStyleSheet(u"QPushButton {\n"  #  左侧菜单的样式和布局
"    background-color: transparent; /* Transparent background */\n"
"    border: none; /* No border */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(200, 200, 200, 100); /* Color when the mouse hovers over the button */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 0, 0, 100); /* Color when the button is pressed */\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/all/img/begin.png", QSize(), QIcon.Normal, QIcon.Off)  # 配置了两个 QPushButton 部件的样式和图标
        self.start_button.setIcon(icon)
        self.start_button.setIconSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.start_button)

        self.files_button = QPushButton(self.RightMenuBg)
        self.files_button.setObjectName(u"files_button")
        self.files_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent; /* Transparent background */\n"
"    border: none; /* No border */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(200, 200, 200, 100); /* Color when the mouse hovers over the button */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(180, 180, 180, 100); /* Color when the button is pressed */\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/all/img/file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.files_button.setIcon(icon1)
        self.files_button.setIconSize(QSize(50, 50))  #第二个图标

        self.verticalLayout_2.addWidget(self.files_button)

        self.save_button = QPushButton(self.RightMenuBg)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent; /* Transparent background */\n"
"    border: none; /* No border */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 0, 100); /* Color when the mouse hovers over the button */\n"  # 指针移到组件上的亮度
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 0, 0, 100); /* Color when the button is pressed */\n"  # 指针移到组件上的亮度
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/all/img/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon2)
        self.save_button.setIconSize(QSize(90, 90))

        self.verticalLayout_2.addWidget(self.save_button)

#         self.undo_button = QPushButton(self.LeftMenuBg)
#         self.undo_button.setObjectName(u"undo_button")
#         self.undo_button.setStyleSheet(u"QPushButton {\n"
# "    background-color: transparent; /* Transparent background */\n"
# "    border: none; /* No border */\n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "    background-color: rgba(200, 200, 200, 100); /* Color when the mouse hovers over the button */\n"
# "}\n"
# "\n"
# "QPushButton:pressed {\n"
# "    background-color: rgba(180, 180, 180, 100); /* Color when the button is pressed */\n"
# "}")
#         icon3 = QIcon()
#         icon3.addFile(u":/all/img/delay.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.undo_button.setIcon(icon3)
#         self.undo_button.setIconSize(QSize(30, 60))
#         self.undo_button.setCheckable(True)
#
#         self.verticalLayout_2.addWidget(self.undo_button)


#        self.main_qframe.addWidget(self.RightMenuBg)   # 添加左边主界面

        self.ContentBox = QFrame(self.Main_QF)
        self.ContentBox.setObjectName(u"ContentBox")
        self.ContentBox.setMaximumSize(QSize(240, 10000))
        self.ContentBox.setMinimumSize((QSize(240, 50)))
        self.ContentBox.setStyleSheet(u"QFrame#ContentBox{\n"
"	background-color: rgb(255, 0, 0);\n"  # 大背景 
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.ContentBox.setFrameShape(QFrame.StyledPanel)
        self.ContentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.ContentBox)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.ContentBox)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 30))
        self.top.setMaximumSize(QSize(16777215, 30))
        self.top.setStyleSheet(u"QFrame#top{\n"
"background-color: rgba(255, 255, 255,0);\n"
"}")
        self.top.setFrameShape(QFrame.StyledPanel)  # top 是一个框架（QFrame），用于界面的顶部部分。
        self.top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, -1, 0)
        self.explain_title = QLabel(self.top)
        self.explain_title.setObjectName(u"explain_title")  # explain_title 是一个标签（QLabel），用于显示一些文本内容
        self.explain_title.setMinimumSize(QSize(0, 30))
        self.explain_title.setMaximumSize(QSize(16777215, 30))
        self.explain_title.setStyleSheet(u"font: 700 italic 11pt \"Segoe UI\";")
        self.explain_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.explain_title)


        self.verticalLayout_6.addWidget(self.top)

        self.content = QFrame(self.ContentBox)  # 是另一个框架，用于界面的主要内容区域。
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.content)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.main_content = QVBoxLayout()
        self.main_content.setSpacing(5)
        self.main_content.setObjectName(u"main_content")
        self.QF_Group = QFrame(self.content)
        self.QF_Group.setObjectName(u"QF_Group")

        self.QF_Group.setMinimumSize(QSize(0, 100))  # QF_Group 是内部框架，可能用于包装某些特定的界面元素或组件。
        self.QF_Group.setMaximumSize(QSize(200, 16777215))
        self.QF_Group.setStyleSheet(u"QFrame#QF_Group{\n"
"background-color: rgb(173, 216, 230);\n"  # 四个窗口的那个框
"border:2px solid rgb(255, 255, 255);\n"   # 大窗口框的边框
"border-radius:15px;\n"
"}")
        self.QF_Group.setFrameShape(QFrame.StyledPanel)
        self.QF_Group.setFrameShadow(QFrame.Raised)
        # self.horizontalLayout_3 = QHBoxLayout(self.QF_Group)
        # self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        # self.horizontalLayout_3.setContentsMargins(-1, 9, -1, 15)
        # 替换水平布局为竖直布局
        self.verticalLayout_33 = QVBoxLayout(self.QF_Group)
        self.verticalLayout_33.setObjectName(u"verticalLayout_3")

        # 设置竖直布局的内容边距
        self.verticalLayout_33.setContentsMargins(-1, 15, -1, 15)
        self.Class_QF = QFrame(self.QF_Group)
        self.Class_QF.setObjectName(u"Class_QF")
        self.Class_QF.setMinimumSize(QSize(170, 80))  # Class_QF 是另一个框架，可能是 QF_Group 中的一个子元素。它具有特定的样式设置，包括颜色、边框、背景颜色等。这些样式设置将影响 Class_QF 的外观。
        self.Class_QF.setMaximumSize(QSize(170, 80))
        self.Class_QF.setToolTipDuration(0)
        self.Class_QF.setStyleSheet(u"QFrame#Class_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));\n"
"border: 1px outset rgb(98, 91, 213);\n"
"}\n"
"")
        self.Class_QF.setFrameShape(QFrame.StyledPanel)
        self.Class_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Class_QF)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Class_top = QFrame(self.Class_QF)
        self.Class_top.setObjectName(u"Class_top")
        self.Class_top.setStyleSheet(u"border:none")
        self.Class_top.setFrameShape(QFrame.StyledPanel)
        self.Class_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Class_top)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 3, 0, 3)
        self.label_5 = QLabel(self.Class_top)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-right:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setIndent(0)

        self.horizontalLayout_6.addWidget(self.label_5)


        self.verticalLayout_7.addWidget(self.Class_top)

        self.line_2 = QFrame(self.Class_QF)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(16777215, 1))
        self.line_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.Class_bottom = QFrame(self.Class_QF)
        self.Class_bottom.setObjectName(u"Class_bottom")
        self.Class_bottom.setStyleSheet(u"border:none")
        self.Class_bottom.setFrameShape(QFrame.StyledPanel)
        self.Class_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Class_bottom)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 6, 0, 6)
        self.lineEdit = QLineEdit(self.Class_bottom)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color: transparent;")
        self.lineEdit.setMaxLength(4)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lineEdit)


        self.verticalLayout_7.addWidget(self.Class_bottom)

        self.verticalLayout_7.setStretch(1, 2)

        self.verticalLayout_33.addWidget(self.Class_QF)

        self.Target_QF = QFrame(self.QF_Group)
        self.Target_QF.setObjectName(u"Target_QF")
        self.Target_QF.setMinimumSize(QSize(170, 80))
        self.Target_QF.setMaximumSize(QSize(170, 80))
        self.Target_QF.setToolTipDuration(0)
        self.Target_QF.setStyleSheet(u"QFrame#Target_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));\n"
"border: 1px outset rgb(98, 91, 213);\n"
"}")
        self.Target_QF.setFrameShape(QFrame.StyledPanel)  # 这个组件 Target_QF 中的 label_6 是一个 QLabel，根据代码中的描述，它的样式表（StyleSheet）设置了字体、颜色等属性，且位于 Target_top 内部。
        self.Target_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Target_QF)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Target_top = QFrame(self.Target_QF)
        self.Target_top.setObjectName(u"Target_top")
        self.Target_top.setStyleSheet(u"border:none")
        self.Target_top.setFrameShape(QFrame.StyledPanel)
        self.Target_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Target_top)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 3, 0, 3)
        self.label_6 = QLabel(self.Target_top)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-right:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setIndent(0)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.verticalLayout_9.addWidget(self.Target_top)

        self.line_3 = QFrame(self.Target_QF)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(16777215, 1))
        self.line_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_3)

        self.Target_bottom = QFrame(self.Target_QF)
        self.Target_bottom.setObjectName(u"Target_bottom")
        self.Target_bottom.setStyleSheet(u"border:none")
        self.Target_bottom.setFrameShape(QFrame.StyledPanel)
        self.Target_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.Target_bottom)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 6, 0, 6)
        self.lineEdit_2 = QLineEdit(self.Target_bottom)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color: transparent;")
        self.lineEdit_2.setMaxLength(4)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.lineEdit_2)


        self.verticalLayout_9.addWidget(self.Target_bottom)

        self.verticalLayout_9.setStretch(1, 2)

        self.verticalLayout_33.addWidget(self.Target_QF)

        self.Fps_QF = QFrame(self.QF_Group)
        self.Fps_QF.setObjectName(u"Fps_QF")
        self.Fps_QF.setMinimumSize(QSize(170, 80))
        self.Fps_QF.setMaximumSize(QSize(170, 80))
        self.Fps_QF.setToolTipDuration(0)
        self.Fps_QF.setStyleSheet(u"QFrame#Fps_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));\n"
"border: 1px outset rgb(98, 91, 213);\n"
"}\n"
"")
        self.Fps_QF.setFrameShape(QFrame.StyledPanel)
        self.Fps_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Fps_QF)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Fps_top = QFrame(self.Fps_QF)
        self.Fps_top.setObjectName(u"Fps_top")
        self.Fps_top.setStyleSheet(u"border:none")
        self.Fps_top.setFrameShape(QFrame.StyledPanel)
        self.Fps_top.setFrameShadow(QFrame.Raised)  # 最后，Fps_QF 组件被添加到之前提到的 QF_Group 组件的布局中，可能将其放在用户界面的某个特定位置。
        self.horizontalLayout_8 = QHBoxLayout(self.Fps_top)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 3, 7, 3)
        self.label_7 = QLabel(self.Fps_top)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-right:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_7.setMidLineWidth(-1)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setIndent(0)

        self.horizontalLayout_8.addWidget(self.label_7)


        self.verticalLayout_11.addWidget(self.Fps_top)

        self.line_4 = QFrame(self.Fps_QF)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMaximumSize(QSize(16777215, 1))
        self.line_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_4)

        self.Fps_bottom = QFrame(self.Fps_QF)
        self.Fps_bottom.setObjectName(u"Fps_bottom")
        self.Fps_bottom.setStyleSheet(u"border:none")
        self.Fps_bottom.setFrameShape(QFrame.StyledPanel)
        self.Fps_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Fps_bottom)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 6, 0, 6)
        self.lineEdit_3 = QLineEdit(self.Fps_bottom)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font1)
        self.lineEdit_3.setStyleSheet(u"background-color: transparent;")
        self.lineEdit_3.setMaxLength(4)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.lineEdit_3)


        self.verticalLayout_11.addWidget(self.Fps_bottom)

        self.verticalLayout_11.setStretch(1, 2)

        self.verticalLayout_33.addWidget(self.Fps_QF)

        self.Model_QF = QFrame(self.QF_Group)
        self.Model_QF.setObjectName(u"Model_QF")
        self.Model_QF.setMinimumSize(QSize(170, 80))
        self.Model_QF.setMaximumSize(QSize(170, 80))
        self.Model_QF.setToolTipDuration(0)
        self.Model_QF.setStyleSheet(u"QFrame#Model_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));\n"
"border: 1px outset rgb(98, 91, 213);\n"
"}\n"
"")
        self.Model_QF.setFrameShape(QFrame.StyledPanel)
        self.Model_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.Model_QF)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Model_top = QFrame(self.Model_QF)
        self.Model_top.setObjectName(u"Model_top")
        self.Model_top.setStyleSheet(u"border:none")
        self.Model_top.setFrameShape(QFrame.StyledPanel)
        self.Model_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.Model_top)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 3, 7, 3)
        self.label_8 = QLabel(self.Model_top)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-right:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_8.setMidLineWidth(-1)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setIndent(0)

        self.horizontalLayout_9.addWidget(self.label_8)


        self.verticalLayout_13.addWidget(self.Model_top)

        self.line_5 = QFrame(self.Model_QF)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMaximumSize(QSize(16777215, 1))
        self.line_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_5)

        self.Model_bottom = QFrame(self.Model_QF)
        self.Model_bottom.setObjectName(u"Model_bottom")
        self.Model_bottom.setStyleSheet(u"border:none")
        self.Model_bottom.setFrameShape(QFrame.StyledPanel)
        self.Model_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.Model_bottom)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 6, 0, 6)
        self.lineEdit_4 = QLineEdit(self.Model_bottom)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font1)
        self.lineEdit_4.setStyleSheet(u"background-color: transparent;")
        self.lineEdit_4.setMaxLength(50)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.lineEdit_4)


        self.verticalLayout_13.addWidget(self.Model_bottom)

        self.verticalLayout_13.setStretch(1, 2)

        self.verticalLayout_33.addWidget(self.Model_QF)


        self.main_content.addWidget(self.QF_Group)

        self.char_label = QLabel(self.content)
        self.char_label.setObjectName(u"char_label")
        self.char_label.setMinimumSize(QSize(0, 20))
        self.char_label.setMaximumSize(QSize(16777215, 20))

        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.char_label.setFont(font2)
        self.char_label.setStyleSheet(u"padding-right:12px;")

        self.main_content.addWidget(self.char_label)

        self.Result_QF = QFrame(self.content)
        self.Result_QF.setObjectName(u"Result_QF")
        self.Result_QF.setStyleSheet(u"")
        self.Result_QF.setFrameShape(QFrame.StyledPanel)
        self.Result_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Result_QF)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.Result_QF)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setStyleSheet(u"#splitter::handle{background: 1px solid  rgba(200, 200, 200,100);}")
        # self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(2)

        # self.verticalLayout_16.addWidget(self.splitter)


        self.main_content.addWidget(self.Result_QF)
        # 创建一个垂直布局管理器用于居中对齐
        self.main_content.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addLayout(self.main_content)


        self.verticalLayout_6.addWidget(self.content)

        self.main_qframe.addWidget(self.splitter)
        self.main_qframe.addWidget(self.ContentBox)

        self.main_qframe.addWidget(self.RightMenuBg)
        self.verticalLayout.addWidget(self.Main_QF)

        window.setCentralWidget(self.Main_QW)

        self.retranslateUi(window)

        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"MainWindow", None))
        self.start_button.setText("")
        self.files_button.setText("")
        self.save_button.setText("")
        # self.undo_button.setText("")
        self.explain_title.setText(QCoreApplication.translate("window", u" Hope you have a good day", None))
        self.label_5.setText(QCoreApplication.translate("window", u"Confidence", None))
        self.lineEdit.setText(QCoreApplication.translate("window", u"0.3", None))
        self.lineEdit.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("window", u"Slice Height", None))
        self.lineEdit_2.setText(QCoreApplication.translate("window", u"0.7", None))
        self.label_7.setText(QCoreApplication.translate("window", u"Slice Width", None))
        self.lineEdit_3.setText(QCoreApplication.translate("window", u"0.7", None))
        self.label_8.setText(QCoreApplication.translate("window", u" Model", None))
        self.lineEdit_4.setText(QCoreApplication.translate("window", u"YOLOv8l.pt", None))
        self.char_label.setText(QCoreApplication.translate("window", u"                                         Input Image                                                                                                            Result Image", None))
    # retranslateUi

