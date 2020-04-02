'''
This file organises and reads the FITS files
'''

###standard imports
import os

##testing
import unittest
import unittest.mock

###third party
import fitsio._fitsio_wrap as _fitsio_wrap

def read_fitsfile(thefile):
    '''
    This function is largely inspired from the fitsio python library and used the
    python wrapper around the cFitsio library.
    It takes as argument the name (including path if the location of the file is different from the
    current folder) and returns a dictionnary of keyword = header keyword and value = header value.\n\n

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
        if i['card_string'][:8] == 'HIERARCH':
            prefix = 'HIERARCH '
        else:
            prefix = ''
        n = prefix + i['name'] 
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

    Parameters
    ----------
    thefile     str
                path/and/file.txt

    Returns
    -------
    keywords    list
                list of keywords (string)
    '''
    ##get header
    header = read_fitsfile(thefile)

    ###and keywords
    keywords = list(header.keys())

    return keywords

def keywords_in_file(thefile, keyword, extract=True, header={}):
    '''
    This function extracts in the thefile file the value
    of the keyword

    Parameter
    ---------
    thefile
                str, path/to/file.fits

    keyword
                str, keyword to get the value of

    extract     boolean, if we need to re-extract the keywords
    
    dict_keys   dict, if extract=False, one must give a pre-extracted header

    return
    ------
    value
                str, value of the keyword inside the file
    '''
    if extract:
        ##get all keyword
        header = read_fitsfile(thefile)

    ###check for keywords containing the keyword requested
    match = [i for i in list(header.keys()) if keyword in i]

    dict_keys = {}

    for i in match:
        dict_keys[i] = header[i].strip()

    #if keyword in list(header.keys()):
    #    value = str(header[keyword])
    #else:
    #    value = ''

    return dict_keys


def dfitsort(listfiles, listkeys, grepping=None):
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
        header = read_fitsfile(file)
        for key in listkeys:
            ###get the value
            value_dict = keywords_in_file(file, key, False, header)
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
                    'COMMENT', 'NAME', 'YEAR',
                    'PLACE', 'AUTHOR']
        ###run the function
        keywords = get_all_keyword(filetest)
        ##compare the output and expected quantity
        self.assertEqual(keywords, expected)

    def test_get_value_true(self):
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
        allvalues = dfitsort([filetest, filetest2], ['YEAR', 'NAME'], False)

        ##expected values:
        expected = {'test.fits':{'YEAR':'2018', 'NAME':'dfitspy'}, \
                'test2.fits':{'YEAR':'2018', 'NAME':'dfitspy'}}

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
        dict_value = read_fitsfile(filetest)
        ##check if the header is the expected one
        exp = {'SIMPLE': 'T', 'BITPIX': '-64', 'NAXIS': '2', 'NAXIS1': '4', \
                'NAXIS2': '1', 'EXTEND': 'T', 'COMMENT': '', \
                'NAME': 'dfitspy ', 'YEAR': '2018    ', 'PLACE': 'ESO Paranal', \
                'AUTHOR': 'Romain Thomas'}
        self.assertEqual(dict_value, exp)
