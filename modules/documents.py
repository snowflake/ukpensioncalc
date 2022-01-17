#
# % BSD 3-Clause License
# %
# % Copyright (c) 2022, David Evans
# % All rights reserved.
# %
# % Redistribution and use in source and binary forms, with or without
# % modification, are permitted provided that the following conditions are met:
# %
# % 1. Redistributions of source code must retain the above copyright notice,
# %    this list of conditions and the following disclaimer.
# %
# % 2. Redistributions in binary form must reproduce the above copyright
# %    notice, this list of conditions and the following disclaimer in the
# %    documentation and/or other materials provided with the distribution.
# %
# % 3. Neither the name of the copyright holder nor the names of its
# %    contributors may be used to endorse or promote products derived from
# %    this software without specific prior written permission.
# %
# % THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# % "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# % TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# % PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# % CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# % EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# % PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# % PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# % LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# % NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# % SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Print a sample configuration file"""


def sample_print():
    """Print sample file"""
    print(sample)


sample = """# sample configuration for the pension calculator

# Configuration files should be plain text.
# Edit your configuration file with an editor in plain text mode, not rich
# text format or any other wordprocessor format.
# Example editors are: 
# TextEdit (macOS), emacs, vim, vi, nano, and many others.
#
# Use only ASCII characters in your configuration file.
# See https://en.wikipedia.org/wiki/ASCII#Printable_characters
#
# Using extended characters from Unicode or Window Latin 1
# will result in the file being rejected. Avoid the pound sign.

##############################################################################

# Comments start with a '#' and are ignored.
# whitespace characters are Tabs and Spaces
     # There can be whitespace before a comment.
# Whitespace can be used in directives to make thing line up.
# Lines containing only whitespace are ignored, as are empty lines.

##############################################################################

# The 'name' directive is optional.
# We suggest you use the name directive to specify the name of the person
# whom this file applies to.

name   Kermit the Frog

# The 'description' directive is optional.
# You can use it for any descriptive text you like.

description   Frogs pay tax too.

##############################################################################

# The 'accrualday' directive specifies the tax on the week that your
# pension accrues on. It should be the same as your payment day.
# This directive is required.
#
# To find your accrual day, visit:
# https://www.gov.uk/state-pension/what-youll-get
#
# The accrualday should be one of Monday Tuesday Wednesday Thursday Friday
# This directive is required.  There should be only one accrualday
# directive in the file.

accrualday	 Thursday

##############################################################################

# The 'rate' directive specifies the weekly pension accrual.
#
# The directive take 2 parameters, the date the rate applies from, and the
# rate applying on or after that date up to the day before the next rate.

#         Start date  	    Payment

rate      2010-04-15  	    300.02
rate	  14/4/2011	    310.78
rate	  15/4/2012	    319.22
rate      1/5/2013	    340.37
rate	  2014-05-13        355.72
rate      2015-01-10          0.00

          #########################################
          #                                       #
          #              WARNING                  #
          #                                       #
          #   You should delete all these rates   #
          #         and add your own!!!           #
          #                                       #
          #########################################



# The date can be specified in UK or ISO format.
#
# The year must be between 2000 and 2099
#
# UK format is  dd/mm/yyyy
#     dd and mm can be either one or two digits.
#     yyyy must always be 4 digits
# 

# ISO format is yyyy-mm-dd
#     yyyy is always 4 digits. mm and dd are always 2 digits

# The payment is speified as  nnnn.nn
#     There must be exactly 2 digits to the right of the decimal point,
#     even when both digits are zero.
# 
#     There must be from one to six digits to the left of the decimal point.
#     Do not put pound signs in front of your payments.
#
# Make sure you specify the weekly rate, not the monthly payment from your
# bank statement.

"""
