.. _Usagecli:


|JOSS| |Python36| |Licence|

.. |JOSS| image:: http://joss.theoj.org/papers/10.21105/joss.01249/status.svg
   :target: https://doi.org/10.21105/joss.01249

.. |Licence| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
      :target: http://perso.crans.org/besson/LICENSE.html

.. |Opensource| image:: https://badges.frapsoft.com/os/v1/open-source.svg?v=103
      :target: https://github.com/ellerbrock/open-source-badges/

.. |Python36| image:: https://img.shields.io/badge/python-3.6-blue.svg
.. _Python36: https://www.python.org/downloads/release/python-360/


dfitspy as a Python Module
==========================


dfitspy can be also used as a third party module in one of your own code. You can import it the usual way::

           In [1]: import dfitspy


dfitspy contains a few functions that I detail below::

    get_all_keyword
    get_files
    get_keys
    keywords_view
    keywords_in_file
    dfitsort
    dfitsort_view
    test
    version



If you want to dfits | fitsort inside your program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1 - Get your files ready
------------------------

dfitspy can be easily use to dfits|fitsio a set of files. First of all you must prepare a list of files. You can do it using your favorite python package. Or you can use the *get_files* function of dfitspy::

    In [1]: import dfitspy

    In [2]: help(dfitspy.get_files)  <---this print the help of the function

    get_files(files, dire=False)
    This function extracts the list of files based on the files
    and dire parameters.
    
    example: get_files(['fil1.fits,file2.fits'] , '/home/Documents')
    example: get_files(['fil1.fits,file2.fits'])
    
    
    Parameter
    ---------
    files
                list of str, list of files names (without path)
                             it can be ['file1.fits,file2.fits,....']
                                       ['file1.fits']
                                       ['file1,fits', 'file2.fits']
                                       ['all']
    dire
                str, path of the directory to look in
    
    Return
    ------
    list of files


This function takes two arguments. The first is the file argument and must be a **LIST** of strings. It will return a list of files. **Only fits files will be returned**. 

The easiest way is to analyse **all** the files in a directory::

    In [3]: listfiles = dfitspy.get_files(['all'],'Test_data/')
    ['/run/media/romain/Test_Data/r.NACO.2919-99-04T21:42:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-04T21:11:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T03:26:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-04T22:03:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-04T21:11:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-05T01:01:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.KMOS.2919-99-05T03:50:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-05T04:25:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.KMOS.2919-99-05T03:50:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-04T22:03:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T03:26:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T01:52:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T01:52:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-05T05:06:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T05:57:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T00:06:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-05T01:01:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-05T05:06:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-04T21:42:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.KMOS.2919-99-04T21:00:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-04T22:44:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.KMOS.2919-99-04T21:00:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T03:26:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-05T04:25:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-05T00:47:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T00:06:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T01:52:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.KMOS.2919-99-05T03:50:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-05T00:47:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-04T22:03:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T02:35:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-04T21:42:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.KMOS.2919-99-04T21:00:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T02:35:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-04T22:44:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-04T22:44:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.KMOS.2919-99-04T23:35:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T05:57:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T02:35:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T00:06:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-05T01:01:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-04T21:11:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-05T00:47:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.KMOS.2919-99-04T23:35:00_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.KMOS.2919-99-04T23:35:03_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-05T04:25:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.NACO.2919-99-05T05:57:06_tpl-A01_0001.fits',
     '/run/media/romain/Test_Data/r.FORS2.2919-99-05T05:06:00_tpl-A01_0001.fits']


You would get the same results using::

    In [4]: listfiles = get_files(['all'],'../Test_data/')
    or
    In [5]: listfiles = get_files(['all']) ##<---If you are alredy in the dictionnary


2 - Get your keywords ready
---------------------------

After preparing the files you must prepare the keywords you want to fitsort your files with. The correct format is a list of strings, each string being a keyword, example::

    listkeys = ['HIERARCH ESO OBS ID', 'EXPTIME']


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
         'HIERARCH ESO INS MODE',
         'HIERARCH ESO OBS PROG ID',
         'HIERARCH ESO OBS ID',
         'HIERARCH ESO OBS TARG NAME',
         'DATE-OBS',
         'MJD-OBS',
         'EXPTIME',
         'HIERARCH ESO OBS AIRM',
         'HIERARCH ESO OBS AMBI FWHM',
         'HIERARCH ESO OBS AMBI TRANS',
         'HIERARCH ESO TPL EXPNO',
         'HIERARCH ESO TPL NEXP',
         'HIERARCH ESO TEL AIRM START',
         'HIERARCH ESO TEL AIRM END',
         'HIERARCH ESO TEL AMBI FWHM START',
         'HIERARCH ESO TEL AMBI FWHM END',
         'HIERARCH ESO PRO CATG'
         .
         .
         .(cut for display convinience)]


If you have a very long list you can display it using the *keywords_view* function, which will cut the length by three::

    In [8] : dfitspy.keywords_view(keys)

    --------------------------------------------------------------------------------
    SIMPLE                            | BITPIX                            | NAXIS                            
    EXTEND                            | HIERARCH ESO INS MODE             | HIERARCH ESO OBS PROG ID         
    HIERARCH ESO OBS ID               | HIERARCH ESO OBS TARG NAME        | DATE-OBS                         
    MJD-OBS                           | EXPTIME                           | HIERARCH ESO OBS AIRM            
    HIERARCH ESO OBS AMBI FWHM        | HIERARCH ESO OBS AMBI TRANS       | HIERARCH ESO TPL EXPNO           
    HIERARCH ESO TPL NEXP             | HIERARCH ESO TEL AIRM START       | HIERARCH ESO TEL AIRM END        
    HIERARCH ESO TEL AMBI FWHM START  | HIERARCH ESO TEL AMBI FWHM END    | HIERARCH ESO PRO CATG       
    .                                 | .                                 | .             
    .                                 | .                                 | .       
    .                                 | .                                 | .       
    (it has been cut)



3 - Fitsort your files
----------------------

At this point you are ready to fitsort all files. In order to achieve that you have to use the *get_all_values* function::

    In [9]: help(dfitspy.dfitsort)

	dfitsort(listfiles, listkeys, grepping=None)
	    This function get for all files, the value of all the keywords that are passed
	    
	    example:  dfitsort([file1, file2], [key1, key2]) <-- no grep
	    example:  dfitsort([file1, file2], [key1, key2], ['match', 'match2']) <-- multi grep 
	    
	    Parameter
	    ---------
	    listfiles
		        list, with file names (string, path included)
	    listkeys
		        list, of keywords (strings)
	    grep
		        list of string,
		        if not false, the grepping valueS 
		        will be compared to all the values 
		        of the keywords. If all grepping values appear in the
		        header of one file the file will be kept
	    Return
	    ------
	    file_dict
		        dictionnary, keys=filename
		                     values=dictionnary of keyword-value pairs



This function takes as argument the list of files and the list of parameters and returns a dictionary of files with values of all the keywords required::

    In [10]: fitsort = dfitspy.dfitsort(listfiles, listkeys)

    In [11]: fitsort
   {'r.NACO.2019-09-04T21:42:06_tpl-A01_0001.fits': {'HIERARCH ESO OBS ID': '5464795467',
  'EXPTIME': '234.0'},
 'r.NACO.2019-09-04T21:11:06_tpl-A01_0001.fits': {'HIERARCH ESO OBS ID': '5464795467',
  'EXPTIME': '234.0'},
 'r.NACO.2019-09-05T03:26:03_tpl-A01_0001.fits': {'HIERARCH ESO OBS ID': '5464795467',
  'EXPTIME': '234.0'},
 'r.FORS2.2019-09-04T22:03:03_tpl-A01_0001.fits': {'HIERARCH ESO OBS ID': '5464795467',
  'EXPTIME': '234.0'},
 'r.NACO.2019-09-04T21:11:03_tpl-A01_0001.fits': {'HIERARCH ESO OBS ID': '5464795467',
  'EXPTIME': '234.0'},
 'r.FORS2.2019-09-05T01:01:06_tpl-A01_0001.fits': {'HIERARCH ESO OBS ID': '5464795467',
  'EXPTIME': '234.0'},
 .
 .
 .
 .
 'r.FORS2.2019-09-05T00:47:03_tpl-A01_0001.fits': {'HIERARCH ESO OBS ID': '56472813',
  'EXPTIME': '234.0'},
 'r.KMOS.2019-09-04T23:35:00_tpl-A01_0001.fits': {'HIERARCH ESO OBS ID': '56472813',
  'EXPTIME': '234.0'},
 'r.KMOS.2019-09-04T23:35:03_tpl-A01_0001.fits': {'HIERARCH ESO OBS ID': '56472813',
  'EXPTIME': '234.0'},
 'r.FORS2.2019-09-05T04:25:06_tpl-A01_0001.fits': {'HIERARCH ESO OBS ID': '56472813',
  'EXPTIME': '234.0'},
 'r.NACO.2019-09-05T05:57:06_tpl-A01_0001.fits': {'HIERARCH ESO OBS ID': '56472813',
  'EXPTIME': '234.0'},
 'r.FORS2.2019-09-05T05:06:00_tpl-A01_0001.fits': {'HIERARCH ESO OBS ID': '56472813',
  'EXPTIME': '234.0'}}


you can display everything in a nice way using the *dfitsort_view* function::

    In [12]: dfitspy.dfitsort_view(fitsort)

       filename                                     	     HIERARCH ESO OBS ID      EXPTIME
        ---------------------------------------------	     -------------------      -------

        r.FORS2.2919-99-04T22:03:00_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-04T22:03:03_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-04T22:03:06_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-04T22:44:00_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-04T22:44:03_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-04T22:44:06_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-05T00:47:00_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-05T00:47:03_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-05T00:47:06_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-05T01:01:00_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-05T01:01:03_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-05T01:01:06_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-05T04:25:00_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-05T04:25:03_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-05T04:25:06_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-05T05:06:00_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-05T05:06:03_tpl-A01_0001.fits 		56472813              234.0
        r.FORS2.2919-99-05T05:06:06_tpl-A01_0001.fits 		56472813              234.0
        r.KMOS.2919-99-04T21:00:00_tpl-A01_0001.fits 		56479546              234.0
        r.KMOS.2919-99-04T21:00:03_tpl-A01_0001.fits 		56479546              234.0
        r.KMOS.2919-99-04T21:00:06_tpl-A01_0001.fits 		56479546              234.0
        r.KMOS.2919-99-04T23:35:00_tpl-A01_0001.fits 		56479546              234.0
        r.KMOS.2919-99-04T23:35:03_tpl-A01_0001.fits 		56479546              234.0
        r.KMOS.2919-99-04T23:35:06_tpl-A01_0001.fits 		56479546              234.0
        r.KMOS.2919-99-05T03:50:00_tpl-A01_0001.fits 		56479546              234.0
        r.KMOS.2919-99-05T03:50:03_tpl-A01_0001.fits 		56479546              234.0
        r.KMOS.2919-99-05T03:50:06_tpl-A01_0001.fits 		56479546              234.0
        r.NACO.2919-99-04T21:11:00_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-04T21:11:03_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-04T21:11:06_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-04T21:42:00_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-04T21:42:03_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-04T21:42:06_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-05T00:06:00_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-05T00:06:03_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-05T00:06:06_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-05T01:52:00_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-05T01:52:03_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-05T01:52:06_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-05T02:35:00_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-05T02:35:03_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-05T02:35:06_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-05T03:26:00_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-05T03:26:03_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-05T03:26:06_tpl-A01_0001.fits 		5464795467            234.0
        r.NACO.2919-99-05T05:57:00_tpl-A01_0001.fits 		439120439             234.0
        r.NACO.2919-99-05T05:57:03_tpl-A01_0001.fits 		439120439             234.0
        r.NACO.2919-99-05T05:57:06_tpl-A01_0001.fits 		439120439             234.0


4 - Grepping
------------

The last option allows you to grep files that have a certain value in their keywords.
By default it is set to *None* but you can give a *grepping value* (**in a list**) to replace it. When doing so dfitspy will look at all the files you give in listfiles and in all the keywords you give in listkeys. **If all the grepping values are inside the keyword values the file will be kept, if not the file will be rejected.** For example here we want all the files for which HIERARCH ESO OBS ID = 439120439 ::

    In [13]: fitsortgrep = dfitspy.dfitsort(listfiles, listkeys, ['439120439'])

    In [14]: dfitspy.dfitsort_view(fitsortgrep)

        filename                                     	     HIERARCH ESO OBS ID      EXPTIME    HIERARCH ESO PRO CATG
        ---------------------------------------------	     -------------------      -------    ---------------------
        r.NACO.2919-99-05T05:57:00_tpl-A01_0001.fits 		439120439             234.0             nac1 
        r.NACO.2919-99-05T05:57:03_tpl-A01_0001.fits 		439120439             234.0             nac2
        r.NACO.2919-99-05T05:57:06_tpl-A01_0001.fits 		439120439             234.0             nac3

.. warning ::
    
        We added an extra value in the listkeys: 'HIERARCH ESO PRO CATG'

We can also multi-grep. For example if you want to keep only *HIERARCH ESO PRO CATG = nac2* then we must add a grepping value ::

    In [15]: fitsortgrep = dfitspy.dfitsort(listfiles, listkeys, ['439120439', 'nac2'])
    In [16:] dfitspy.dfitsort_view(fitsortgrep)

        filename                                     	     HIERARCH ESO OBS ID      EXPTIME    HIERARCH ESO PRO CATG
        ---------------------------------------------	     -------------------      -------    ---------------------

        r.NACO.2919-99-05T05:57:03_tpl-A01_0001.fits 		439120439             234.0             nac2



 
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


