'''
---dfitspy---

dfitspy is a program aimed at reproducing the dfits program in python.
the functions can be used inside another program or it can also be called
as an executable

This file organises the terminal display of the output od the code, if used
as an executable

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

def display_final(values_dict):
    '''
    This function displays a-la-dfits the requested informations

    First we display the number of files that was found
    Then we display the header with keywords

    Parameter
    ---------
    values_dict
                dictionnary, keys=filename
                             values=dictionnary of keyword-value pair

    Return
    ------
    None
    '''
    ###############get columns sizes
    ##1-filename
    filenames = list(values_dict.keys())
    maxsize_filename = max([len(os.path.basename(i)) for i in filenames])

    ##2-keywords
    keys = list(values_dict[filenames[0]])
    header_keys_length = [len(i) for i in keys]
    keys_length = numpy.zeros((len(values_dict), len(keys)))
    for i in range(len(filenames)):
        for j in range(len(keys)):
            keys_length[i][j] = len(str(values_dict[filenames[i]][keys[j]]))

    keys_length = keys_length.T
    length = [int(max(i)) for i in keys_length]

    ################prepare header
    ##create format
    form = ""
    form += "{:%s}"%maxsize_filename
    #for i in length:
    for i, j in zip(length, header_keys_length):
        if i > j:
            form += "\t{:%s}"%i
        else:
            form += "\t{:%s}"%j
    form += ""

    #header
    header = form.format('filename', *keys)

    #separation
    sep = maxsize_filename*"-"
    for i, j in zip(length, header_keys_length):
        if i > j:
            sep += '\t'+i*"-"
        else:
            sep += '\t'+j*"-"

    ##print them
    print(header)
    print(sep)
    ##and print all values
    for i in values_dict:
        linevalues = [os.path.basename(i)]
        values = list(values_dict[i].values())
        allvalue = linevalues + values
        print(form.format(*allvalue))


def display_list(keywords):
    '''
    This function displays the list of keywords given in parameters
    By default it displays it in a 3 columns display :

    1   2   3
    4   5   6
    .   .   .
    .   .   .

    Parameters
    ----------
    keywords
                list of keywords (string)

    Return
    ------
    None (display in terminal)
    '''

    ##get the length of all the keywords
    length = [len(i) for i in keywords]

    print('List of keywords in the first file')
    print(34*'-')

    ##define the format of the output
    form = "{:%s} | {:%s} | {:%s}"%(max(length)+1, max(length)+1, max(length)+1)

    i = 0
    while i < len(keywords):

        if i < len(keywords)-2:
            one = keywords[i]
            two = keywords[i+1]
            three = keywords[i+2]

        elif i == len(keywords) - 2:
            one = keywords[i]
            two = keywords[i+1]
            three = '-'

        elif i == len(keywords) - 1:
            one = keywords[i]
            two = '-'
            three = '-'

        line = form.format(one, two, three)
        print(line)
        i += 3

class Testdisplay_list(unittest.TestCase):
    '''
    Class that test the display of the list of header keywords
    '''

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def displaylist(self, param, exp, mock_stdout):
        '''
        Function that run that actually run the test
        '''
        display_list(param)
        self.assertEqual(mock_stdout.getvalue(), exp)

    def test_three(self):
        '''
        Test if 3 keywords have to be displayed
        '''
        out1 = 'List of keywords in the first file\n'
        out2 = '----------------------------------\n'
        out3 = 'A  | B  | C \n'
        out = out1 + out2 + out3
        self.displaylist(['A', 'B', 'C'], out)

    def test_four(self):
        '''
        idem with 4 keywords
        '''
        out1 = 'List of keywords in the first file\n'
        out2 = '----------------------------------\n'
        out3 = 'A  | B  | C \n'
        out4 = 'D  | -  | - \n'
        out = out1 + out2 + out3 + out4
        self.displaylist(['A', 'B', 'C', 'D'], out)

    def test_five(self):
        '''
        idem with five
        '''
        out1 = 'List of keywords in the first file\n'
        out2 = '----------------------------------\n'
        out3 = 'A  | B  | C \n'
        out4 = 'D  | E  | - \n'
        out = out1 + out2 + out3 + out4
        self.displaylist(['A', 'B', 'C', 'D', 'E'], out)

    def test_six(self):
        '''
        idem with six
        '''
        out1 = 'List of keywords in the first file\n'
        out2 = '----------------------------------\n'
        out3 = 'A  | B  | C \n'
        out4 = 'D  | E  | F \n'
        out = out1 + out2 + out3 + out4
        self.displaylist(['A', 'B', 'C', 'D', 'E', 'F'], out)


class Testdisplay_final(unittest.TestCase):
    '''
    Class that tests the final display function
    '''

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def displayfinal(self, param, exp, mock_stdout):
        '''
        Function that actually run the test
        '''
        display_final(param)
        self.assertEqual(mock_stdout.getvalue(), exp)

    def test_displayfinal(self):
        '''
        test the final display function
        '''
        out1 = 'filename  	AA	BB	CC\n'
        out2 = '----------	--	--	--\n'
        out3 = 'file1.fits	 1	 2	 3\n'
        out4 = 'file2.fits	 3	 4	 5\n'
        out5 = 'file3.fits	 3	 7	 7\n'
        out = out1 + out2 + out3 + out4+ out5
        dico = {'file1.fits': {'AA':1, 'BB':2, 'CC':3}, \
                'file2.fits': {'AA':3, 'BB':4, 'CC':5},\
                'file3.fits': {'AA':3, 'BB':7, 'CC':7}}
        self.displayfinal(dico, out)
