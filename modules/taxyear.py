# 
#% BSD 3-Clause License
#% 
#% Copyright (c) 2022, David Evans
#% All rights reserved.
#% 
#% Redistribution and use in source and binary forms, with or without
#% modification, are permitted provided that the following conditions are met:
#% 
#% 1. Redistributions of source code must retain the above copyright notice,
#%    this list of conditions and the following disclaimer.
#% 
#% 2. Redistributions in binary form must reproduce the above copyright
#%    notice, this list of conditions and the following disclaimer in the
#%    documentation and/or other materials provided with the distribution.
#% 
#% 3. Neither the name of the copyright holder nor the names of its
#%    contributors may be used to endorse or promote products derived from
#%    this software without specific prior written permission.
#% 
#% THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#% "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
#% TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#% PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
#% CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#% EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#% PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#% PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#% LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#% NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#% SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



"""Taxyear class"""

import datetime

APRIL = 4  # The month in which a tax year begins or ends
START_DAY = 6
END_DAY = START_DAY - 1

def printdate(date):
    """Return a friendly string representation of date"""
    return date.strftime(' %A %e %B %Y ')

class Taxyear:
    """Definitions for a tax year"""

    def __init__(self, year):
        """Initialise a tax year
          Integer year is the end year of the tax year"""
        self.year_ending = year
        self.start_date = datetime.date(year - 1, APRIL, START_DAY)
        self.end_date = datetime.date(year, APRIL, END_DAY)

    def in_tax_year(self, date):
        """Return True if date is within a tax year"""
        return self.start_date <= date <= self.end_date

    def __str__(self):
        """Return a string describing the tax year"""
        return 'Tax year from' + printdate(self.start_date) + 'to' \
            + printdate(self.end_date)

    
if __name__ == "__main__":
    YY = 2020
    y = Taxyear(YY)
    print('For tax year ending', YY)
    print(y)
    print(YY, 'should be', y.year_ending)
    print("Begin:", y.start_date)
    print("End:", y.end_date)
    d = datetime.date(YY, 1, 1)
    print(y.in_tax_year(d), 'should be True')
    d = datetime.date(1999, 2, 2)
    print(y.in_tax_year(d), 'should be False')
