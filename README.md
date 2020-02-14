Suppylement
---------
Quick & easy to use nutritional supplement tracking software. Simple input via
command line arguments. Data stored in CSV files. Provides output of various
statistics when requested.

The intention of this project is to allow the user to track various types and
amounts of nutritional supplements. This can be helpful when trying a new
supplement, or changing things. As you will have a log of what you did, and
when. The ability to run statistics and analysis on the data can be useful as
well. Interpretation of the results presented is an exercise for the user ;)

Currently, there are no plans to add a GUI to this program. The decision was
made because it will add an undue layer of complexity to a relatively simple
design. Suppylement aims to be intuitive in it's use on the command line.

Suppylement is still a very new project, having only been created in the end
of January 2020. The current state is still very much in-progress and very
much unfinished. Most of the functionality has not yet been implemented. Work
is underway, however. Without giving any sort of time estimates, I think the
functional prototype milestone is not a very far reach once the time is made.

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
environment for Suppylement to run in, install the dependencies and display
the program's help text.


```
# Clone the repo
git clone https://github.com/ncdulo/suppylement.git
cd suppylement

# Create a new virtual environment and enable it
python -m venv .env
source .env/bin/activate

# Install dependencies
pip install -r requirements.txt

# To run via wrapper (recommended)
sh bin/suppylement --help

# To run directly
python suppylement/main.py --help

# If using virtual environment, to disable it when finished run:
deactivate

# Link the executable to `/usr/local/bin` so that it's available in `$PATH`
sudo ln -sf /path/to/repo/bin/suppylement /usr/local/bin/suppylement
```

Usage
-----
Suppylement aims to be simple and intuitive to use. The full set of arguments
has not be decided on or implemented yet but anything that is can be listed
with the `-h` or `--help` argument. Some basic examples are listed below. Note
that some (most) functionality is currently not fully implemented.

```
# Display help
sh bin/suppylement --help
sh bin/suppylement log --help

# List most recent 5 entries
sh bin/suppylement list
# List most recent 20 entries
sh bin/suppylement list --most-recent 20

# Log a new entry
sh bin/suppylement log 1000 VitaminC
sh bin/suppylement log 250 magnesium-citrate

# Delete the most recent entry
sh bin/suppylement rm
# Delete the most recent 5 entries
sh bin/suppylement rm --most-recent 5

# View statistics
sh bin/suppylement stats
# View full statistics
sh bin/suppylement stats --full
```

Development Goals & Roadmap
---------------------------
Stub section for an overview of the current development direction, priorities,
and goals. The roadmap is planned to be more of a list of features than an
a full-fledged roadmap document.


Contributing
------------
This will be filled in with a brief overview of some general guidelines for
contributing to this project. Also a link to the full text when created.
