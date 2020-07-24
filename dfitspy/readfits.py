'''
This file organises and reads the FITS files
'''

###standard imports
import os
import warnings
import time

##testing
import unittest
import unittest.mock

###third party
from astropy.io import fits as pyfits
from astropy.io.fits.verify import VerifyWarning

warnings.simplefilter('ignore', category=VerifyWarning)

def read_fitsfile(thefile, HDU = 0):
    '''
    This function is largely inspired from the fitsio python library and used the
    python wrapper around the cFitsio library.
    It takes as argument the name (including path if the location of the file is different from the
    current folder) and returns a dictionnary of keyword = header keyword and value = header
    value.\n\n

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
    #header = FITS[HDU].header
    try:
        dict_values = pyfits.getheader(thefile, ext=HDU)
        keys = list(dict_values.keys())
    except IndexError:
        raise ValueError('HDU %s not in %s'%(HDU, os.path.basename(thefile)))

    ##and close the file
    #FITS.close()
    #print(dict_values)
    return dict_values, keys



def get_all_keyword(thefile, HDU = 0):
    '''
    This function gets all the keyword in the header of the file

    Parameters
    ----------
    thefile     str
                path/and/file.txt
    HDU         int
                FITS extension number to get the keywords from

    Returns
    -------
    keywords    list
                list of keywords (string)
    '''
    ##get header
    header,keys = read_fitsfile(thefile, HDU)

    ###and keywords
    #keywords = list(header.keys())

    return keys

def keywords_in_file(thefile, keyword, exact=False, extract=True, header={}):
    '''
    This function extracts in the thefile file the value
    of the keyword

    Parameter
    ---------
    thefile
                str, path/to/file.fits

    keyword
                str, keyword to get the value of

    exact       boolean, to consider only exact values of keywords
                         (instead of considering all keywords with
                          a given value)

    extract     boolean, if we need to re-extract the keywords

    dict_keys   dict, if extract=False, one must give a pre-extracted header

    return
    ------
    value
                str, value of the keyword inside the file
    '''
    if extract:
        ##get all keyword
        header, allkeys = read_fitsfile(thefile)

    dict_keys = {}
    if exact: ##we consider the keyword given by the user only
        match = [keyword]
        if keyword in header:
            dict_keys[keyword] = str(header[keyword]).strip()
    else: ## we check for all keywords containing the keyword requested
        ##strip the hierarch keyword:
        hierarch = 0
        if keyword.startswith('HIERARCH '):
            keyword = keyword.replace('HIERARCH ', '')
            hierarch = 1

        match = [i for i in list(header.keys()) if keyword in i]
        
        for i in match:
            ###we put back the HIERARCH
            key = i
            if i.startswith('ESO ') and hierarch==1:
                key = 'HIERARCH ' + i
            dict_keys[key] = str(header[i]).strip()

    return dict_keys


def dfitsort(listfiles, listkeys, exact=False, grepping=None, HDU = 0):
    '''
    This function get for all files, the value of all the keywords that are passed\n

    Parameters
    ----------
    listfiles : lisr
                list, with file names (string, path included)
    listkeys :  list
                list, of keywords (strings)
    grep : list
                list of string, if not false, the grepping valueS
                will be compared to all the values
                of the keywords. If all grepping values appear in the
                header of one file the file will be kept
    exact   : bool
              if the exact keyword from the user must be retrieved. If not,
              any keyword containing the requested keyword will be used.
    HDU     : int
              extension number to look in. Default is primary: 0

    Returns
    -------
    file_dict : dictionary
                dictionary, keys=filename & values=dictionnary of keyword-value pairs

    Examples
    --------
    dfitsort([file1, file2], [key1, key2]) <-- no grep\n
    dfitsort([file1, file2], [key1, key2], ['match', 'match2']) <-- multi grep
    '''

    file_dict = {}

    ##start to loop over the files
    for file in listfiles:
        ##and create a key dictionnary
        key_dict = {}
        header, allkeys = read_fitsfile(file, HDU)
        for key in listkeys:
            ###get the value
            value_dict = keywords_in_file(file, key, exact, False, header)

            ##append the value to the dictionnary
            for i in value_dict:
                key_dict[i] = value_dict[i]

        ##do the greeping
        if not grepping:
            file_dict[os.path.basename(file)] = key_dict
        else:
            ###we check at one if all the grepping values are
            ##in the file
            grepped = []
            for i in key_dict.values():
                for j in grepping:
                    k = j
                    #f '.' in j:
                    #    k = j.replace(".", " ")
                    #else:
                    #    k = j
                    if k in i:
                        grepped.append(j)

            #if set(grepping).issubset(key_dict.values()):
            if set(grepped) == set(grepping):
                file_dict[os.path.basename(file)] = key_dict

    return file_dict



class Testkeywordextraction(unittest.TestCase):
    '''
    This class is a testing class that deal with the extraction of the keywords inside
    the fits files
    '''

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
                    'COMMENT', 'COMMENT', 'NAME', 'YEAR',
                    'PLACE', 'AUTHOR']
        ###run the function
        keywords = get_all_keyword(filetest)
        ##compare the output and expected quantity
        self.assertEqual(keywords, expected)

    def test_get_value_true(self):
        '''
        This method tests the function that gets the value of the keyword in the file
        in the case the keyword exists
        '''
        ##get a test file
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filetest = os.path.join(dir_path, 'tests/test.fits')

        ##get the year
        v = keywords_in_file(filetest, 'YEAR')

        ##and compare expected value and output
        self.assertEqual(v, {'YEAR':'2018'})

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
        print(v)

        ##and compare expected value and output
        self.assertFalse(v)

    def test_get_value_no_grep(self):
        '''
        This function tests the extraction of keywords without grepping values
        '''
        ##get 2 test files
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filetest = os.path.join(dir_path, 'tests/test.fits')
        filetest2 = os.path.join(dir_path, 'tests/test2.fits')

        ###get all values
        allvalues = dfitsort([filetest, filetest2], ['YEAR', 'NAME'])

        ##expected values:
        expected = {'test.fits':{'YEAR':'2018', 'NAME':'dfitspy'}, \
                'test2.fits':{'YEAR':'2018', 'NAME':'dfitspy'}}

        self.assertEqual(expected, allvalues)

    def test_get_value_same_keyword_root(self):
        '''
        This function tests the extraction of keywords without grepping values
        when there are similar keywords
        '''
        ##get 2 test files
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filetest = os.path.join(dir_path, 'tests/test.fits')
        filetest2 = os.path.join(dir_path, 'tests/test2.fits')

        ###get all values
        allvalues = dfitsort([filetest, filetest2], ['NAXIS'])

        ##expected values:
        expected = {'test.fits':{'NAXIS': '2', 'NAXIS1': '4', 'NAXIS2': '1'},
                    'test2.fits':{'NAXIS': '2', 'NAXIS1': '4', 'NAXIS2': '1'}}

        self.assertEqual(expected, allvalues)

    def test_get_value_same_keyword_root_but_exact(self):
        '''
        This function tests the extraction of keywords without grepping values
        when there are similar keywords. But this time we force the keyword matching
        '''
        ##get 2 test files
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filetest = os.path.join(dir_path, 'tests/test.fits')
        filetest2 = os.path.join(dir_path, 'tests/test2.fits')

        ###get all values
        allvalues = dfitsort([filetest, filetest2], ['NAXIS'], exact=True)

        ##expected values:
        expected = {'test.fits':{'NAXIS': '2'},
                    'test2.fits':{'NAXIS': '2'}}

        self.assertEqual(expected, allvalues)



    def test_get_value_missing_keyword(self):
        '''
        This function tests the extraction of keywords without grepping values
        but with some missin keyword
        '''
        ##get 2 test files
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filetest = os.path.join(dir_path, 'tests/test.fits')
        filetest2 = os.path.join(dir_path, 'tests/test2.fits')
        filetest3 = os.path.join(dir_path, 'tests/test_extra_keyword.fits')

        ###get all values
        allvalues = dfitsort([filetest, filetest2, filetest3], ['YEAR', 'NAME', 'EXTRA'])

        ##expected values:
        expected = {'test.fits':{'YEAR':'2018', 'NAME':'dfitspy'},
                    'test2.fits':{'YEAR':'2018', 'NAME':'dfitspy'},
                    'test_extra_keyword.fits':{'YEAR':'201810', 'NAME':'dfitspy', 'EXTRA': 'extra keyword'}}

        self.assertEqual(expected, allvalues)

    def test_get_value_with_grep(self):
        '''
        Same as before but with grepping
        '''
        ##get 2 test files
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filetest = os.path.join(dir_path, 'tests/test.fits')
        filetest2 = os.path.join(dir_path, 'tests/test5.fits')

        ###get all values
        allvalues = dfitsort([filetest, filetest2], ['YEAR', 'NAME'], ['2018'])

        ##expected values (one out of the two files as year=2018)
        expected = {'test.fits':{'YEAR':'2018', 'NAME':'dfitspy'}, \
                   'test5.fits':{'YEAR':'201810', 'NAME':'dfitspy'}}

        self.assertEqual(expected, allvalues)

class Testextractheader(unittest.TestCase):
    '''
    This class tests the extraction of the header from the fits file
    '''
    def test_readfile(self):
        '''
        This function test the header extraction
        '''
        ##get the test file
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filetest = os.path.join(dir_path, 'tests/test.fits')
        ###run the function on the test file
        dict_value, keys = read_fitsfile(filetest)
        ##check if the header is the expected one
        dict_value = dict(dict_value)
        dict_value['COMMENT'] = str(dict_value['COMMENT'])
        exp = {'SIMPLE': True, 'BITPIX': -64, 'NAXIS': 2, 'NAXIS1': 4, \
                'NAXIS2': 1, 'EXTEND': True, 'COMMENT': "  FITS (Flexible Image Transport System) format"+\
                " is defined in 'Astronomy\n  and Astrophysics', volume 376, page 359; bibcode: 2001A&A...376..359H",
                'NAME': 'dfitspy', 'YEAR': '2018', 'PLACE': 'ESO Paranal', \
                'AUTHOR': 'Romain Thomas'}
        self.assertEqual(dict_value, exp)
