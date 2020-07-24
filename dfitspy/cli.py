'''
---dfitspy---

dfitspy is a program aimed at reproducing the dfits program in python.
the functions can be used inside another program or it can also be called
as an executable

This file organises the command line interface (and nunit test it)

@place: ESO - La Silla - Paranal Observatory
@author(s): Romain Thomas
@year(s):  2018
@First version: 18.09-0
@Current version: 20.7.1
@Telescope(s): ALL
@Instrument(s): ALL
@Valid for SciOpsPy: v0.1-b
@Documentation url:
@Last SciOps review [date + name]: 18-09-2018 - Romain Thomas
@Usage: inside another code (dfitspy)
@Licence: GPL
@Testable: Yes
@Test data place (if any required): N.A.
'''


##standard library
import argparse

##testing
import unittest

#local import
from . import __info__ as info


def command_line(args):
    '''
    This function defines the command line interface of the program.
    It is used only if dfitspy is used as an executable

    Parameters
    -----------
    None

    Returns
    -------
    args    Namespace with arguments
    '''

    ##create parser object
    parser = argparse.ArgumentParser(description='dfitspy: dfits|fitsort in python, version %s, \
            Licence: GPL'%(info.__version__))

    mand = parser.add_argument_group("Mandatory arguments if you want to dfitsort your files")
    mand.add_argument('-file', nargs='*', help='a file, a list of file separated by coma,\
            *.fits is accepted, * as well, test* as well, testdir/test* as well')
    mand.add_argument('-key', help='Header keyword or list of header keywords\
            (separated by coma)')


    ###optional arguments
    #parser.add_argument('--dir', help='Directory where we search for files. \
    #        If none given, the default directory is the one from where dfitspy \
    #        is started.', default=os.getcwd())
    opt = parser.add_argument_group("Optional arguments")
    opt.add_argument('--list', help='List all keywords in a given file \
            (if a list of file is given the first one is used)', action='store_true')
    opt.add_argument('--grep', help='Restrain the files to the one with a given \
            value of a given parameter. It can be used multiple times with different values', \
            type=str, action='append')
    opt.add_argument('--exact', '-e', help='Consider only exact matches for keywords',
                     action='store_true')
    opt.add_argument('--HDU', '-H', help='HDU extension, default is 0 (primary header)', type=int, default=0) 
    opt.add_argument('--save', help='Save the list of files into an ascii file',\
            action='store_true')
    opt.add_argument('--test', help='Start the testing of the program', \
            action='store_true')
    opt.add_argument('--version', help='Display the version of the program', \
            action='version', version=info.__version__)
    opt.add_argument('--docs', help='Diplay the online or local documentation program', \
            action='store_true')

    ##create a group of arguments that are mandatory
    return parser.parse_args(args)



class Interfacetest(unittest.TestCase):
    '''
    Class that define the test for the command line interface
    '''
    def test_cli(self):
        '''
        This method tests the command line interface
        The principle is that we send some argument configuration
        and see what the interface is giving back
        '''
        options = command_line(['--grep', 'testobject',\
                                '--list', '--test'])
        self.assertEqual(options.grep, ['testobject'])
        self.assertEqual(options.list, True)
        self.assertEqual(options.test, True)

        options2 = command_line(['-file', '/home/file', \
                                 '-key', 'testkey'])
        self.assertEqual(options2.key, 'testkey')
        self.assertEqual(options2.file, ['/home/file'])
