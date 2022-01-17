#!/usr/bin/env python3

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

"""UK State Pension calculator"""
import argparse
import re
import sys
import io
import modules


def main():
    """The main body of the program"""
    if sys.hexversion < 0x03070000:
        print('This program requires Python 3.7+')
        sys.exit(1)

    desc = """Calculate UK State Pension accruing in a tax year"""

    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-r', '--ratesfile', help='Name of the rates file.',
                        required=False, nargs=1)
    parser.add_argument('-t', '--taxyearending', required=False, nargs=1,
                        help="""The calendar year in which \
the tax year ended. \
Enter the year as a 4 digit number between 2000 and 2099.""")
    parser.add_argument('--sample', action="store_true",
                        help="""Show a sample rates file.""")
    parser.add_argument('--licence', action='store_true',
                        help='Show the software licence and disclaimer.')
    parser.add_argument('--version', action='store_true',
                        help='Show the version of this program')
    args = parser.parse_args()
    if args.version:
        print('Pension Calculator version 1.2.3')
        sys.exit(0)
    if args.sample:
        modules.documents.sample_print()
        sys.exit(0)
    if args.licence:
        modules.licence.licence_show()
        sys.exit(0)
    if not (args.taxyearending and args.ratesfile):
        print('Both the --taxyearending and --ratefile options are required.')
        sys.exit(1)
    ys = args.taxyearending[0]
    # validate the tax year is 2000 to 2099
    r = re.compile('^20[0-9]{2,2}$')
    if not r.match(ys):
        print()
        print('Error: Tax Year Ending must be in the range 2000 to 2099')
        sys.exit(1)

    ms = modules.mainstore.Main_store()
    ms.set_taxyear(ys)
    # Read the file and parse it
    try:
        with io.open(args.ratesfile[0], encoding='ascii', newline=None) \
                as config:
            lineno = 0
            error_count = 0
            for line in config:
                lineno = lineno + 1
                try:
                    modules.parser.parser(ms, line, lineno)
                except ValueError as inst:
                    error_count = error_count + 1
                    print('-------------------')
                    print('There is an error at line ' + str(lineno))
                    print(line)
                    print(inst.args[0])
                    print()
            config.close()
    except UnicodeDecodeError:
        print('Error: unknown character in the file: ' + args.ratesfile[0])
        print('You must create the file using a plain text editor.')
        print('Use only ASCII characters in the file.')
        print('Do not use a pound sign.')
        sys.exit(1)
    except FileNotFoundError:
        print('Error: File not found: ' + args.ratesfile[0])
        sys.exit(1)
    if not ms.accrualday:
        print('-------------------')
        error_count = error_count + 1
        print('-------------------')
        print('Error: required directive \"accrualday\" not found')
    if error_count:
        print('Lines: ' + str(lineno) + ', Errors: ' + str(error_count))
        print('Cannot continue.')
        sys.exit(1)
    ms.print()
    modules.calculate.calculate(ms)
    return ms
# ------------------- End of subroutines ------------------


ms = main()
