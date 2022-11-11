# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Projects/PythonProjects/KOLONTIP/KolonTip.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 571)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 42, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 63, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 52, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 21, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 42, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 21, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 42, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 63, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 52, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 21, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 42, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 21, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 21, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 42, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 63, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 52, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 21, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(25, 28, 28))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 21, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(19, 21, 21))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 42, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 42, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 42, 43))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 120, 701, 311))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setStyleSheet(" QGroupBox {\n"
"     \n"
"     border: 2px solid gray;\n"
"     border-radius: 5px;\n"
"     margin-top: 1ex; /* leave space at the top for the title */\n"
" }\n"
"\n"
" QGroupBox::title {\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top center; /* position at the top center */\n"
"     padding: 0 3px;\n"
"    color:white;\n"
" }")
        self.groupBox_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_10.setFlat(False)
        self.groupBox_10.setCheckable(False)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_combinations_5 = QtWidgets.QLabel(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_combinations_5.sizePolicy().hasHeightForWidth())
        self.label_combinations_5.setSizePolicy(sizePolicy)
        self.label_combinations_5.setMinimumSize(QtCore.QSize(120, 30))
        self.label_combinations_5.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_combinations_5.setFont(font)
        self.label_combinations_5.setStyleSheet("QLabel{\n"
"     padding:8px;\n"
"padding-top:10px;\n"
"padding-bottom:10px;\n"
"    color:white;\n"
"    border-left:0.5px solid;\n"
"    border-color:white;\n"
"\n"
"}")
        self.label_combinations_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_combinations_5.setObjectName("label_combinations_5")
        self.verticalLayout.addWidget(self.label_combinations_5)
        self.comboBox_section_name = QtWidgets.QComboBox(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_section_name.sizePolicy().hasHeightForWidth())
        self.comboBox_section_name.setSizePolicy(sizePolicy)
        self.comboBox_section_name.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_section_name.setMaximumSize(QtCore.QSize(10100, 16777215))
        self.comboBox_section_name.setBaseSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_section_name.setFont(font)
        self.comboBox_section_name.setStyleSheet("")
        self.comboBox_section_name.setObjectName("comboBox_section_name")
        self.verticalLayout.addWidget(self.comboBox_section_name)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_combinations_8 = QtWidgets.QLabel(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_combinations_8.sizePolicy().hasHeightForWidth())
        self.label_combinations_8.setSizePolicy(sizePolicy)
        self.label_combinations_8.setMinimumSize(QtCore.QSize(120, 30))
        self.label_combinations_8.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_combinations_8.setFont(font)
        self.label_combinations_8.setStyleSheet("QLabel{\n"
"     padding:8px;\n"
"padding-top:10px;\n"
"padding-bottom:10px;\n"
"    color:white;\n"
"    border-left:0.5px solid;\n"
"    border-color:white;\n"
"\n"
"}")
        self.label_combinations_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_combinations_8.setObjectName("label_combinations_8")
        self.verticalLayout_3.addWidget(self.label_combinations_8)
        self.listWidget_all_columns = QtWidgets.QListWidget(self.groupBox_10)
        self.listWidget_all_columns.setStyleSheet("\n"
"border-width:0.5px;\n"
"border-radius:2.5px;\n"
"background-color: rgb(54, 54, 54);\n"
"color:white;\n"
"padding:5px;\n"
"    color:white;\n"
"    border:0.5px solid;\n"
"    border-color:white; \n"
" ")
        self.listWidget_all_columns.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget_all_columns.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_all_columns.setAlternatingRowColors(False)
        self.listWidget_all_columns.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.listWidget_all_columns.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget_all_columns.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget_all_columns.setObjectName("listWidget_all_columns")
        self.verticalLayout_3.addWidget(self.listWidget_all_columns)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_combinations_7 = QtWidgets.QLabel(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_combinations_7.sizePolicy().hasHeightForWidth())
        self.label_combinations_7.setSizePolicy(sizePolicy)
        self.label_combinations_7.setMinimumSize(QtCore.QSize(120, 30))
        self.label_combinations_7.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_combinations_7.setFont(font)
        self.label_combinations_7.setStyleSheet("QLabel{\n"
"     padding:8px;\n"
"padding-top:10px;\n"
"padding-bottom:10px;\n"
"    color:white;\n"
"    border-left:0.5px solid;\n"
"    border-color:white;\n"
"\n"
"}")
        self.label_combinations_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_combinations_7.setObjectName("label_combinations_7")
        self.verticalLayout_2.addWidget(self.label_combinations_7)
        self.listWidget_selectted_columns_for_typing = QtWidgets.QListWidget(self.groupBox_10)
        self.listWidget_selectted_columns_for_typing.setStyleSheet("\n"
"border-width:0.5px;\n"
"border-radius:2.5px;\n"
"background-color: rgb(54, 54, 54);\n"
"color:white;\n"
"padding:5px;\n"
"    color:white;\n"
"    border:0.5px solid;\n"
"    border-color:white; \n"
" ")
        self.listWidget_selectted_columns_for_typing.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget_selectted_columns_for_typing.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_selectted_columns_for_typing.setAlternatingRowColors(False)
        self.listWidget_selectted_columns_for_typing.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.listWidget_selectted_columns_for_typing.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget_selectted_columns_for_typing.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget_selectted_columns_for_typing.setObjectName("listWidget_selectted_columns_for_typing")
        self.verticalLayout_2.addWidget(self.listWidget_selectted_columns_for_typing)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.pushButton_make_typing = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_make_typing.setEnabled(True)
        self.pushButton_make_typing.setGeometry(QtCore.QRect(10, 450, 711, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_make_typing.sizePolicy().hasHeightForWidth())
        self.pushButton_make_typing.setSizePolicy(sizePolicy)
        self.pushButton_make_typing.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_make_typing.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_make_typing.setFont(font)
        self.pushButton_make_typing.setStyleSheet("QPushButton{\n"
"border-width:0.5px;\n"
"border-radius:2.5px;\n"
"background-color: rgb(54, 54, 54);\n"
"color:white;\n"
"padding:5px;\n"
"    color:white;\n"
"    border:0.5px solid;\n"
"    border-color:white; \n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: qradialgradient(spread:pad, cx:0.494, cy:0.517, radius:2, fx:0.5, fy:0.528, stop:0 rgba(39, 43, 44, 255), stop:1 rgba(0, 209, 166, 255));\n"
"margin-left:10px;\n"
"border-width:0px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: white;\n"
"    size: 20;\n"
"margin-left:10px;\n"
"border-width:0.5px;\n"
"border-style: outset;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/frequency.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_make_typing.setIcon(icon)
        self.pushButton_make_typing.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_make_typing.setObjectName("pushButton_make_typing")
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setGeometry(QtCore.QRect(20, 10, 701, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setStyleSheet(" QGroupBox {\n"
"     \n"
"     border: 2px solid gray;\n"
"     border-radius: 5px;\n"
"     margin-top: 1ex; /* leave space at the top for the title */\n"
" }\n"
"\n"
" QGroupBox::title {\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top center; /* position at the top center */\n"
"     padding: 0 3px;\n"
"    color:white;\n"
" }")
        self.groupBox_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_11.setFlat(False)
        self.groupBox_11.setCheckable(False)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_63 = QtWidgets.QLabel(self.groupBox_11)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setToolTipDuration(-1)
        self.label_63.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_63.setScaledContents(True)
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.gridLayout.addWidget(self.label_63, 0, 0, 1, 1)
        self.label_combinations_6 = QtWidgets.QLabel(self.groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_combinations_6.sizePolicy().hasHeightForWidth())
        self.label_combinations_6.setSizePolicy(sizePolicy)
        self.label_combinations_6.setMinimumSize(QtCore.QSize(120, 30))
        self.label_combinations_6.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_combinations_6.setFont(font)
        self.label_combinations_6.setStyleSheet("QLabel{\n"
"     padding:8px;\n"
"padding-top:10px;\n"
"padding-bottom:10px;\n"
"    color:white;\n"
"    border-left:0.5px solid;\n"
"    border-color:white;\n"
"\n"
"}")
        self.label_combinations_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_combinations_6.setObjectName("label_combinations_6")
        self.gridLayout.addWidget(self.label_combinations_6, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_path = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_path.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"border: 2px solid rgba(39, 43, 44, 255);\n"
"\n"
"border-width:0.5px;\n"
"border-radius:2.5px;\n"
"background-color: rgb(54, 54, 54);\n"
"color:white;\n"
"padding:5px;\n"
"    color:white;\n"
"    border:0.5px solid;\n"
"    border-color:white; \n"
" ")
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.horizontalLayout.addWidget(self.lineEdit_path)
        self.pushButton_select_path = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_select_path.setStyleSheet("QPushButton{\n"
"border-width:0.5px;\n"
"border-radius:2.5px;\n"
"background-color: rgb(54, 54, 54);\n"
"color:white;\n"
"padding:5px;\n"
"    color:white;\n"
"    border:0.5px solid;\n"
"    border-color:white; \n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: qradialgradient(spread:pad, cx:0.494, cy:0.517, radius:2, fx:0.5, fy:0.528, stop:0 rgba(39, 43, 44, 255), stop:1 rgba(0, 209, 166, 255));\n"
"margin-left:1px;\n"
"border-width:0px;\n"
"border-style: outset;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: white;\n"
"    size: 20;\n"
"margin-left:10px;\n"
"border-width:0.5px;\n"
"border-style: outset;\n"
"}")
        self.pushButton_select_path.setObjectName("pushButton_select_path")
        self.horizontalLayout.addWidget(self.pushButton_select_path)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.comboBox_sheet_name_excel = QtWidgets.QComboBox(self.groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_sheet_name_excel.sizePolicy().hasHeightForWidth())
        self.comboBox_sheet_name_excel.setSizePolicy(sizePolicy)
        self.comboBox_sheet_name_excel.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_sheet_name_excel.setMaximumSize(QtCore.QSize(10100, 16777215))
        self.comboBox_sheet_name_excel.setBaseSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_sheet_name_excel.setFont(font)
        self.comboBox_sheet_name_excel.setStyleSheet("")
        self.comboBox_sheet_name_excel.setObjectName("comboBox_sheet_name_excel")
        self.gridLayout.addWidget(self.comboBox_sheet_name_excel, 1, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_section_name.setCurrentIndex(-1)
        self.comboBox_sheet_name_excel.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_10.setTitle(_translate("MainWindow", "TİPLENDİRME AYARLARI"))
        self.label_combinations_5.setText(_translate("MainWindow", "KESİT İSMİ SÜTUNU"))
        self.comboBox_section_name.setProperty("placeholderText", _translate("MainWindow", "Düşey yük kombinasyonu"))
        self.label_combinations_8.setText(_translate("MainWindow", "TÜM SÜTUN İSİMLERİ"))
        self.label_combinations_7.setText(_translate("MainWindow", "TİPLENDİR İÇİN SÜTUN SEÇİMİ"))
        self.pushButton_make_typing.setText(_translate("MainWindow", "TİPLENDİR"))
        self.groupBox_11.setTitle(_translate("MainWindow", "EXCEL AYARLARI"))
        self.label_63.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#555555;\">Kesme Çatlama Dayanımı | Vcr(tonf)=0,65*fctd*bw*d*(1+ γ*Nd/Ac)</span></p></body></html>"))
        self.label_63.setText(_translate("MainWindow", "TİPLENDİRME YAPILACAK EXCEL DOSYASI"))
        self.label_combinations_6.setText(_translate("MainWindow", "EXCEL PAFTA İSMİ"))
        self.pushButton_select_path.setText(_translate("MainWindow", "SEÇ"))
        self.comboBox_sheet_name_excel.setProperty("placeholderText", _translate("MainWindow", "Düşey yük kombinasyonu"))

import Media.icons_rc
