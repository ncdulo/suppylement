PyMaengDa
---------
Quick & easy to use kratom burn tracking software. Simple input via command
line arguments. Data stored in CSV files. Provides output of various statistics
when requested.

Requirements
------------
Note: Other versions of these packages may very well work just fine. This
is simply the package versions used for this project, and specified in
`requirements.txt`.

* Python 3.6
* Pandas 1.0.0
  * Numpy 1.18.1
  * Python-dateutil 2.8.1
  * Pytz 2019.3
  * Six 1.14.0

Installation
------------
At the moment, the only supported installation is to directly clone this
repository and either run the wrapper script, or run the Python program
directly. In the future `pip` installation is planned to be supported.

The commands laid out below will clone this repository, create a new virtual
environment for PyMaengDa to run in, install the dependencies and display the
program's help text.


```
# Clone the repo
git clone https://github.com/ncdulo/pymaengda.git
cd pymaengda

# Create a new virtual environment and enable it
python -m venv .env
source .env/bin/activate

# Install dependencies
pip install -r requirements.txt

# To run via wrapper (recommended)
sh bin/pymaengda

# To run directly
python pymaengda/main.py

# If using virtual environment, to disable it when finished run:
deactivate
```

Usage
-----
Type this.

Notice
------
This program was created simply as an exercise in working with a slightly
larger Python project than I have before. Working with data, reading/writing
files, testing, that sort of thing. Kratom is intended strictly for botanical
purposes only. Not for human consumption. We cannot condone or encourage any
personal use or consumption of kratom.
