'''
This file organises the tests of the library
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
