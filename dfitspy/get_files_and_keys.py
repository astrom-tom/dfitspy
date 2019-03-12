'''
This file creates the filelist depending on the user input as well as the keywords input
'''

###standard imports
import os

##testing
import unittest
import unittest.mock


def get_files(files, dire=False):
    '''
    This function extracts the list of files based on the files
    and dire parameter.

    example: get_files(['fil1.fits,file2.fits'] , '/home/Documents')
    example: get_files(['fil1.fits,file2.fits'])


    Parameters
    ----------
    files : list of str
            list of files names (without path), it can be:\n
            ['file1.fits,file2.fits,....']\n
            ['file1.fits']\n
            ['file1,fits', 'file2.fits']\n
            ['all']\n
    dire :  str 
            path of the directory to look in

    Returns
    -------
    allfiles : list 
                list of all the files
    '''

    ##if no directory was given, we assume the current working directory
    if not dire:
        dire = os.getcwd()

    ##A list is given, need to check if some are fits file
    if len(files) > 1:
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
        splits = files[0].split(',')
        allfiles = [os.path.join(dire, i.strip()) for i in splits if \
                os.path.join(dire, i).endswith(".fits")]

    return allfiles

def get_keys(key_string):
    '''
    This function extracts from a string the list of keys

    Parameters
    ----------
    keystring : string
                keys to be requested by user, example:\n
                \tSEEING\n
                \tSEEING,AIRMASS\n
                \tSEEING,ARIMASS,OBID\n
                if a string contains dots, e.g, ESO.SEQ.ARM it will be
                transform to ESO SEQ ARM (with spaces)

    Returns
    -------
    keys : list
           list of keys (string)
    '''

    keys = [i.strip().replace('.', ' ') for i in key_string.split(',')]
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
        expected_files = set(['test.fits', 'test5.fits', 'test2.fits', 'test4.fits', 'test3.fits'])
        self.assertEqual(set(files), expected_files)

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
        files = [os.path.basename(i) for i in files]
        self.assertEqual(files, inputlist)

if __name__ == "__main__":
    unittest.main(verbosity=3)
