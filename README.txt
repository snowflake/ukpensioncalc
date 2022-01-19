Pension calculator for UK State Pension from the DWP

Disclaimer

This software is developed independently of DWP and HMRC and it is not
endorsed by them. See also the LICENSE file.

Q: What does this software do?

A: It calculates the total state pension accruing in a tax year. This is
not necessarily the same as the total obtained by adding up all the
payments to your bank account in a tax year.

Q: How do I obtain the software?

Go to our software repository on GitHub:
https://github.com/snowflake/ukpensioncalc

if you are not already viewing this document there.

On the right-hand-side of the page, under Releases, click on the release
next to the Latest icon.

This takes you to the releases page.

On the left-hand-side, under Assets, you should see 2 Source code links.
If these are not shown, click on the triangle next to Assets. To
download the software, click on Source code (zip) or ```Source code
(tar.gz) deoending on which format of archive you want

Installing the program

Create an empty folder and unpack the softare archive into it.

Running the progam

This progam requires Python3 version 3.7 or later versions.

Python3 is avalable as standard on recent versions of macOS.

Python3 for Windows and macOS can be downloaded from:

    ( the Python site ) https://www.python.org 

It can also be obtained using your operating system's package manager.

On Linux there is apt-get and several others.

On FreeBSD use pkg

On macOS there is Homebrew and Macports. Macports supports older
versions of macOS

Change into the folder you just created and type at the prompt:

         python3 pension.py --help

to get the help.

To see the calculation for the sample.txt configuration file, type:

         python3 pension.py --ratesfile sample.txt --taxyearend 2013

Copy sample.txt to yourfile.txt

Edit yourfile.txt using a plain text editor. Change the configuration as
desired for your own tax rates, using the comments as a guide. Use the
letters you receive from DWP each year to configure the rates.

Now run:

        python3 pension.py --ratesfile yourfile.txt --taxyearend 2021

to see the calculation for the tax year ending 2021.
