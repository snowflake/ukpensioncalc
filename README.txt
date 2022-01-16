Pension calculator for UK State Pension from the DWP

This progam requires Python3 version 3.7 or later versions.

Python3 is avalable as standard on recent versions of macOS.

Python3 for Windows and macOS can be downloaded from:

	https://www.python.org

It can also be obtained using your operating system's package manager.

On Linux there is apt-get and several others.

On FreeBSD use pkg

On macOS there is Homebrew and Macports. Macports supports older versions
of macOS

-----

In your operating system, open a shell.

Create a new empty folder and unpack the zip file into it.

Change into the folder you just created and type at the prompt:

     python3 pension.py --help

to get the help.

To see the calculation for the sample.txt configuration file, type:

     python3 pension.py --ratesfile sample.txt --taxyearend 2013

Copy sample.txt to  yourfile.txt

Edit yourfile.txt using a plain text editor.  Change the configuration
as desired for your own tax rates, using the comments as a guide. Use the
letters you receive from DWP each year to configure the rates.

Now run:

    python3 pension.py --ratesfile yourfile.txt --taxyearend 2021

to see the calculation for the  tax year ending 2021.




