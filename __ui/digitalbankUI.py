# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\project\digital_bank\__ui\digitalbankUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(758, 362)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.open_acc_checkBox = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.open_acc_checkBox.setFont(font)
        self.open_acc_checkBox.setObjectName(_fromUtf8("open_acc_checkBox"))
        self.verticalLayout_3.addWidget(self.open_acc_checkBox)
        self.close_acc_checkBox = QtGui.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.close_acc_checkBox.setFont(font)
        self.close_acc_checkBox.setObjectName(_fromUtf8("close_acc_checkBox"))
        self.verticalLayout_3.addWidget(self.close_acc_checkBox)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.date_lineEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_lineEdit.sizePolicy().hasHeightForWidth())
        self.date_lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.date_lineEdit.setFont(font)
        self.date_lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.date_lineEdit.setObjectName(_fromUtf8("date_lineEdit"))
        self.horizontalLayout_8.addWidget(self.date_lineEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.generate_account_num_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.generate_account_num_lineEdit.setObjectName(_fromUtf8("generate_account_num_lineEdit"))
        self.horizontalLayout_7.addWidget(self.generate_account_num_lineEdit)
        self.loadAccount_pushButton = QtGui.QPushButton(self.centralwidget)
        self.loadAccount_pushButton.setObjectName(_fromUtf8("loadAccount_pushButton"))
        self.horizontalLayout_7.addWidget(self.loadAccount_pushButton)
        self.generate_account_num_pushButton = QtGui.QPushButton(self.centralwidget)
        self.generate_account_num_pushButton.setObjectName(_fromUtf8("generate_account_num_pushButton"))
        self.horizontalLayout_7.addWidget(self.generate_account_num_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.account_type_label = QtGui.QLabel(self.centralwidget)
        self.account_type_label.setObjectName(_fromUtf8("account_type_label"))
        self.horizontalLayout_3.addWidget(self.account_type_label)
        self.account_type_comboBox = QtGui.QComboBox(self.centralwidget)
        self.account_type_comboBox.setObjectName(_fromUtf8("account_type_comboBox"))
        self.account_type_comboBox.addItem(_fromUtf8(""))
        self.account_type_comboBox.addItem(_fromUtf8(""))
        self.account_type_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.account_type_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.account_holder_name_label = QtGui.QLabel(self.centralwidget)
        self.account_holder_name_label.setObjectName(_fromUtf8("account_holder_name_label"))
        self.horizontalLayout_2.addWidget(self.account_holder_name_label)
        spacerItem1 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.account_holder_name_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.account_holder_name_lineEdit.setObjectName(_fromUtf8("account_holder_name_lineEdit"))
        self.horizontalLayout_2.addWidget(self.account_holder_name_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.date_of_birth_label = QtGui.QLabel(self.centralwidget)
        self.date_of_birth_label.setObjectName(_fromUtf8("date_of_birth_label"))
        self.horizontalLayout_10.addWidget(self.date_of_birth_label)
        spacerItem2 = QtGui.QSpacerItem(42, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.date_of_birth_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.date_of_birth_lineEdit.setObjectName(_fromUtf8("date_of_birth_lineEdit"))
        self.horizontalLayout_10.addWidget(self.date_of_birth_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.mobile_num_label = QtGui.QLabel(self.centralwidget)
        self.mobile_num_label.setObjectName(_fromUtf8("mobile_num_label"))
        self.horizontalLayout_6.addWidget(self.mobile_num_label)
        spacerItem3 = QtGui.QSpacerItem(33, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.mobile_num_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.mobile_num_lineEdit.setObjectName(_fromUtf8("mobile_num_lineEdit"))
        self.horizontalLayout_6.addWidget(self.mobile_num_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.address_label = QtGui.QLabel(self.centralwidget)
        self.address_label.setObjectName(_fromUtf8("address_label"))
        self.horizontalLayout_5.addWidget(self.address_label)
        spacerItem4 = QtGui.QSpacerItem(65, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.address_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.address_lineEdit.setObjectName(_fromUtf8("address_lineEdit"))
        self.horizontalLayout_5.addWidget(self.address_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.aadhar_num_label = QtGui.QLabel(self.centralwidget)
        self.aadhar_num_label.setObjectName(_fromUtf8("aadhar_num_label"))
        self.horizontalLayout_4.addWidget(self.aadhar_num_label)
        spacerItem5 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.aadhar_num_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.aadhar_num_lineEdit.setObjectName(_fromUtf8("aadhar_num_lineEdit"))
        self.horizontalLayout_4.addWidget(self.aadhar_num_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.gender_label = QtGui.QLabel(self.centralwidget)
        self.gender_label.setObjectName(_fromUtf8("gender_label"))
        self.horizontalLayout_9.addWidget(self.gender_label)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.male_radioButton = QtGui.QRadioButton(self.centralwidget)
        self.male_radioButton.setObjectName(_fromUtf8("male_radioButton"))
        self.horizontalLayout_9.addWidget(self.male_radioButton)
        self.female_radioButton = QtGui.QRadioButton(self.centralwidget)
        self.female_radioButton.setObjectName(_fromUtf8("female_radioButton"))
        self.horizontalLayout_9.addWidget(self.female_radioButton)
        self.other_radioButton = QtGui.QRadioButton(self.centralwidget)
        self.other_radioButton.setObjectName(_fromUtf8("other_radioButton"))
        self.horizontalLayout_9.addWidget(self.other_radioButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.create_pushButton = QtGui.QPushButton(self.centralwidget)
        self.create_pushButton.setObjectName(_fromUtf8("create_pushButton"))
        self.horizontalLayout_11.addWidget(self.create_pushButton)
        self.reset_pushButton = QtGui.QPushButton(self.centralwidget)
        self.reset_pushButton.setObjectName(_fromUtf8("reset_pushButton"))
        self.horizontalLayout_11.addWidget(self.reset_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Digital Bank", None))
        self.open_acc_checkBox.setText(_translate("MainWindow", "Open Bank Account", None))
        self.close_acc_checkBox.setText(_translate("MainWindow", "Close Bank Account", None))
        self.loadAccount_pushButton.setText(_translate("MainWindow", "Load Account", None))
        self.generate_account_num_pushButton.setText(_translate("MainWindow", "Generate Account Number", None))
        self.account_type_label.setText(_translate("MainWindow", "Account Type", None))
        self.account_type_comboBox.setItemText(0, _translate("MainWindow", "Savings", None))
        self.account_type_comboBox.setItemText(1, _translate("MainWindow", "Current", None))
        self.account_type_comboBox.setItemText(2, _translate("MainWindow", "Salary", None))
        self.account_holder_name_label.setText(_translate("MainWindow", "Account Holder Name", None))
        self.date_of_birth_label.setText(_translate("MainWindow", "Date of Birth", None))
        self.mobile_num_label.setText(_translate("MainWindow", "Mobile Number", None))
        self.address_label.setText(_translate("MainWindow", "Address", None))
        self.aadhar_num_label.setText(_translate("MainWindow", "Aadhar Number", None))
        self.gender_label.setText(_translate("MainWindow", "Gender", None))
        self.male_radioButton.setText(_translate("MainWindow", "male", None))
        self.female_radioButton.setText(_translate("MainWindow", "female", None))
        self.other_radioButton.setText(_translate("MainWindow", "other", None))
        self.create_pushButton.setText(_translate("MainWindow", "Create", None))
        self.reset_pushButton.setText(_translate("MainWindow", "Reset", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

