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


from decimal import Decimal as D
import datetime
# from operator import itemgetter
from . import convert


def sort_key(entry):
    """Get the value for a key"""
    return entry[ds]


ds = 'date'
rs = 'rate'


class Rates:
    """Code for maintaining the rates and payments databases"""

    def __init__(self):
        self.__sorted = False
        self.__rates = []
        self.duplicates = {}  # A dict to check for duplicate entries
        self.add_rate(datetime.date(1, 1, 1), D('0.00'))
        self.add_rate(datetime.date(9999, 12, 31), D('0.00'))

    def list_rates(self):
        """List all the rates"""
        self.sort_rates()
        for i in self.__rates:
            print(i[ds], i[rs])

    def __str__(self):
        """create string of the rates if called by print(rates)"""
        self.sort_rates()
        ret = ''
        for i in self.__rates:
            ret = ret + str(i[ds]) + '   ' + str(i[rs]) + '\n'
        return ret

    def sort_rates(self):
        """Sort the database"""
        if not self.__sorted:
            self.__rates.sort(key=sort_key)
            self.__sorted = True

    def add_rate(self, date, rate, lineno=999999):
        """Add a rate to the database"""
        dt = convert.convert_date(date)
        rt = convert.convert_value(rate)
        dups = self.duplicates.get(dt)  # check for duplicates
        if dups:
            raise ValueError('Entry already in database at line ' +
                             str(dups) + ', date = ' + str(dt))
        self.duplicates[dt] = lineno
        self.__rates.append({ds: dt,
                             rs: rt})
        self.__sorted = False

    def get_rate_for_date(self, datex):
        """Get rate for datex. date can be a string or datetime.date object"""
        date = convert.convert_date(datex)
        self.sort_rates()
        for i in range(0, len(self.__rates) - 1):
            # is date on or after first date and before second date
            #            print('comparing ')
            if self.__rates[i][ds] <= date < self.__rates[i+1][ds]:
                return self.__rates[i][rs]
        # Should not get to this line
        raise RuntimeError('rates.py: could not find rate for date')
