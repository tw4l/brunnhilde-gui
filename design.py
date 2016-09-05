# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
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
        MainWindow.resize(687, 832)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout.addWidget(self.radioButton)
        self.directorySource = QtGui.QLineEdit(self.centralwidget)
        self.directorySource.setText(_fromUtf8(""))
        self.directorySource.setObjectName(_fromUtf8("directorySource"))
        self.verticalLayout.addWidget(self.directorySource)
        self.directoryBrowseBtn = QtGui.QPushButton(self.centralwidget)
        self.directoryBrowseBtn.setObjectName(_fromUtf8("directoryBrowseBtn"))
        self.verticalLayout.addWidget(self.directoryBrowseBtn)
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout.addWidget(self.radioButton_2)
        self.diskImageSource = QtGui.QLineEdit(self.centralwidget)
        self.diskImageSource.setText(_fromUtf8(""))
        self.diskImageSource.setObjectName(_fromUtf8("diskImageSource"))
        self.verticalLayout.addWidget(self.diskImageSource)
        self.diskImageBrowseBtn = QtGui.QPushButton(self.centralwidget)
        self.diskImageBrowseBtn.setObjectName(_fromUtf8("diskImageBrowseBtn"))
        self.verticalLayout.addWidget(self.diskImageBrowseBtn)
        self.hfsDiskBtn = QtGui.QCheckBox(self.centralwidget)
        self.hfsDiskBtn.setObjectName(_fromUtf8("hfsDiskBtn"))
        self.verticalLayout.addWidget(self.hfsDiskBtn)
        self.removeFilesBtn = QtGui.QCheckBox(self.centralwidget)
        self.removeFilesBtn.setObjectName(_fromUtf8("removeFilesBtn"))
        self.verticalLayout.addWidget(self.removeFilesBtn)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.destination = QtGui.QLineEdit(self.centralwidget)
        self.destination.setText(_fromUtf8(""))
        self.destination.setObjectName(_fromUtf8("destination"))
        self.verticalLayout.addWidget(self.destination)
        self.destinationBrowseBtn = QtGui.QPushButton(self.centralwidget)
        self.destinationBrowseBtn.setObjectName(_fromUtf8("destinationBrowseBtn"))
        self.verticalLayout.addWidget(self.destinationBrowseBtn)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.identifier = QtGui.QLineEdit(self.centralwidget)
        self.identifier.setText(_fromUtf8(""))
        self.identifier.setObjectName(_fromUtf8("identifier"))
        self.verticalLayout.addWidget(self.identifier)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.skipClamscanBtn = QtGui.QCheckBox(self.centralwidget)
        self.skipClamscanBtn.setObjectName(_fromUtf8("skipClamscanBtn"))
        self.verticalLayout.addWidget(self.skipClamscanBtn)
        self.bulkExtractorBtn = QtGui.QCheckBox(self.centralwidget)
        self.bulkExtractorBtn.setObjectName(_fromUtf8("bulkExtractorBtn"))
        self.verticalLayout.addWidget(self.bulkExtractorBtn)
        self.scanArchivesBtn = QtGui.QCheckBox(self.centralwidget)
        self.scanArchivesBtn.setObjectName(_fromUtf8("scanArchivesBtn"))
        self.verticalLayout.addWidget(self.scanArchivesBtn)
        self.throttleSiegfriedBtn = QtGui.QCheckBox(self.centralwidget)
        self.throttleSiegfriedBtn.setObjectName(_fromUtf8("throttleSiegfriedBtn"))
        self.verticalLayout.addWidget(self.throttleSiegfriedBtn)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout.addWidget(self.textEdit_2)
        self.startScanBtn = QtGui.QPushButton(self.centralwidget)
        self.startScanBtn.setObjectName(_fromUtf8("startScanBtn"))
        self.verticalLayout.addWidget(self.startScanBtn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Brunnhilde GUI", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Choose source</span></p></body></html>", None))
        self.radioButton.setText(_translate("MainWindow", "Directory", None))
        self.directorySource.setPlaceholderText(_translate("MainWindow", "/path/to/directory", None))
        self.directoryBrowseBtn.setText(_translate("MainWindow", "Browse", None))
        self.radioButton_2.setText(_translate("MainWindow", "Disk image", None))
        self.diskImageSource.setPlaceholderText(_translate("MainWindow", "/path/to/disk/image", None))
        self.diskImageBrowseBtn.setText(_translate("MainWindow", "Browse", None))
        self.hfsDiskBtn.setText(_translate("MainWindow", "Hierarchical File System (HFS)-formatted disk", None))
        self.removeFilesBtn.setText(_translate("MainWindow", "Remove files carved from disk image at end of process", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Destination for reports</span></p></body></html>", None))
        self.destination.setPlaceholderText(_translate("MainWindow", "/path/to/reports/directory", None))
        self.destinationBrowseBtn.setText(_translate("MainWindow", "Browse", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Accesion number or identifier</span></p></body></html>", None))
        self.identifier.setPlaceholderText(_translate("MainWindow", "Enter accession no. or other identifer (no spaces)", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Options</span></p></body></html>", None))
        self.skipClamscanBtn.setText(_translate("MainWindow", "Skip virus scan", None))
        self.bulkExtractorBtn.setText(_translate("MainWindow", "Run bulk_extractor", None))
        self.scanArchivesBtn.setText(_translate("MainWindow", "Scan archive files (zip, tar, etc.)", None))
        self.throttleSiegfriedBtn.setText(_translate("MainWindow", "Throttle Siegfried", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Output (stdout)</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Errors (stderr)</span></p></body></html>", None))
        self.startScanBtn.setText(_translate("MainWindow", "Start scan", None))

