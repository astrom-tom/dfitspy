'''
---dfitspy---

dfitspy is a program aimed at reproducing the dfits program in python.
the functions can be used inside another program or it can also be called
as an executable

This file organises the tests of the library

@place: ESO - La Silla - Paranal Observatory
@author(s): Romain Thomas
@year(s):  2018
@First version: 18.09-0
@Current version: 18.10-0
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

#testing
import unittest

#local imports
from . import cli
from . import display
from . import readfits
from . import get_files_and_keys

def test():
    '''
    This function calls the test of each module and run them
    '''
    ###test the command line interface
    print('\n\033[1m---UnitTest the command interface\033[0;0m')
    suite = unittest.TestLoader().loadTestsFromModule(cli)
    unittest.TextTestRunner(verbosity=2).run(suite)

    ##test the display
    print('\n\033[1m---UnitTest the display printouts\033[0;0m')
    suite2 = unittest.TestLoader().loadTestsFromModule(display)
    unittest.TextTestRunner(verbosity=3).run(suite2)

    ##test the display
    print('\n\033[1m---UnitTest read fits and extraction functions\033[0;0m')
    suite3 = unittest.TestLoader().loadTestsFromModule(readfits)
    unittest.TextTestRunner(verbosity=3).run(suite3)

    ##test the display
    print('\n\033[1m---UnitTest getting file names\033[0;0m')
    suite4 = unittest.TestLoader().loadTestsFromModule(get_files_and_keys)
    unittest.TextTestRunner(verbosity=3).run(suite4)
