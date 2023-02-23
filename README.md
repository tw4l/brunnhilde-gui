# Brunnhilde GUI

Version 2.1.0

## Installation  

### Install Siegfried  

Install Siegfried. See [Siegfried Github repo](https://github.com/richardlehane/siegfried/) for instructions.

### Install Brunnhilde CLI utility  

Install the Brunnhilde command-line utility:

`sudo pip install brunnhilde` or `sudo pip3 install brunnhilde`

This version of the GUI requires Brunnhilde 1.6.1 or higher. To check which version of Brunnhilde you have installed, type: `brunnhilde.py -V`. To upgrade your version of Brunnhilde to the latest, use `sudo pip install --upgrade brunnhilde`

### Install PyQt5  

Install PyQt5 if not already installed.  

`sudo pip install pyqt5` or `sudo pip3 install pyqt5`

#### GUI Installation in Bitcurator 4.x.x / Ubuntu 22

```bash
git clone https://github.com/tw4l/brunnhilde-gui
cd brunnhilde-gui
sudo ./install
```

You will now be able to launch the Brunnhilde GUI by double-clicking on the Brunnhilde icon in the upper menu under Applications -> Forensics and Reporting.

### GUI Installation in Bitcurator 1.x.x-3.x.x / Ubuntu 18-20

```bash
git clone https://github.com/tw4l/brunnhilde-gui
cd brunnhilde-gui
sudo ./install-bc2-ubuntu18
```

You will now be able to launch the Brunnhilde GUI by double-clicking on the Brunnhilde icon in the "Forensics and Reporting" Desktop folder.  

### GUI Installation in MacOS/OS X  

* Download zip or tar.gz file from Github and extract files to location of your choice  
* Launch GUI by entering the following in a terminal:  
`python3 /path/to/brunnhilde-gui/main.py`  

## Usage  

For detailed information about how Brunnhilde works, see the [Brunnhilde command line utility](https://github.com/tw4l/brunnhilde) repo.  

## Creators

* Canadian Centre for Architecture
* Tessa Walsh

This project was initially developed in 2016-2017 for the [Canadian Centre for Architecture](https://www.cca.qc.ca) by Tessa Walsh, Digital Archivist, as part of the development of the Archaeology of the Digital project.
