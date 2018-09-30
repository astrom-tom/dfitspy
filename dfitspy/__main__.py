#!/usr/bin/./python
# -*- coding: utf-8 -*-

'''
---dfitspy---

dfitspy is a program aimed at reproducing the dfits program in python.
the functions can be used inside another program or it can also be called
as an executable

usage: dfitspy FILE.fits OBJECT

@place: ESO - La Silla - Paranal Observatory
@author(s): Romain Thomas
@year(s):  ex 2018
@First version: 19.9-0
@Current version: 19.9-0
@Telescope(s): ALL
@Instrument(s): ALL
@Valid for SciOpsPy: v0.1-b
@Documentation url:
@Last SciOps review [date + name]: 18-09-2018 - Romain Thomas
@Usage: dfitspy FILE.fits HEADER_KEY_WORD, diftspy --help for more options
@Licence: GPL
@Testable:
@Test data place (if any required):
'''


###Python standard library
import sys

###local imports
from . import cli
from . import display as dp
from . import readfits
from . import get_files_and_keys as get
from . import tests

def main():
    ###first we load the command line interface
    args = cli.command_line(sys.argv[1:])

    if args.test:
        tests.test()
        ###exit code
        sys.exit()

    ###get all the files
    list_files = get.get_files(args.file, args.dir)
    print('\n\033[1m[DFITSPY INFO]> %s files found \033[0;0m'%len(list_files))
    print('\033[1m',35*'-', '\033[0;0m')

    if list_files == []:
        print('\n\033[1m[DFITSPY Error]>Invalid file name or no fits file found \033[0;0m')
        sys.exit()

    if args.list:
        ###get all keywords
        all_keywords = readfits.get_all_keyword(list_files[0])
        ###display them
        dp.display_list(all_keywords)
        sys.exit()

    ###get greeping from command line
    if args.grep:
        grep = args.grep
    else:
        grep = False

    if not args.key:
        print('\n\033[1m[DFISTPY Error]>no keywords given...exit... \033[0;0m')
        sys.exit()
    else:
        ##get all keywords
        list_keys = get.get_keys(args.key)

    ##get all values for each keys and each files
    allvalues = readfits.get_all_values(list_files, list_keys, grep)

    ##display them in terminal
    dp.display_final(allvalues)

if __name__ == "__main__":
    main()
