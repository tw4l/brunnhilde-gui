# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Brunnhilde(object):
    def setupUi(self, Brunnhilde):
        Brunnhilde.setObjectName("Brunnhilde")
        Brunnhilde.resize(658, 522)
        self.centralwidget = QtWidgets.QWidget(Brunnhilde)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 631, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.directoryTab = QtWidgets.QWidget()
        self.directoryTab.setObjectName("directoryTab")
        self.layoutWidget = QtWidgets.QWidget(self.directoryTab)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 21, 611, 267))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dirSource = QtWidgets.QLineEdit(self.layoutWidget)
        self.dirSource.setObjectName("dirSource")
        self.horizontalLayout.addWidget(self.dirSource)
        self.dirSourceBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.dirSourceBtn.setObjectName("dirSourceBtn")
        self.horizontalLayout.addWidget(self.dirSourceBtn)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dirDestination = QtWidgets.QLineEdit(self.layoutWidget)
        self.dirDestination.setObjectName("dirDestination")
        self.horizontalLayout_2.addWidget(self.dirDestination)
        self.dirDestinationBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.dirDestinationBtn.setObjectName("dirDestinationBtn")
        self.horizontalLayout_2.addWidget(self.dirDestinationBtn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.dirIdentifier = QtWidgets.QLineEdit(self.layoutWidget)
        self.dirIdentifier.setObjectName("dirIdentifier")
        self.verticalLayout_7.addWidget(self.dirIdentifier)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.dirStatus = QtWidgets.QLineEdit(self.layoutWidget)
        self.dirStatus.setObjectName("dirStatus")
        self.verticalLayout_8.addWidget(self.dirStatus)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dirCancelBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.dirCancelBtn.setObjectName("dirCancelBtn")
        self.horizontalLayout_3.addWidget(self.dirCancelBtn)
        self.dirStartScanBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.dirStartScanBtn.setDefault(True)
        self.dirStartScanBtn.setFlat(False)
        self.dirStartScanBtn.setObjectName("dirStartScanBtn")
        self.horizontalLayout_3.addWidget(self.dirStartScanBtn)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.directoryTab, "")
        self.diskImageTab = QtWidgets.QWidget()
        self.diskImageTab.setObjectName("diskImageTab")
        self.layoutWidget_2 = QtWidgets.QWidget(self.diskImageTab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(11, 21, 611, 301))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_10.addWidget(self.label_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.diskImageSource = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.diskImageSource.setObjectName("diskImageSource")
        self.horizontalLayout_4.addWidget(self.diskImageSource)
        self.diskImageSourceBtn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.diskImageSourceBtn.setObjectName("diskImageSourceBtn")
        self.horizontalLayout_4.addWidget(self.diskImageSourceBtn)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.verticalLayout_14.addLayout(self.verticalLayout_10)
        self.hfsDisk = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.hfsDisk.setObjectName("hfsDisk")
        self.verticalLayout_14.addWidget(self.hfsDisk)
        self.verticalLayout_15.addLayout(self.verticalLayout_14)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.diskImageDestination = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.diskImageDestination.setObjectName("diskImageDestination")
        self.horizontalLayout_5.addWidget(self.diskImageDestination)
        self.diskImageDestinationBtn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.diskImageDestinationBtn.setObjectName("diskImageDestinationBtn")
        self.horizontalLayout_5.addWidget(self.diskImageDestinationBtn)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.verticalLayout_15.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_12.addWidget(self.label_11)
        self.diskImageIdentifier = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.diskImageIdentifier.setObjectName("diskImageIdentifier")
        self.verticalLayout_12.addWidget(self.diskImageIdentifier)
        self.verticalLayout_15.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_13.addWidget(self.label_12)
        self.diskImageStatus = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.diskImageStatus.setObjectName("diskImageStatus")
        self.verticalLayout_13.addWidget(self.diskImageStatus)
        self.verticalLayout_15.addLayout(self.verticalLayout_13)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.diskImageCancelBtn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.diskImageCancelBtn.setObjectName("diskImageCancelBtn")
        self.horizontalLayout_6.addWidget(self.diskImageCancelBtn)
        self.diskImageStartScan = QtWidgets.QPushButton(self.layoutWidget_2)
        self.diskImageStartScan.setDefault(True)
        self.diskImageStartScan.setFlat(False)
        self.diskImageStartScan.setObjectName("diskImageStartScan")
        self.horizontalLayout_6.addWidget(self.diskImageStartScan)
        self.verticalLayout_15.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.diskImageTab, "")
        self.optionsTab = QtWidgets.QWidget()
        self.optionsTab.setObjectName("optionsTab")
        self.layoutWidget_3 = QtWidgets.QWidget(self.optionsTab)
        self.layoutWidget_3.setGeometry(QtCore.QRect(11, 21, 422, 380))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.virusScan = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.virusScan.setChecked(True)
        self.virusScan.setObjectName("virusScan")
        self.verticalLayout.addWidget(self.virusScan)
        self.largeFiles = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.largeFiles.setObjectName("largeFiles")
        self.verticalLayout.addWidget(self.largeFiles)
        self.verticalLayout_16.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.md5 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.md5.setChecked(True)
        self.md5.setObjectName("md5")
        self.horizontalLayout_7.addWidget(self.md5)
        self.sha256 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.sha256.setObjectName("sha256")
        self.horizontalLayout_7.addWidget(self.sha256)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.sha1 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.sha1.setObjectName("sha1")
        self.horizontalLayout_8.addWidget(self.sha1)
        self.sha512 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.sha512.setObjectName("sha512")
        self.horizontalLayout_8.addWidget(self.sha512)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.verticalLayout_16.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.removeFiles = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.removeFiles.setObjectName("removeFiles")
        self.verticalLayout_3.addWidget(self.removeFiles)
        self.resForks = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.resForks.setObjectName("resForks")
        self.verticalLayout_3.addWidget(self.resForks)
        self.verticalLayout_16.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.scanArchives = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.scanArchives.setChecked(True)
        self.scanArchives.setObjectName("scanArchives")
        self.verticalLayout_4.addWidget(self.scanArchives)
        self.sfWarnings = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.sfWarnings.setChecked(True)
        self.sfWarnings.setObjectName("sfWarnings")
        self.verticalLayout_4.addWidget(self.sfWarnings)
        self.bulkExtractor = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.bulkExtractor.setObjectName("bulkExtractor")
        self.verticalLayout_4.addWidget(self.bulkExtractor)
        self.throttleSiegfried = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.throttleSiegfried.setObjectName("throttleSiegfried")
        self.verticalLayout_4.addWidget(self.throttleSiegfried)
        self.verticalLayout_16.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.optionsTab, "")
        Brunnhilde.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Brunnhilde)
        self.statusbar.setObjectName("statusbar")
        Brunnhilde.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(Brunnhilde)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 25))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        Brunnhilde.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(Brunnhilde)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(Brunnhilde)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Brunnhilde)

    def retranslateUi(self, Brunnhilde):
        _translate = QtCore.QCoreApplication.translate
        Brunnhilde.setWindowTitle(_translate("Brunnhilde", "Brunnhilde"))
        self.label.setText(_translate("Brunnhilde", "<html><head/><body><p><span style=\" font-weight:600;\">Source</span></p></body></html>"))
        self.dirSource.setPlaceholderText(_translate("Brunnhilde", "/path/to/source/directory"))
        self.dirSourceBtn.setText(_translate("Brunnhilde", "Browse"))
        self.label_5.setText(_translate("Brunnhilde", "<html><head/><body><p><span style=\" font-weight:600;\">Destination</span></p></body></html>"))
        self.dirDestination.setPlaceholderText(_translate("Brunnhilde", "/path/to/output/directory"))
        self.dirDestinationBtn.setText(_translate("Brunnhilde", "Browse"))
        self.label_6.setText(_translate("Brunnhilde", "<html><head/><body><p><span style=\" font-weight:600;\">Accession number/identifier</span></p></body></html>"))
        self.dirIdentifier.setPlaceholderText(_translate("Brunnhilde", "Enter accession number or other identifier (no spaces)"))
        self.label_7.setText(_translate("Brunnhilde", "<html><head/><body><p><span style=\" font-weight:600;\">Status</span></p></body></html>"))
        self.dirCancelBtn.setText(_translate("Brunnhilde", "Cancel"))
        self.dirStartScanBtn.setText(_translate("Brunnhilde", "Start scan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.directoryTab), _translate("Brunnhilde", "Directory"))
        self.label_9.setText(_translate("Brunnhilde", "<html><head/><body><p><span style=\" font-weight:600;\">Source</span></p></body></html>"))
        self.diskImageSource.setPlaceholderText(_translate("Brunnhilde", "/path/to/diskimage"))
        self.diskImageSourceBtn.setText(_translate("Brunnhilde", "Browse"))
        self.hfsDisk.setText(_translate("Brunnhilde", "Hierarchical File System (HFS)-formatted disk"))
        self.label_10.setText(_translate("Brunnhilde", "<html><head/><body><p><span style=\" font-weight:600;\">Destination</span></p></body></html>"))
        self.diskImageDestination.setPlaceholderText(_translate("Brunnhilde", "/path/to/output/directory"))
        self.diskImageDestinationBtn.setText(_translate("Brunnhilde", "Browse"))
        self.label_11.setText(_translate("Brunnhilde", "<html><head/><body><p><span style=\" font-weight:600;\">Accession number/identifier</span></p></body></html>"))
        self.diskImageIdentifier.setPlaceholderText(_translate("Brunnhilde", "Enter accession number or other identifier (no spaces)"))
        self.label_12.setText(_translate("Brunnhilde", "<html><head/><body><p><span style=\" font-weight:600;\">Status</span></p></body></html>"))
        self.diskImageCancelBtn.setText(_translate("Brunnhilde", "Cancel"))
        self.diskImageStartScan.setText(_translate("Brunnhilde", "Start scan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.diskImageTab), _translate("Brunnhilde", "Disk Image"))
        self.label_2.setText(_translate("Brunnhilde", "<html><head/><body><p><span style=\" font-weight:600;\">Virus scanning</span></p></body></html>"))
        self.virusScan.setText(_translate("Brunnhilde", "Scan for viruses"))
        self.largeFiles.setText(_translate("Brunnhilde", "Scan large files and sources (note: may take much longer)"))
        self.label_3.setText(_translate("Brunnhilde", "<html><head/><body><p><span style=\" font-weight:600;\">Checksum algorithm</span></p></body></html>"))
        self.md5.setText(_translate("Brunnhilde", "md5"))
        self.sha256.setText(_translate("Brunnhilde", "sha256"))
        self.sha1.setText(_translate("Brunnhilde", "sha1"))
        self.sha512.setText(_translate("Brunnhilde", "sha512"))
        self.label_8.setText(_translate("Brunnhilde", "<html><head/><body><p><span style=\" font-weight:600;\">Disk image options</span></p></body></html>"))
        self.removeFiles.setText(_translate("Brunnhilde", "Remove files carved from disk image at end of process"))
        self.resForks.setText(_translate("Brunnhilde", "Extract AppleDouble resource forks from HFS disks"))
        self.label_4.setText(_translate("Brunnhilde", "<html><head/><body><p><span style=\" font-weight:600;\">General options</span></p></body></html>"))
        self.scanArchives.setText(_translate("Brunnhilde", "Scan archive files (zip, tar, gzip, warc, arc)"))
        self.sfWarnings.setText(_translate("Brunnhilde", "Include Siegfried warnings in HTML report"))
        self.bulkExtractor.setText(_translate("Brunnhilde", "Run bulk_extractor"))
        self.throttleSiegfried.setText(_translate("Brunnhilde", "Throttle Siegfried"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optionsTab), _translate("Brunnhilde", "Options"))
        self.menuAbout.setTitle(_translate("Brunnhilde", "About"))
        self.actionAbout.setText(_translate("Brunnhilde", "About"))
        self.actionAbout.setToolTip(_translate("Brunnhilde", "About"))

