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


import argparse
import re
import sys

from . import rates, taxyear


class Main_store:
    """A class to store various parameters"""

    def __init__(self):
        """Initialize the databases"""
        self.rates_db = rates.Rates()  # rates database
        self.oneoff_db = rates.Rates()  # one-off database
        self.taxyear = None
        self.name = ''
        self.description = ''
        self.accrualday = None

    def print(self):
        notspec = '*** Not Specified ***'
        if self.name:
            print('Name:', self.name)
        else:
            print('Name:', notspec)
        if self.description:
            print('Description:', self.description)
        else:
            print('Description:', notspec)
        if self.taxyear:
            print(self.taxyear)
        else:
            print('Taxyear:', notspec)
        if self.accrualday:
            print('Accrual Day:', self.accrualday)
        else:
            print('Accrual Day:', notspec)
        print('One-Off Payments')
        self.oneoff_db.list_rates()
        print('Pension Payment Rates')
        self.rates_db.list_rates()

    def set_taxyear(self, taxyear_str):
        """Create a taxyear instance"""
        self.taxyear = taxyear.Taxyear(int(taxyear_str))
