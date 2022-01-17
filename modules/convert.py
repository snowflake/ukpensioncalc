
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

"""Conversion functions for dates, decimals, and days of the week"""
import datetime
from decimal import Decimal as D
import re

# dates in iso format yyyy-mm-dd
re_iso = re.compile(r'^[0-9]{4,4}-[01][0-9]-[0-3][0-9]$')
# dates in uk format dd/mm/yyyy
re_ukdate = re.compile(r'^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4,4}$')
# values like 9999.01
re_value = re.compile(r'^[0-9]{1,6}\.[0-9]{2,2}$')

daydict = {'Monday':   0,
           'Tuesday':   1,
           'Wednesday': 2,
           'Thursday':  3,
           'Friday':    4,
           'Saturday':  5,
           'Sunday':    6}

day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday']


def convert_date(datestring):
    """Convert a date string"""
    if isinstance(datestring, datetime.date):
        # already a date
        return datestring
    if re_iso.match(datestring):
        return datetime.date.fromisoformat(datestring)
    elif re_ukdate.match(datestring):
        datelist = datestring.split('/')
        return datetime.date(int(datelist[2]),  # Year
                             int(datelist[1]),   # Month
                             int(datelist[0]))   # Day
    else:
        raise ValueError('Unrecognised date: ' + datestring)


def convert_value(value):
    """Convert decimal string to Decimal"""
    if isinstance(value, D):
        return value
    if not re_value.match(value):
        raise ValueError('Invalid decimal value', value)
    return D(value)


def day_number(daystring):
    """Given a day of the week like 'Tuesday', return the day_number ( Monday = 0 )"""
    if not isinstance(daystring, str):
        raise ValueError('Error: day name must be a string: ' + str(daystring))
    try:
        number = daydict[daystring]
    except KeyError:
        raise ValueError('Error: Not a day of the week: ' + daystring)
    return number


def day_name(daynumber):
    """Given a day number int 0..6, return day name as string"""
    if not isinstance(daynumber, int):
        raise ValueError('Error: expecting integer in convert.day_name()')
    if not 0 <= daynumber <= 6:
        raise ValueError('Error: day number must be 0 .. 6')
    return day_list[daynumber]
