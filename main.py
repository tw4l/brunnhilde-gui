#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import * 
import subprocess
import sys

import design

class BrunnhildeApp(QMainWindow, design.Ui_MainWindow):

    def __init__(self, parent=None):
        super(BrunnhildeApp, self).__init__(parent)
        self.setupUi(self)

        # build browse functionality buttons
        self.directoryBrowseBtn.clicked.connect(self.browse_dirsource)
        self.diskImageBrowseBtn.clicked.connect(self.browse_diskimage)
        self.destinationBrowseBtn.clicked.connect(self.browse_dest)

        # build start functionality
        self.startScanBtn.clicked.connect(self.start_scan)

    @pyqtSlot()
    def readStdOutput(self):
        self.textEdit.append(QString(self.proc.readAllStandardOutput()))

    @pyqtSlot()
    def readStdError(self):
        self.textEdit_2.append(QString(self.proc.readAllStandardError()))

    def browse_dirsource(self):
        self.directorySource.clear() # clear directory source text
        directory = QFileDialog.getExistingDirectory(self, "Select folder")

        if directory: # if user didn't pick directory don't continue
            self.directorySource.setText(directory)

    def browse_diskimage(self):
        self.diskImageSource.clear() # clear existing disk image source text
        diskimage = QFileDialog.getOpenFileName(self, "Select disk image")

        if file: # if user didn't pick file don't continue
            self.diskImageSource.setText(diskimage)

    def browse_dest(self):
        self.destination.clear() # clear existing report destination text
        directory = QFileDialog.getExistingDirectory(self, "Select folder")

        if directory: # if user didn't pick directory don't continue
            self.destination.setText(directory)

    def start_scan(self):
        # clear output windows
        self.textEdit.clear()
        self.textEdit_2.clear()

        # create list for options
        self.options = []
        
        # give indication process has started
        self.textEdit.append('Process started.')

        # source is a directory
        if self.radioButton.isChecked():

            # universal option handling
            if self.skipClamscanBtn.isChecked():
                self.options.append('-n')
            if self.bulkExtractorBtn.isChecked():
                self.options.append('-b')
            if self.scanArchivesBtn.isChecked():
                self.options.append('-z')
            if self.throttleSiegfriedBtn.isChecked():
                self.options.append('-t')
            if self.sfWarningsBtn.isChecked():
                self.options.append('-w')
            if self.btn_sha1.isChecked():
                self.options.append('--hash')
                self.options.append('sha1')
            if self.btn_sha256.isChecked():
                self.options.append('--hash')
                self.options.append('sha256')
            if self.btn_sha512.isChecked():
                self.options.append('--hash')
                self.options.append('sha512')


            # run brunnhilde.py as QProcess and redirect stdout and stderr to GUI
            self.proc = QProcess()
            self.proc.start("python", QStringList() << 'brunnhilde.py' << self.options << 
                self.directorySource.text() << self.destination.text() << self.identifier.text())
            self.proc.setProcessChannelMode(QProcess.MergedChannels);
            QObject.connect(self.proc, SIGNAL("readyReadStandardOutput()"), self, SLOT("readStdOutput()"));
            QObject.connect(self.proc, SIGNAL("readyReadStandardError()"), self, SLOT("readStdError()"));

        # source is a disk image
        elif self.radioButton_2.isChecked():
            
            # add disk image flag  
            self.options.append('-d')
            
            # universal option handling
            if self.skipClamscanBtn.isChecked():
                self.options.append('-n')
            if self.bulkExtractorBtn.isChecked():
                self.options.append('-b')
            if self.scanArchivesBtn.isChecked():
                self.options.append('-z')
            if self.throttleSiegfriedBtn.isChecked():
                self.options.append('-t')
            if self.sfWarningsBtn.isChecked():
                self.options.append('-w')
            if self.btn_sha1.isChecked():
                self.options.append('--hash')
                self.options.append('sha1')
            if self.btn_sha256.isChecked():
                self.options.append('--hash')
                self.options.append('sha256')
            if self.btn_sha512.isChecked():
                self.options.append('--hash')
                self.options.append('sha512')

            # disk image option handling
            if self.removeFilesBtn.isChecked():
                self.options.append('-r')
            if self.hfsDiskBtn.isChecked():
                self.options.append('--hfs')

             # run brunnhilde.py as QProcess and redirect stdout and stderr to GUI
            self.proc = QProcess()
            self.proc.start("python", QStringList() << 'brunnhilde.py' << self.options << 
                self.diskImageSource.text() << self.destination.text() << self.identifier.text())
            self.proc.setProcessChannelMode(QProcess.MergedChannels);
            QObject.connect(self.proc, SIGNAL("readyReadStandardOutput()"), self, SLOT("readStdOutput()"));
            QObject.connect(self.proc, SIGNAL("readyReadStandardError()"), self, SLOT("readStdError()"));

def main():
    app = QApplication(sys.argv)
    form = BrunnhildeApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
