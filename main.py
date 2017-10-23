#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtGui import *
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *
import subprocess
import sys

import design

class StartScanThread(QThread):

    def __init__(self, process_list):
        QThread.__init__(self)
        self.process_list = process_list

    def start_scan(self):
        print(self.process_list) # for debugging
        subprocess.check_output(self.process_list)

    def run(self):
        self.start_scan()

class BrunnhildeApp(QMainWindow, design.Ui_Brunnhilde):

    def __init__(self, parent=None):
        super(BrunnhildeApp, self).__init__(parent)
        self.setupUi(self)

        # build browse functionality buttons
        self.dirSourceBtn.clicked.connect(self.browse_dirsource)
        self.diskImageSourceBtn.clicked.connect(self.browse_diskimage)
        self.dirDestinationBtn.clicked.connect(self.browse_dirdest)
        self.diskImageDestinationBtn.clicked.connect(self.browse_diskimagedest)

        # build start functionalities
        self.dirStartScanBtn.clicked.connect(self.start_scan_dir)
        self.diskImageStartScan.clicked.connect(self.start_scan_diskimage)

        # about menu functionality
        self.actionAbout.triggered.connect(self.about_dialog)

        # Set buttons
        self.dirCancelBtn.setEnabled(False)
        self.dirStartScanBtn.setEnabled(True)
        self.diskImageCancelBtn.setEnabled(False)
        self.diskImageStartScan.setEnabled(True)
    
    def about_dialog(self):
        QMessageBox.information(self, "About", 
            "Brunnhilde GUI v.2.0.0\nTim Walsh, 2017\nMIT License\nhttps://github.com/timothyryanwalsh/brunnhilde-gui\nCompatible with Brunnhilde 1.6.1+")

    def browse_dirsource(self):
        self.dirSource.clear() # clear directory source text
        directory = QFileDialog.getExistingDirectory(self, "Select folder")

        if directory: # if user didn't pick directory don't continue
            self.dirSource.setText(directory)

    def browse_diskimage(self):
        self.diskImageSource.clear() # clear existing disk image source text
        diskimage = QFileDialog.getOpenFileName(self, "Select disk image")[0]

        if diskimage:
            self.diskImageSource.setText(diskimage)

    def browse_dirdest(self):
        self.dirDestination.clear() # clear existing report destination text
        directory = QFileDialog.getExistingDirectory(self, "Select folder")

        if directory: # if user didn't pick directory don't continue
            self.dirDestination.setText(directory)

    def browse_diskimagedest(self):
        self.diskImageDestination.clear() # clear existing report destination text
        directory = QFileDialog.getExistingDirectory(self, "Select folder")

        if directory: # if user didn't pick directory don't continue
            self.diskImageDestination.setText(directory)

    def done_dir(self):
        self.dirCancelBtn.setEnabled(False)
        self.dirStartScanBtn.setEnabled(True)
        QMessageBox.information(self, "Finished", "Brunnhilde scan complete.")
        self.dirStatus.setText('Finished')

    def done_diskimage(self):
        self.diskImageCancelBtn.setEnabled(False)
        self.diskImageStartScan.setEnabled(True)
        QMessageBox.information(self, "Finished", "Brunnhilde scan complete.")
        self.diskImageStatus.setText('Finished')

    def start_scan_dir(self):
        # clear output window
        self.dirStatus.clear()

        # create list for process
        self.process_list = list()
        self.process_list.append("brunnhilde.py")
        
        # give indication process has started
        self.dirStatus.setText('Processing')

        # universal option handling
        if not self.virusScan.isChecked():
            self.process_list.append('-n')
        if self.largeFiles.isChecked():
            self.process_list.append('-l')
        if self.bulkExtractor.isChecked():
            self.process_list.append('-b')
        if self.scanArchives.isChecked():
            self.process_list.append('-z')
        if self.throttleSiegfried.isChecked():
            self.process_list.append('-t')
        if self.sfWarnings.isChecked():
            self.process_list.append('-w')
        if self.sha1.isChecked():
            self.process_list.append('--hash')
            self.process_list.append('sha1')
        if self.sha256.isChecked():
            self.process_list.append('--hash')
            self.process_list.append('sha256')
        if self.sha512.isChecked():
            self.process_list.append('--hash')
            self.process_list.append('sha512')

        self.process_list.append(self.dirSource.text())
        self.process_list.append(self.dirDestination.text())
        self.process_list.append(self.dirIdentifier.text())

        # process
        self.get_thread = StartScanThread(self.process_list)
        self.get_thread.finished.connect(self.done_dir)
        self.get_thread.start()
        self.dirCancelBtn.setEnabled(True)
        self.dirCancelBtn.clicked.connect(self.get_thread.terminate)
        self.dirStartScanBtn.setEnabled(False)


    def start_scan_diskimage(self):
        # clear output window
        self.diskImageStatus.clear()

        # create list for process
        self.process_list = list()
        self.process_list.append("brunnhilde.py")

        # give indication process has started
        self.diskImageStatus.setText('Processing')

        # add disk image flag  
        self.process_list.append('-d')
        
        # universal option handling
        if not self.virusScan.isChecked():
            self.process_list.append('-n')
        if self.largeFiles.isChecked():
            self.process_list.append('-l')
        if self.bulkExtractor.isChecked():
            self.process_list.append('-b')
        if self.scanArchives.isChecked():
            self.process_list.append('-z')
        if self.throttleSiegfried.isChecked():
            self.process_list.append('-t')
        if self.sfWarnings.isChecked():
            self.process_list.append('-w')
        if self.sha1.isChecked():
            self.process_list.append('--hash')
            self.process_list.append('sha1')
        if self.sha256.isChecked():
            self.process_list.append('--hash')
            self.process_list.append('sha256')
        if self.sha512.isChecked():
            self.process_list.append('--hash')
            self.process_list.append('sha512')

        # disk image option handling
        if self.removeFiles.isChecked():
            self.process_list.append('-r')
        if self.hfsDisk.isChecked():
            self.process_list.append('--hfs')
        if self.resForks.isChecked():
            self.process_list.append('--resforks')

        self.process_list.append(self.diskImageSource.text())
        self.process_list.append(self.diskImageDestination.text())
        self.process_list.append(self.diskImageIdentifier.text())

         # process
        self.get_thread = StartScanThread(self.process_list)
        self.get_thread.finished.connect(self.done_diskimage)
        self.get_thread.start()
        self.diskImageCancelBtn.setEnabled(True)
        self.diskImageCancelBtn.clicked.connect(self.get_thread.terminate)
        self.diskImageStartScan.setEnabled(False)

def main():
    app = QApplication(sys.argv)
    form = BrunnhildeApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
