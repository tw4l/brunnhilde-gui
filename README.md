## Brunnhilde GUI  
Version 2.0.0

### Installation  

#### Install Siegfried  

Install Siegfried. See [Siegfried Github repo](https://github.com/richardlehane/siegfried/) for instructions.

#### Install Brunnhilde CLI utility  

Install the Brunnhilde command-line utility:

`sudo pip install brunnhilde`

This version of the GUI requires Brunnhilde 1.6.1 or higher. To check which version of Brunnhilde you have installed, type: `brunnhilde.py -V`. To upgrade your version of Brunnhilde to the latest, use `sudo pip install --upgrade brunnhilde`

#### Install PyQt5  

Install PyQt5 if not already installed.  

`sudo pip install pyqt5` or `sudo pip3 install pyqt5` (depending on default Python/pip in your system)

#### GUI Installation in Bitcurator  

* Download tar.gz or zip file and extract to location of your choice (or clone repo with 'git clone').  
* Run install shell script:  
`sudo bash install`  

You will now be able to launch the Brunnhilde GUI by double-clicking on the Brunnhilde icon in the "Forensics and Reporting" folder.  

#### GUI Installation in Linux

* Download zip or tar.gz file from Github and extract files to location of your choice  
* Modify the install script to create the Brunnhilde GUI.desktop file in a location of your choice. This will become the graphical launcher for the Brunnhilde GUI. Alternatively, save the code to a location of your choice and launch the GUI by entering the following in a terminal:   
`python3 /path/to/brunnhilde-gui/main.py`  

#### GUI Installation in MacOS/OS X  

* Download zip or tar.gz file from Github and extract files to location of your choice  
* Launch GUI by entering the following in a terminal:  
`python3 /path/to/brunnhilde-gui/main.py`  

### Usage  

For detailed information about how Brunnhilde works, see the [Brunnhilde command line utility](https://github.com/timothyryanwalsh/brunnhilde) repo.  

### Licensing  

The MIT License (MIT)  

Copyright (c) 2017 Tim Walsh  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
