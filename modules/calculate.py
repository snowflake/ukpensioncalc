
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

"""Calculate the pension and print the results"""

import datetime
import decimal
from . import convert
DAYS_IN_WEEK = 7


def calculate(ms):
    """Calculate the total pension for a tax year. ms is an instance \
 of mainstore class"""
    count_of_payments = {}
    accrual_day_of_week = convert.day_number(ms.accrualday)  # returns 0..6

    # Calcualate the first accrual day in the taxyear
    offset = (accrual_day_of_week - ms.taxyear.start_date.weekday()) \
        % DAYS_IN_WEEK
    first_accrual_day = ms.taxyear.start_date + datetime.timedelta(days=offset)
    print('First accrual day in taxyear: ' + str(first_accrual_day))
    total = decimal.Decimal('0.00')  # Initialise
    loop = first_accrual_day
    while loop <= ms.taxyear.end_date:
        rate = ms.rates_db.get_rate_for_date(loop)
        #    print(str(loop) + ' ' + str(rate))
        total = total + rate
        if rate in count_of_payments:
            count_of_payments[rate] = count_of_payments.get(rate) + 1
        else:
            count_of_payments[rate] = 1
        loop = loop + datetime.timedelta(days=DAYS_IN_WEEK)  # goto next week

    print('-------------------- calculation results --------------------')
    print(str(ms.taxyear))
    print('Pension received by: ', ms.name)
    for a in count_of_payments:
        print('There are ', str(count_of_payments[a]),
              ' weekly accruals of ', str(a))
    print('Grand total: ' + str(total))
