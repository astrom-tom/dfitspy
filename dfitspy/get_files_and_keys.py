'''
---dfitspy---

dfitspy is a program aimed at reproducing the dfits program in python.
the functions can be used inside another program or it can also be called
as an executable

This file create the file list depending on the user input as well as the keywords input

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

###standrd imports
import os
import glob

##testing
import unittest
import unittest.mock


def get_files(files, dire):
    '''
    This function extracts the list of files based on the files
    and dire parameters.

    example: get_files(['fil1.fits,file2.fits'] , '/home/Documents')


    Parameter
    ---------
    files
                list of str, list of files names (without path)
                             it can be ['file1.fits,file2.fits,....']
                                       ['file1.fits']
                                       ['file1,fits', 'file2.fits']
                                       ['*.fits']
                                       ['all']
    dire
                str, path of the directory to look in

    Return
    ------
    list of files
    '''
    ###first solution, user want to look at all fits file in the directory
    if files == ['*.fits']:
        allfiles = []
        for j in os.listdir(dire):
            if j.endswith(".fits"):
                allfiles.append(os.path.join(dire, j))

    ##second option, a list is given, need to check if some are fits file
    elif len(files) > 1:
        allfiles = []
        for k in files:
            if k.endswith(".fits"):
                allfiles.append(k)

    ##third option the user wants to look at all the files in the directory
    elif files == ['all']:
        allfiles = []
        files_path = [os.path.join(dire, i) for i in os.listdir(dire)]
        for k in files_path:
            if k.endswith(".fits"):
                allfiles.append(k)

    else:
        ##last solution, the user gives a files or a list of files
        ##we split it by coma
        #print('ok')
        splits = files[0].split(',')
        allfiles = [os.path.join(dire, i.strip()) for i in splits if \
                os.path.join(dire, i).endswith(".fits")]

    return allfiles

def get_keys(key_string):
    '''
    This function extract from a string the list of keys

    Parameter
    ---------
    keystring
                string, keys to be requested by user
                        ex: SEEING
                            SEEING,AIRMASS
                            SEEING,ARIMASS,OBID

    Return
    ------
    keys
            list, list of keys (string)
    '''

    keys = [i.strip() for i in key_string.split(',')]
    return keys


class Testgetkeys(unittest.TestCase):
    '''
    Class that tests the keyword relative functions
    '''
    def test_get_single_key(self):
        '''
        We give a single keyword and have to get exaclty the same
        keyword contained in a list
        '''
        key = 'OBJECT'
        out = get_keys(key)
        self.assertEqual([key], out)

    def test_get_multi_key(self):
        '''
        We give three keywords and have to get the three keywords
        contained in a list
        '''
        key = 'OBJECT,STR,SEEING'
        out = get_keys(key)
        self.assertEqual(['OBJECT', 'STR', 'SEEING'], out)


class Testgetfiles(unittest.TestCase):
    '''
    Class that tests the get file function
    '''

    def test_get_file_all_no_files(self):
        '''
        Here we test the get_files function when the user does not precise the
        directory (<--> look current directory), ask for all file and does not get any
        file in return (no fits file)
        '''
        ##the current directory here is set at the directory of the program
        files = get_files(['all'], os.path.dirname(os.path.realpath(__file__)))
        ##we are not expecting any fits file to be found
        self.assertEqual(files, [])

    def test_get_file_all_with_files(self):
        '''
        Here we test the get_files function when the user does not precise the
        directory (<--> look current directory), ask for all file and does get file
        file in return
        '''
        ##the current directory here is set at the directory of the program
        files = get_files(['all'], os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                'tests'))
        ##we are expecting 4 files to be found
        ##for convinience here we just compare the file name (without paths)
        files = [os.path.basename(i) for i in files]
        expected_files = ['test.fits', 'test5.fits', 'test2.fits', 'test4.fits', 'test3.fits']
        self.assertEqual(files, expected_files)

    def test_get_files_allfits(self):
        '''
        Test the *.fits function
        '''
        ##the current directory here is set at the directory of the program
        files = get_files(['*.fits'], os.path.join(os.path.dirname(os.path.realpath(__file__)), \
                'tests'))
        ##we are expecting 4 files to be found
        ##for convinience here we just compare the file name (without paths)
        files = [os.path.basename(i) for i in files]
        expected_files = ['test.fits', 'test5.fits', 'test2.fits', 'test4.fits', 'test3.fits']
        self.assertEqual(files, expected_files)

    def test_get_single_file_wrongname(self):
        '''
        Test with single file when a wrong filename is given
        '''
        ##the current directory here is set at the directory of the program
        ##which is here useless
        ##we give a wrong file name (no fits)
        files = get_files(['single'], os.path.join(os.path.dirname(os.path.realpath(__file__)),\
                'tests'))
        ##we are expecting no file to be found
        self.assertEqual(files, [])

    def test_get_single_file_goodname(self):
        '''
        Test with single file when a good filename is given
        '''
        ##the current directory here is set at the directory of the program
        ##which is here useless
        ##we give a wrong file name (no fits)
        files = get_files(['test.fits'], os.path.join(os.path.dirname(os.path.realpath(__file__)),\
                'tests'))
        ##we are expecting no file to be found
        self.assertEqual([os.path.basename(files[0])], ['test.fits'])

    def test_get_multi_file_goodname(self):
        '''
        Test for multiple files
        '''
        ##the current directory here is set at the directory of the program
        ##which is here useless
        ##we give a wrong file name (no fits)
        files = get_files(['test.fits,test2.fits,test3.fits'], \
                os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tests'))
        ##we are expecting 3 files to be found
        #we only take basenames for convinience
        files = [os.path.basename(i) for i in files]
        self.assertEqual(files, ['test.fits', 'test2.fits', 'test3.fits'])

    def test_list_files(self):
        '''
        Test for list of files as input
        '''
        inputlist = ['test.fits', 'test5.fits', 'test2.fits', 'test4.fits', 'test3.fits']
        files = get_files(inputlist, os.path.join(os.path.dirname(os.path.realpath(__file__)),\
                'tests'))
        self.assertEqual(files, inputlist)
 
if __name__ == "__main__": 
    unittest.main(verbosity=3)
