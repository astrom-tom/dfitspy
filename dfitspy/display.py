'''
dfitspy is a program aimed at reproducing the dfits program in python.
This file codes the display in the terminal

@place: ESO - La Silla - Paranal Observatory
@author(s): Romain Thomas
@year(s): 2018-2020
@First version: 19.9-0
@Current version: 20.7.0
@Telescope(s): ALL
@Instrument(s): ALL
@Documentation url:
@Last review [date + name]: 2020-07-21 - Romain Thomas
'''

###standrd imports
import os

##testing
import io
import unittest
import unittest.mock

###third party
import numpy

def dfitsort_view(values_dict):
    '''
    This function displays a-la-dfits the requested informations

    First we display the number of files that was found and then we
    display the header with keywords

    Parameters
    ----------
    values_dict : dictionnary
                keys=filename & values=dictionnary of keyword-value pair

    Returns
    -------
    None (prints in terminal)
    '''
    ###first we must make sure that there is an entry for each keywords for all the files
    ###get all keywords
    allkeys = []
    for i in values_dict:
        for k in values_dict[i].keys():
            allkeys.append(k)
    allkeys = numpy.unique(allkeys)

    ###then we add potential missing keywords to each file dictionary
    final_values_dict = {}
    for i in values_dict:
        for k in allkeys:
            if k not in values_dict[i].keys():
                values_dict[i][k] = '-'
        ###and finally make sure they are all in the right order
        ordered_dict = {} ###there are faster way to do it but requires latest python
        for j in sorted(allkeys):
            ordered_dict[j] = values_dict[i][j]
        final_values_dict[i] = ordered_dict


    ###and then we work on the display
    ###############get columns sizes
    ##1-filename
    filenames = list(final_values_dict.keys())
    if filenames:
        maxsize_filename = max([len(os.path.basename(i)) for i in filenames])

        ##2-keywords
        keys = list(final_values_dict[filenames[0]])
        header_keys_length = [len(i) for i in keys]
        keys_length = numpy.zeros((len(final_values_dict), len(keys)))
        for i in range(len(filenames)):
            for j in range(len(keys)):
                ###if the keyword is not founf we show it!
                if keys[j] not in final_values_dict[filenames[i]].keys():
                    final_values_dict[filenames[i]][keys[j]] = ' '

                keys_length[i][j] = len(str(final_values_dict[filenames[i]][keys[j]]))

        keys_length = keys_length.T
        length = [int(max(i)) for i in keys_length]

        ################prepare header
        ##create format
        form = ""
        form += "{:^%s}"%maxsize_filename
        #for i in length:
        for i, j in zip(length, header_keys_length):
            if i > j:
                form += "\t{:^%s}"%i
            else:
                form += "\t{:^%s}"%j
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
        for i in final_values_dict:
            linevalues = [os.path.basename(i)]
            values = list(final_values_dict[i].values())

            ##check if one line is missing a keyword
            ##and replace by 'Not FOUND'
            #if len(keys)-len(values) != 0:
            #    values += ['Not FOUND!'] * (len(keys)-len(values))
            allvalue = linevalues + values
            #print(allvalue)
            print(form.format(*allvalue))


def keywords_view(keywords):
    '''
    This function displays the list of keywords given in parameters.
    By default it displays it in a 3 columns display.

    Parameters
    ----------
    keywords : list
               list of keywords (each keyword is a string)

    Returns
    -------
    None (display in terminal)
    '''

    ##get the length of all the keywords
    length = [len(i) for i in keywords]

    print(80*'-')

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

class Testdisplaylist(unittest.TestCase):
    '''
    Class that test the display of the list of header keywords
    '''

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def displaylist(self, param, exp, mock_stdout):
        '''
        Function that run that actually run the test
        '''
        keywords_view(param)
        self.assertEqual(mock_stdout.getvalue(), exp)

    def test_three(self):
        '''
        Test if 3 keywords have to be displayed
        '''
        out1 = 80*'-'+'\n'
        out2 = 'A  | B  | C \n'
        out = out1 + out2
        self.displaylist(['A', 'B', 'C'], out)

    def test_four(self):
        '''
        idem with 4 keywords
        '''
        out1 = 80*'-'+'\n'
        out2 = 'A  | B  | C \n'
        out3 = 'D  | -  | - \n'
        out = out1 + out2 + out3
        self.displaylist(['A', 'B', 'C', 'D'], out)

    def test_five(self):
        '''
        idem with five
        '''
        out1 = 80*'-'+'\n'
        out2 = 'A  | B  | C \n'
        out3 = 'D  | E  | - \n'
        out = out1 + out2 + out3
        self.displaylist(['A', 'B', 'C', 'D', 'E'], out)

    def test_six(self):
        '''
        idem with six
        '''
        out1 = 80*'-'+'\n'
        out2 = 'A  | B  | C \n'
        out3 = 'D  | E  | F \n'
        out = out1 + out2 + out3
        self.displaylist(['A', 'B', 'C', 'D', 'E', 'F'], out)


class Testdisplayfinal(unittest.TestCase):
    '''
    Class that tests the final display function
    '''

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def displayfinal(self, param, exp, mock_stdout):
        '''
        Function that actually run the test
        '''
        dfitsort_view(param)
        self.assertEqual(mock_stdout.getvalue(), exp)

    def test_displayfinal(self):
        '''
        test the final display function
        '''
        out1 = '{:^9}\t{:^2}\t{:^2}\t{:^2}\n'.format(' filename ', 'AA', 'BB', 'CC')
        out2 = '{:^9}\t{:^2}\t{:^2}\t{:^2}\n'.format('----------', '--', '--', '--')
        out3 = '{:^9}\t{:^2}\t{:^2}\t{:^2}\n'.format('file1.fits', '1', '2', '3')
        out4 = '{:^9}\t{:^2}\t{:^2}\t{:^2}\n'.format('file2.fits', '3', '4', '5')
        out5 = '{:^9}\t{:^2}\t{:^2}\t{:^2}\n'.format('file3.fits', '3', '7', '7')
        out = out1 + out2 + out3 + out4+ out5
        dico = {'file1.fits': {'AA':1, 'BB':2, 'CC':3}, \
                'file2.fits': {'AA':3, 'BB':4, 'CC':5},\
                'file3.fits': {'AA':3, 'BB':7, 'CC':7}}
        self.displayfinal(dico, out)

    def test_displayfinal_missing_keyword(self):
        '''
        test the final display function when a keyword is missing for a file
        '''
        out1 = '{:^9}\t{:^2}\t{:^2}\t{:^2}\n'.format(' filename ', 'AA', 'BB', 'CC')
        out2 = '{:^9}\t{:^2}\t{:^2}\t{:^2}\n'.format('----------', '--', '--', '--')
        out3 = '{:^9}\t{:^2}\t{:^2}\t{:^2}\n'.format('file1.fits', '1', '-', '-')
        out4 = '{:^9}\t{:^2}\t{:^2}\t{:^2}\n'.format('file2.fits', '3', '-', '5')
        out5 = '{:^9}\t{:^2}\t{:^2}\t{:^2}\n'.format('file3.fits', '3', '7', '-')
        out = out1 + out2 + out3 + out4+ out5
        dico = {'file1.fits': {'AA':1}, \
                'file2.fits': {'AA':3, 'CC':5},\
                'file3.fits': {'AA':3, 'BB':7}}
        self.displayfinal(dico, out)
