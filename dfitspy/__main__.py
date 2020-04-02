#!/usr/bin/./python
# -*- coding: utf-8 -*-

'''
---dfitspy---

dfitspy is a program aimed at reproducing the dfits program in python.
the functions can be used inside another program or it can also be called
as an executable

usage: dfitspy -f FILE.fits -k OBJECT

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
@Testable: Yes
@Test data place (if any required): inside the package
'''


###Python standard library
import sys
import os
from subprocess import call
import datetime
import socket


###local imports
from . import __info__ as info
from . import cli
from . import display as dp
from . import readfits
from . import get_files_and_keys as get
from . import tests

def main():
    '''
    This is the main function of the program.
    '''
    ###first we load the command line interface
    args = cli.command_line(sys.argv[1:])

    ###here we check if at least one argument was given:
    if not args.docs and args.file is None and args.grep is None and \
            args.key is None and not args.list and not args.test:
        print('\033[1m[DFITSPY Error]> no argument passed ...exit\033[0;0m')
        sys.exit()

    if args.docs is True:
        ##check if there is any internet connection
        try:
            socket.setdefaulttimeout(3)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
            url = info.__website__
        ##if not we use the local documentation distributed along the software
        except:
            print('No internet connection detected, open local documentation')
            dir_path = os.path.dirname(os.path.realpath(__file__))
            url = os.path.join(dir_path, 'docs/build/html/index.html')

        for i in ['firefox', 'falkon', 'open', 'qupzilla', \
                'chromium', 'google-chrome']:
            ##we check if the command exist in the system
            exist = call(['which', i])
            if exist == 0:
                if i == 'firefox':
                    call([i, '--no-remote', url])
                    sys.exit()
                ##if it does then we use it to load the documentation
                else:
                    call([i, url])
                    ##and we stop the loop
                    sys.exit()
                break

    if args.test:
        tests.test()
        ###exit code
        sys.exit()

    ###get all the files
    list_files = get.get_files(args.file)

    if list_files == []:
        print('\n\033[1m[DFITSPY Error]>Invalid file name or no fits file found \033[0;0m')
        sys.exit()

    if args.list:
        ###get all keywords
        all_keywords = readfits.get_all_keyword(list_files[0])
        ###display them
        print('\n\033[1m[DFITSPY INFO]>keywords in %s \033[0;0m'%\
                os.path.basename(list_files[0]))
        dp.keywords_view(all_keywords)
        sys.exit()

    ##display number of files
    print('\n\033[1m[DFITSPY INFO]> Current directory: %s \033[0;0m'%os.getcwd())
    print('\033[1m[DFITSPY INFO]> %s fits files will be considered \033[0;0m\n'%len(list_files))

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
    allvalues = readfits.dfitsort(list_files, list_keys, grep)

    ##display them in terminal
    dp.dfitsort_view(allvalues)

    print('\n\033[1m[DFITSPY INFO]> %s files used in output \033[0;0m'%len(allvalues))
    if args.save:
        ###if we want to save the list of files into a file:
        with open('dfitspy_file_list.txt', 'w') as finalfile:
            finalfile.write('##file produced by dfitspy %s\n'%(datetime.datetime.now()))
            finalfile.write('##Current directory: %s\n'%os.getcwd())
            for i in allvalues.keys():
                finalfile.write('%s\n'%i)
        if os.path.isfile('dfitspy_file_list.txt'):
            print('\033[1m[DFITSPY INFO]> File saved: dfitspy_file_list.txt \033[0;0m')


if __name__ == "__main__":
    main()
