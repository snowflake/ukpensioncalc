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

"""Line parser"""
from . import convert


def parser(main, line, lineno):
    """Parse the line at linenumber lineno"""
    s = line.split(sep=None)
    l = len(s)
    if not l:  # Test if line is whitespace
        return
    elif l >= 1:
        if s[0][0] == '#':  # a comment
            return
        elif s[0] == 'rate':
            if l == 3:
                # add to the rates database
                main.rates_db.add_rate(s[1], s[2], lineno=lineno)
            else:
                raise ValueError('Not enough or too many dates and rates')
        elif s[0] == 'oneoff':
            if l == 3:
                # add to the oneoff database
                main.oneoff_db.add_rate(s[1], s[2], lineno=lineno)
            else:
                raise ValueError('Not enough or too many dates ' +
                                 'and one-off payments')
        elif s[0] == 'accrualday':
            if main.accrualday:
                raise ValueError('Duplicate accrualday directive')
            if l != 2:
                raise ValueError('accrualday requires one parameter ' +
                                 '(day of week)')
            acc_day_num = convert.day_number(s[1])
            if 0 <= acc_day_num <= 4:  # Is day between Mon .. Fri ?
                main.accrualday = s[1]
            else:
                raise ValueError('accrualday must be one of Monday Tuesday ' +
                                 'Wednesday Thursday Friday')
        elif s[0] == 'name':
            main.name = joiner(s)
        elif s[0] == 'description':
            main.description = joiner(s)
        else:
            raise ValueError('Unknown directive (misspelled?): ' + s[0])


def joiner(list_of_strings):
    """Join all the stings in the list, excepting the first"""
    if len(list_of_strings) > 1:
        return ' '.join(list_of_strings[1:])
    return ''
