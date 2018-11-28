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
* Install Python 3 PyQt5 library:  
`sudo pip3 install pyqt5`  

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

### Creators

* Canadian Centre for Architecture
* Tim Walsh

This project was initially developed in 2016-2017 for the [Canadian Centre for Architecture](https://www.cca.qc.ca) by Tim Walsh, Digital Archivist, as part of the development of the Archaeology of the Digital project.
