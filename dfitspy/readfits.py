'''
---dfitspy---

dfitspy is a program aimed at reproducing the dfits program in python.
the functions can be used inside another program or it can also be called
as an executable

This file organises reads the fits files

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

##testing
import io
import unittest
import unittest.mock

###third party
import numpy

###local import
from . import _fitsio_wrap


def read_fitsfile(thefile):
    '''
    This function is largely inspired from the fitsio python library and used the
    python wrapper around the cFitsio library.
    It takes as argument the name (including path if the location of the file is different from the
    current folder) and returns a dictionnary of keyword = header keyword and value = header value.


    WARNING: in the ESO fits header format, the HIERARCH prefix will be ignored by this function
             and the resulting dictionnary will not contain the HIERARCH prefix.
             Ex: 'HIERARCH ESO TEL ALT' will become 'ESO TEL ALT'

    Parameter
    ----------
    filename
                str,  path/to/file (fits file)

    Return
    ------
    dict_values
                python dictionnary with header keywords/value pairs.

    '''
    ###open the fits file
    FITS = _fitsio_wrap.FITS(thefile, 0, 0)

    ##read header (a is a dicytionnary but with two much imformation)
    a = FITS.read_header(1)

    ###open empty dictionnary to save the header
    dict_values = {}

    ###loop over the header
    for i in a:
        n = i['name']
        v = i['value']
        if len(v) > 2 and v[0] == "'" and v[-1] == "'":
            v = v[1:-1]
        dict_values[n] = v

    ##and close the file
    FITS.close()
    return dict_values



def get_all_keyword(thefile):
    '''
    This function gets all the keyword in the header of the file

    Parameter:
    ----------
    thefile
                str, path/and/file.txt

    Return
    ------
    keywords
                list, of keywords (string)
    '''
    ##get header
    header = read_fitsfile(thefile)

    ###and keywords
    keywords = list(header.keys())

    return keywords

def keywords_in_file(thefile, keyword):
    '''
    This function extract in the thefile file the value
    of the keyword

    Parameter
    ---------
    thefile
                str, path/to/file.fits

    keyword
                str, keyword to get the value of

    return
    ------
    value
                str, value of the keyword inside the file
    '''

    ##get all keyword
    header = read_fitsfile(thefile)

    if keyword in list(header.keys()):
        value = str(header[keyword])
    else:
        value = ''

    return value.strip()


def get_all_values(listfiles, listkeys, grepping=None):
    '''
    This function get for all files, the value of all the keywords that are passed

    example:  get_all_values([file1, file2], [key1, key2]) <-- no grep
    example:  get_all_values([file1, file2], [key1, key2], 'match') <--grep 

    Parameter
    ---------
    listfiles
                list, with file names (string, path included)
    listkeys
                list, of keywords (strings)
    grep
                string, if not false, the grepping value 
                        will be compared to all the values 
                        of the keywords and if one match 
                        the file will be kept
    Return
    ------
    file_dict
                dictionnary, keys=filename
                             values=dictionnary of keyword-value pairs
    '''

    file_dict = {}

    ##start to loop over the files
    for file in listfiles:
        ##and create a key dictionnary
        key_dict = {}
        save = 'ok'
        for key in listkeys:
            ###get the value
            value = keywords_in_file(file, key)
            ##append the value to the dictionnary
            key_dict[key] = value

    
        ##do the greeping
        if not grepping:
            file_dict[os.path.basename(file)] = key_dict
        else:
            if grepping in key_dict.values():
                file_dict[os.path.basename(file)] = key_dict


    return file_dict



class Testkeyword_extraction(unittest.TestCase):

    def test_get_all_keyword(self):
        '''
        This function test function that extracts all the keyword of the header
        '''
        ##get a test file
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filetest = os.path.join(dir_path, 'tests/test.fits')

        ###expected header keyword:
        expected = ['SIMPLE', 'BITPIX', 'NAXIS', \
                    'NAXIS1', 'NAXIS2', 'EXTEND', \
                    'COMMENT', 'NAME', 'YEAR', 
                    'PLACE', 'AUTHOR']
        ###run the function
        keywords = get_all_keyword(filetest)
        ##compare the output and expected quantity
        self.assertEqual(keywords, expected)
         
    def test_get_value_True(self):
        '''
        This function test function that gets the value of the keyword in the file
        in the case the keyword exists
        '''
        ##get a test file
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filetest = os.path.join(dir_path, 'tests/test.fits')

        ##get the year
        v = keywords_in_file(filetest, 'YEAR')
        
        ##and compare expected value and output
        self.assertEqual(v, '2018')
        
    def test_get_value_wrong(self):
        '''
        This function test function that gets the value of the keyword in the file
        in the case the keyword does not exist
        '''
        ##get a test file
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filetest = os.path.join(dir_path, 'tests/test.fits')

        ##get the year
        v = keywords_in_file(filetest, 'YEARS')
        
        ##and compare expected value and output
        self.assertEqual(v, '')

    def test_get_value_no_grep(self):
        ##get 2 test files
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filetest = os.path.join(dir_path, 'tests/test.fits')
        filetest2 = os.path.join(dir_path, 'tests/test2.fits')

        ###get all values
        allvalues = get_all_values([filetest, filetest2], ['YEAR', 'NAME'], False)

        ##expected values:
        expected = {'test.fits':{'YEAR':'2018','NAME':'dfitspy'}, 'test2.fits':{'YEAR':'2018', 'NAME':'dfitspy'}}

        self.assertEqual(expected, allvalues)

    def test_get_value_with_grep(self):
        ##get 2 test files
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filetest = os.path.join(dir_path, 'tests/test.fits')
        filetest2 = os.path.join(dir_path, 'tests/test5.fits')

        ###get all values
        allvalues = get_all_values([filetest, filetest2], ['YEAR', 'NAME'], '2018')

        ##expected values (one out of the two files as year=2018)
        expected = {'test.fits':{'YEAR':'2018','NAME':'dfitspy'}}

        self.assertEqual(expected, allvalues)

class Test_extractheader(unittest.TestCase):
    def test_readfile(self):
        ##get the test file
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filetest = os.path.join(dir_path, 'tests/test.fits')
        ###run the function on the test file
        dict_value = read_fitsfile(filetest)
        ##check if the header is the expected one
        exp = {'SIMPLE': 'T', 'BITPIX': '-64', 'NAXIS': '2', 'NAXIS1': '4', \
                'NAXIS2': '1', 'EXTEND': 'T', 'COMMENT': '', \
                'NAME': 'dfitspy ', 'YEAR': '2018    ', 'PLACE': 'ESO Paranal', \
                'AUTHOR': 'Romain Thomas'}
        self.assertEqual(dict_value, exp) 
