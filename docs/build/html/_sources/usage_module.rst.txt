.. _Usagecli:


|Python36| |Licence| |numpy|  

.. |Licence| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
      :target: http://perso.crans.org/besson/LICENSE.html

.. |Opensource| image:: https://badges.frapsoft.com/os/v1/open-source.svg?v=103
      :target: https://github.com/ellerbrock/open-source-badges/

.. |Python36| image:: https://img.shields.io/badge/python-3.6-blue.svg
.. _Python36: https://www.python.org/downloads/release/python-360/

.. |numpy| image:: https://img.shields.io/badge/poweredby-numpy-orange.svg
   :target: http://www.numpy.org/


dfitspy as a Python Module
==========================


dfitspy can be also used as a third party module in one of your own code. You can import it the usual way::

           In [1]: import dfitspy


dfitspy contains few functions that I will details below::

    get_all_keyword
    get_files
    get_keys
    keywords_in_file
    readfits
    test
    display_final
    display_list



If you want to dfits | fitsort inside your program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1 - Get your files ready
------------------------

dfitspy can be easily use to dfits|fitsio a set of files. First of all you must prepare a list of files. You can do it using your favorite python package. Or you can use the *get_files* function of dfitspy::

    In [1]: import dfitspy

    In [2]: help(dfitspy.get_files)  <---this print the help of the function

    get_files(files, dire)
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

This function takes two arguments. The first is the file argument and must be a **LIST** of strings. It will return a list of files. **Only fits files will be returned**. 

The easiest way is to analyse **all** the files in a directory::

    In [3]: listfiles = get_files(['all'],'/Test_data/')
    ['Test_data/r.XSHOO.2018-06-01T09:53:45.055_tpl-A02_0001.fits',
     'Test_data/r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0004.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:45.055_tpl-A01_0002.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:43.577_tpl-A02_0001.fits',
     'Test_data/r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0002.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:45.055_tpl-A02_0000.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:43.577_tpl-A01_0001.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:44.797_tpl-A03_0002.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:44.797_tpl-A03_0000.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:45.055_tpl-A03_0001.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:45.055_tpl-A02_0002.fits',
     'Test_data/r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0006.fits',
     'Test_data/r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0000.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:43.577_tpl-A02_0002.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:43.577_tpl-A01_0000.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:44.797_tpl-A01_0002.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:43.577_tpl-A03_0001.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:44.797_tpl-A01_0001.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:45.055_tpl-A01_0001.fits',
     'Test_data/r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0001.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:43.577_tpl-A03_0000.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:45.055_tpl-A01_0000.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:43.577_tpl-A03_0002.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:44.797_tpl-A02_0001.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:44.797_tpl-A03_0001.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:45.055_tpl-A03_0000.fits',
     'Test_data/r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0003.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:43.577_tpl-A02_0000.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:45.055_tpl-A03_0002.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:44.797_tpl-A02_0000.fits',
     'Test_data/r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0005.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:44.797_tpl-A01_0000.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:43.577_tpl-A01_0002.fits',
     'Test_data/r.XSHOO.2018-06-01T09:53:44.797_tpl-A02_0002.fits']

You would get the same results using::

    In [4]: listfiles = get_files(['*.fits'],'/Test_data/')


2 - Get your keywords ready
---------------------------

After preparing the files you must prepare the keywords you want to fitsort your files with. The correct format is a list of string, each string being a keyword, example::

    listkeys = ['OBJECT', 'LST', 'DATE']


If you do not remember the name of the keywords you want to use you can retrieve them all and display them::

    In [5]: help(dfitspy.get_all_keyword)

    get_all_keyword(thefile)
    This function gets all the keyword in the header of the file

    Parameter:
    ----------
    thefile
                str, path/and/file.txt

    Return
    ------
    keywords
                list, of keywords (string)


This function takes a file as input and return the list of all the keywords::

    In [6]: keys = dfitspy.get_all_keyword(listfiles[0])
    In [7]: keys

        ['SIMPLE',
     'BITPIX',
     'NAXIS',
     'EXTEND',
     'COMMENT',
     'DATE',
     'ORIGIN',
     'TELESCOP',
     'INSTRUME',
     'OBJECT',
     'MJD-OBS',
     'DATE-OBS',
     'PI-COI',
     'DATAMD5',
     'PIPEFILE',
     'RA',
     'DEC',
     'EQUINOX',
     'RADECSYS',
     'UTC',
     'LST'...........(cut for display convinience)]

If you have a very long list you can display it using the *display_list* function, which will cut the length by three::

    In [8] : dfitspy.display_list(keys)

    List of keywords in the first file
    ----------------------------------
    SIMPLE                        | BITPIX                        | NAXIS                        
    EXTEND                        | COMMENT                       | DATE                         
    ORIGIN                        | TELESCOP                      | INSTRUME                     
    OBJECT                        | MJD-OBS                       | DATE-OBS                     
    PI-COI                        | DATAMD5                       | PIPEFILE                     
    RA                            | DEC                           | EQUINOX                      
    RADECSYS                      | UTC                           | LST                          
    OBSERVER                      | ARCFILE                       | ESO OBS DID                  
    ESO OBS GRP                   | ESO OBS ID                    | ESO OBS NAME                 
    ESO OBS NTPL                  | ESO OBS PI-COI ID             | ESO OBS PI-COI NAME          
    .                             | .                             | .             
    .                             | .                             | .       
    .                             | .                             | .       
    (it has been cut)



3 - Fitsort your files
----------------------

At this point you are ready to fitsort all files. In order to achieve that you have to use the *get_all_values* function::

    In [9]: help(dfitspy.get_all_values)

    get_all_values(listfiles, listkeys, grepping=None)
    This function get for all files, the value of all the keywords that are passed

    example:  get_all_values([file1, file2], [key1, key2], 'match')

    Parameter
    ---------
    listfiles
                list, with file names (string, path included)
    listkeys
                list, of keywords (strings)
    grep
                string, by defaul is None. if not, the grepping value (a string!)
                        will be compared to all the values of the keywords and if one match
                        the file will be kept
    Return
    ------
    file_dict
                dictionnary, keys=filename
                             values=dictionnary of keyword-value pairs


This function takes as argument the list of file and the list of parameter and returns a dictionnary of files withe values of all the keywords required::

    In [10]: fitsort = dfitspy.get_all_values(listfiles, listkeys)

    In [11]: fitsort

    {'r.XSHOO.2018-06-01T09:53:45.055_tpl-A02_0001.fits': {'INSTRUME': 'XSHOOTER',
      'LST': '78685.247',
      'UTC': '35622.'},
     'r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0004.fits': {'INSTRUME': 'XSHOOTER',
      'LST': '79056.26',
      'UTC': '35992.'},
     'r.XSHOO.2018-06-01T09:53:45.055_tpl-A01_0002.fits': {'INSTRUME': 'XSHOOTER',
      'LST': '78685.247',
      'UTC': '35622.'},
     'r.XSHOO.2018-06-01T09:53:43.577_tpl-A02_0001.fits': {'INSTRUME': 'XSHOOTER',
      'LST': '78684.245',
      'UTC': '35621.'},
     'r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0002.fits': {'INSTRUME': 'XSHOOTER',
      'LST': '79056.26',
      'UTC': '35992.'},
     'r.XSHOO.2018-06-01T09:53:45.055_tpl-A02_0000.fits': {'INSTRUME': 'XSHOOTER',
      'LST': '78685.247',
      'UTC': '35622.'},
     'r.XSHOO.2018-06-01T09:53:43.577_tpl-A01_0001.fits': {'INSTRUME': 'XSHOOTER',
      'LST': '78684.245',
      'UTC': '35621.'},
     'r.XSHOO.2018-06-01T09:53:44.797_tpl-A03_0002.fits': {'INSTRUME': 'XSHOOTER',
      'LST': '78684.245',
      'UTC': '35621.'},
     'r.XSHOO.2018-06-01T09:53:44.797_tpl-A03_0000.fits': {'INSTRUME': 'XSHOOTER',
      'LST': '78684.245',
      'UTC': '35621.'},
      .
      .
      .}
    

you can display everything in a nice way using the *display_final* function::

    In [12]: dfitspy.display_final(fitsort)

    filename                                         	INSTRUME	LST      	UTC
    -------------------------------------------------	--------	---------	------
    r.XSHOO.2018-06-01T09:53:45.055_tpl-A02_0001.fits	XSHOOTER	78685.247	35622.
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0004.fits	XSHOOTER	79056.26 	35992.
    r.XSHOO.2018-06-01T09:53:45.055_tpl-A01_0002.fits	XSHOOTER	78685.247	35622.
    r.XSHOO.2018-06-01T09:53:43.577_tpl-A02_0001.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0002.fits	XSHOOTER	79056.26 	35992.
    r.XSHOO.2018-06-01T09:53:45.055_tpl-A02_0000.fits	XSHOOTER	78685.247	35622.
    r.XSHOO.2018-06-01T09:53:43.577_tpl-A01_0001.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:44.797_tpl-A03_0002.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:44.797_tpl-A03_0000.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:45.055_tpl-A03_0001.fits	XSHOOTER	78685.247	35622.
    r.XSHOO.2018-06-01T09:53:45.055_tpl-A02_0002.fits	XSHOOTER	78685.247	35622.
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0006.fits	XSHOOTER	79056.26 	35992.
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0000.fits	XSHOOTER	79056.26 	35992.
    r.XSHOO.2018-06-01T09:53:43.577_tpl-A02_0002.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:43.577_tpl-A01_0000.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:44.797_tpl-A01_0002.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:43.577_tpl-A03_0001.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:44.797_tpl-A01_0001.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:45.055_tpl-A01_0001.fits	XSHOOTER	78685.247	35622.
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0001.fits	XSHOOTER	79056.26 	35992.
    r.XSHOO.2018-06-01T09:53:43.577_tpl-A03_0000.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:45.055_tpl-A01_0000.fits	XSHOOTER	78685.247	35622.
    r.XSHOO.2018-06-01T09:53:43.577_tpl-A03_0002.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:44.797_tpl-A02_0001.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:44.797_tpl-A03_0001.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:45.055_tpl-A03_0000.fits	XSHOOTER	78685.247	35622.
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0003.fits	XSHOOTER	79056.26 	35992.
    r.XSHOO.2018-06-01T09:53:43.577_tpl-A02_0000.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:45.055_tpl-A03_0002.fits	XSHOOTER	78685.247	35622.
    r.XSHOO.2018-06-01T09:53:44.797_tpl-A02_0000.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0005.fits	XSHOOTER	79056.26 	35992.
    r.XSHOO.2018-06-01T09:53:44.797_tpl-A01_0000.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:43.577_tpl-A01_0002.fits	XSHOOTER	78684.245	35621.
    r.XSHOO.2018-06-01T09:53:44.797_tpl-A02_0002.fits	XSHOOTER	78684.245	35621.


4 - Grepping
------------

The last function allows you to grep files that have a certain value in their keywords.
By default it is set to *None* but you can give a *grepping value* (**a string**) to replace it. When doing so dfitspy will look at all the files you give in listfiles and in all the keywords you give in listkeys. **If one of the value of the keywords matches the grepping value the file will be kept, if not the file will be rejected.** For example here we want all the files for which LST = 79056.26 ::

    In [13]: fitsortgrep = dfitspy.get_all_values(listfiles, listkeys, '79056.26')

    In [14]: dfitspy.display_final(fitsortgrep)

    filename                                         	INSTRUME	LST     	UTC
    -------------------------------------------------	--------	--------	------
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0004.fits	XSHOOTER	79056.26	35992.
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0002.fits	XSHOOTER	79056.26	35992.
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0006.fits	XSHOOTER	79056.26	35992.
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0000.fits	XSHOOTER	79056.26	35992.
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0001.fits	XSHOOTER	79056.26	35992.
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0003.fits	XSHOOTER	79056.26	35992.
    r.XSHOO.2018-06-01T09:59:57.509_tpl-A01_0005.fits	XSHOOTER	79056.26	35992.

 
Test
^^^^

Dfitspy comes with a unit testing suite (21 tests in total). To run it::

    In [1]: import dfitspy
    In [2]: dfitspy.test()

        ---UnitTest the command interface
    test_cli (dfitspy.cli.interface_test) ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 0.002s

    OK

    ---UnitTest the display printouts
    test_displayfinal (dfitspy.display.Testdisplay_final) ... ok
    test_five (dfitspy.display.Testdisplay_list) ... ok
    test_four (dfitspy.display.Testdisplay_list) ... ok
    test_six (dfitspy.display.Testdisplay_list) ... ok
    test_three (dfitspy.display.Testdisplay_list) ... ok

    ----------------------------------------------------------------------
    Ran 5 tests in 0.001s

    OK

    ---UnitTest read fits and extraction functions
    test_readfile (dfitspy.readfits.Test_extractheader) ... ok
    test_get_all_keyword (dfitspy.readfits.Testkeyword_extraction) ... ok
    test_get_value_True (dfitspy.readfits.Testkeyword_extraction) ... ok
    test_get_value_no_grep (dfitspy.readfits.Testkeyword_extraction) ... ok
    test_get_value_with_grep (dfitspy.readfits.Testkeyword_extraction) ... ok
    test_get_value_wrong (dfitspy.readfits.Testkeyword_extraction) ... ok

    ----------------------------------------------------------------------
    Ran 6 tests in 0.002s

    OK

    ---UnitTest getting file names
    test_get_file_all_no_files (dfitspy.get_files_and_keys.Testgetfiles) ... ok
    test_get_file_all_with_files (dfitspy.get_files_and_keys.Testgetfiles) ... ok
    test_get_files_allfits (dfitspy.get_files_and_keys.Testgetfiles) ... ok
    test_get_multi_file_goodname (dfitspy.get_files_and_keys.Testgetfiles) ... ok
    test_get_single_file_goodname (dfitspy.get_files_and_keys.Testgetfiles) ... ok
    test_get_single_file_wrongname (dfitspy.get_files_and_keys.Testgetfiles) ... ok
    test_list_files (dfitspy.get_files_and_keys.Testgetfiles) ... ok
    test_get_multi_key (dfitspy.get_files_and_keys.Testgetkeys) ... ok
    test_get_single_key (dfitspy.get_files_and_keys.Testgetkeys) ... ok

    ----------------------------------------------------------------------
    Ran 9 tests in 0.001s

    OK


