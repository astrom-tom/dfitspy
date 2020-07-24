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



1 - Get your files ready
^^^^^^^^^^^^^^^^^^^^^^^^

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

The easiest way is to analyse **all** the files in the current directory::

    In [3]: listfiles = dfitspy.get_files(['all'])
        ['/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:40:13.194.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:10:40.714.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:11:16.622.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:27:32.003.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:27:07.001.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:13:33.009.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:00:53.001.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:12:56.978.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:25:18.621.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:13:58.001.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:10:41.934.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:11:15.667.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:25:19.841.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:24:45.749.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:14:45.502.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:11:16.887.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:01:40.463.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:00:28.009.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:26:29.578.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:28:20.452.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:10:41.562.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:24:46.590.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:24:46.969.fits',
         '/home/romain/Documents/tests/dfitspy/XSHOOTER.2014-06-19T05:25:19.503.fits']


You would get the same results using::

    In [4]: listfiles = get_files(['all'],dire='../Test_data/')


2 - Get your keywords ready
^^^^^^^^^^^^^^^^^^^^^^^^^^^

After preparing the files you must prepare the keywords you want to fitsort your files with. The correct format is a list of strings, each string being a keyword, example::

    listkeys = ['HIERARCH ESO OBS ID', 'EXPTIME']


If you do not remember the name of the keywords you want to use you can retrieve them all and display them::

    In [5]: help(dfitspy.get_all_keyword)

        get_all_keyword(thefile, HDU=0)
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


This function takes a file as input and return the list of all the keywords::

    In [6]: keys = dfitspy.get_all_keyword('XSHOOTER.2014-06-19T05:10:40.714.fits')
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

It is important to note that you can also search in the header of different extension. For example accessing the extension number 1 (default is 0, the primary header)::


    In [37]: dfitspy.get_all_keyword('../lcogtdata-2022-1/tfn0m410-kb98-20100-x00.fits.fz', HDU=1)   
    Out[37]: 
        ['SIMPLE',
         'BITPIX',
         'NAXIS',
         'NAXIS1',
         'NAXIS2',
         'PCOUNT',
         'GCOUNT',
         'XTENSION',
         'BZERO',
         'BSCALE',
         'DATADICV',
         'HDRVER',
         'ORIGIN',
         'SITEID',


3 - Fitsort your files
^^^^^^^^^^^^^^^^^^^^^^

At this point you are ready to fitsort all files. In order to achieve that you have to use the *get_all_values* function::

    In [9]: help(dfitspy.dfitsort)

        dfitsort(listfiles, listkeys, exact=False, grepping=None, HDU=0)
            This function get for all files, the value of all the keywords that are passed
            
            
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
            dfitsort([file1, file2], [key1, key2]) <-- no grep
            
            dfitsort([file1, file2], [key1, key2], ['match', 'match2']) <-- multi grep



This function takes as argument the list of files and the list of parameters and returns a dictionary of files with values of all the keywords required::

    In [10]: fitsort = dfitspy.dfitsort(listfiles, listkeys)

    In [11]: fitsort
 
        {'XSHOOTER.2014-06-19T05:40:13.194.fits': {'HIERARCH ESO OBS START': '2014-06-19T05:34:44',
          'EXPTIME': '150.0'},
         'XSHOOTER.2014-06-19T05:10:40.714.fits': {'HIERARCH ESO OBS START': '2014-06-19T05:09:01',
          'EXPTIME': '10.0'},
         'XSHOOTER.2014-06-19T05:11:16.622.fits': {'HIERARCH ESO OBS START': '2014-06-19T05:09:01',
          'EXPTIME': '5.0'},
         'XSHOOTER.2014-06-19T05:27:32.003.fits': {'HIERARCH ESO OBS START': '2014-06-19T05:23:09',
          'EXPTIME': '250.0'},
         'XSHOOTER.2014-06-19T05:27:07.001.fits': {'HIERARCH ESO OBS START': '2014-06-19T05:23:09',
          'EXPTIME': '300.0'},
          .
          .
          .
         'XSHOOTER.2014-06-19T05:28:20.452.fits': {'HIERARCH ESO OBS START': '2014-06-19T05:23:09',
          'EXPTIME': '150.0'},
         'XSHOOTER.2014-06-19T05:10:41.562.fits': {'HIERARCH ESO OBS START': '2014-06-19T05:09:01',
          'EXPTIME': '5.0'},
         'XSHOOTER.2014-06-19T05:24:46.590.fits': {'HIERARCH ESO OBS START': '2014-06-19T05:23:09',
          'EXPTIME': '5.0'},
         'XSHOOTER.2014-06-19T05:24:46.969.fits': {'HIERARCH ESO OBS START': '2014-06-19T05:23:09',
          'EXPTIME': '1.5'},
         'XSHOOTER.2014-06-19T05:25:19.503.fits': {'HIERARCH ESO OBS START': '2014-06-19T05:23:09',
          'EXPTIME': '5.0'}}


you can display everything in a nice way using the *dfitsort_view* function::

    In [12]: dfitspy.dfitsort_view(fitsort)
                      filename               	EXPTIME	HIERARCH ESO OBS START
        -------------------------------------	-------	----------------------
        XSHOOTER.2014-06-19T05:40:13.194.fits	 150.0 	 2014-06-19T05:34:44  
        XSHOOTER.2014-06-19T05:10:40.714.fits	 10.0  	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:11:16.622.fits	  5.0  	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:27:32.003.fits	 250.0 	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:27:07.001.fits	 300.0 	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:13:33.009.fits	 300.0 	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:00:53.001.fits	 250.0 	 2014-06-19T04:55:50  
        XSHOOTER.2014-06-19T05:12:56.978.fits	  0.0  	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:25:18.621.fits	 10.0  	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:13:58.001.fits	 250.0 	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:10:41.934.fits	  1.5  	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:11:15.667.fits	 10.0  	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:25:19.841.fits	  1.5  	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:24:45.749.fits	 10.0  	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:14:45.502.fits	 150.0 	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:11:16.887.fits	  1.5  	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:01:40.463.fits	 150.0 	 2014-06-19T04:55:50  
        XSHOOTER.2014-06-19T05:00:28.009.fits	 300.0 	 2014-06-19T04:55:50  
        XSHOOTER.2014-06-19T05:26:29.578.fits	  0.0  	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:28:20.452.fits	 150.0 	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:10:41.562.fits	  5.0  	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:24:46.590.fits	  5.0  	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:24:46.969.fits	  1.5  	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:25:19.503.fits	  5.0  	 2014-06-19T05:23:09  

**It is important to understand the following things to fully understand the output of dfitspy:**

* By default, dfitspy will look for all the header keywords **that contain** the one you gave with the '-k' argument .Using the file in the previous example, if I want the keyword NAXIS, dfitspy will retrieve **ALL** the following keywords: NAXIS, NAXIS1 and NAXIS2::

    In [10]: fitsort = dfitspy.dfitsort(listfiles, ['HIERARCH ESO OBS START', 'NAXIS'])
    In [11]: dfitspy.dfitsort_view(fitsort)
                  filename               	HIERARCH ESO OBS START	NAXIS	NAXIS1	NAXIS2
        -------------------------------------	----------------------	-----	------	------
        XSHOOTER.2014-06-19T05:40:13.194.fits	 2014-06-19T05:34:44  	  2  	 2048 	 1100
        XSHOOTER.2014-06-19T05:10:40.714.fits	 2014-06-19T05:09:01  	  2  	 1000 	 1000
        XSHOOTER.2014-06-19T05:11:16.622.fits	 2014-06-19T05:09:01  	  2  	 2048 	 1100
        XSHOOTER.2014-06-19T05:27:32.003.fits	 2014-06-19T05:23:09  	  2  	 2106 	 4000
        XSHOOTER.2014-06-19T05:27:07.001.fits	 2014-06-19T05:23:09  	  2  	 2144 	 3000
        XSHOOTER.2014-06-19T05:13:33.009.fits	 2014-06-19T05:09:01  	  2  	 2144 	 3000
        XSHOOTER.2014-06-19T05:00:53.001.fits	 2014-06-19T04:55:50  	  2  	 2106 	 4000
        XSHOOTER.2014-06-19T05:12:56.978.fits	 2014-06-19T05:09:01  	  2  	 562  	 528
        XSHOOTER.2014-06-19T05:25:18.621.fits	 2014-06-19T05:23:09  	  2  	 1000 	 1000
        XSHOOTER.2014-06-19T05:13:58.001.fits	 2014-06-19T05:09:01  	  2  	 2106 	 4000
        XSHOOTER.2014-06-19T05:10:41.934.fits	 2014-06-19T05:09:01  	  2  	 1000 	 1000
        XSHOOTER.2014-06-19T05:11:15.667.fits	 2014-06-19T05:09:01  	  2  	 1000 	 1000
        XSHOOTER.2014-06-19T05:25:19.841.fits	 2014-06-19T05:23:09  	  2  	 1000 	 1000
        XSHOOTER.2014-06-19T05:24:45.749.fits	 2014-06-19T05:23:09  	  2  	 1000 	 1000
        XSHOOTER.2014-06-19T05:14:45.502.fits	 2014-06-19T05:09:01  	  2  	 2048 	 1100
        XSHOOTER.2014-06-19T05:11:16.887.fits	 2014-06-19T05:09:01  	  2  	 1000 	 1000
        XSHOOTER.2014-06-19T05:01:40.463.fits	 2014-06-19T04:55:50  	  2  	 2048 	 1100
        XSHOOTER.2014-06-19T05:00:28.009.fits	 2014-06-19T04:55:50  	  2  	 2144 	 3000
        XSHOOTER.2014-06-19T05:26:29.578.fits	 2014-06-19T05:23:09  	  2  	 562  	 528
        XSHOOTER.2014-06-19T05:28:20.452.fits	 2014-06-19T05:23:09  	  2  	 2048 	 1100
        XSHOOTER.2014-06-19T05:10:41.562.fits	 2014-06-19T05:09:01  	  2  	 2048 	 1100
        XSHOOTER.2014-06-19T05:24:46.590.fits	 2014-06-19T05:23:09  	  2  	 2048 	 1100
        XSHOOTER.2014-06-19T05:24:46.969.fits	 2014-06-19T05:23:09  	  2  	 1000 	 1000
        XSHOOTER.2014-06-19T05:25:19.503.fits	 2014-06-19T05:23:09  	  2  	 2048 	 1100


This has been implemented so you can 'search' for keywords without knowing their exact names. If you happen to know the exact name of the keyword and you don't want the other ones, you can use the boolean argument 'exact' and you will have only the keywords matching exactly the ones you asked for::


    In [12]: fitsort = dfitspy.dfitsort(listfiles, ['HIERARCH ESO OBS START', 'NAXIS'], exact=True)
    In [13]: dfitspy.dfitsort_view(fitsort)
                      filename               	HIERARCH ESO OBS START	NAXIS
        -------------------------------------	----------------------	-----
        XSHOOTER.2014-06-19T05:40:13.194.fits	 2014-06-19T05:34:44  	  2
        XSHOOTER.2014-06-19T05:10:40.714.fits	 2014-06-19T05:09:01  	  2
        XSHOOTER.2014-06-19T05:11:16.622.fits	 2014-06-19T05:09:01  	  2
        XSHOOTER.2014-06-19T05:27:32.003.fits	 2014-06-19T05:23:09  	  2
        XSHOOTER.2014-06-19T05:27:07.001.fits	 2014-06-19T05:23:09  	  2
        XSHOOTER.2014-06-19T05:13:33.009.fits	 2014-06-19T05:09:01  	  2
        XSHOOTER.2014-06-19T05:00:53.001.fits	 2014-06-19T04:55:50  	  2
        XSHOOTER.2014-06-19T05:12:56.978.fits	 2014-06-19T05:09:01  	  2
        XSHOOTER.2014-06-19T05:25:18.621.fits	 2014-06-19T05:23:09  	  2
        XSHOOTER.2014-06-19T05:13:58.001.fits	 2014-06-19T05:09:01  	  2
        XSHOOTER.2014-06-19T05:10:41.934.fits	 2014-06-19T05:09:01  	  2
        XSHOOTER.2014-06-19T05:11:15.667.fits	 2014-06-19T05:09:01  	  2
        XSHOOTER.2014-06-19T05:25:19.841.fits	 2014-06-19T05:23:09  	  2
        XSHOOTER.2014-06-19T05:24:45.749.fits	 2014-06-19T05:23:09  	  2
        XSHOOTER.2014-06-19T05:14:45.502.fits	 2014-06-19T05:09:01  	  2
        XSHOOTER.2014-06-19T05:11:16.887.fits	 2014-06-19T05:09:01  	  2
        XSHOOTER.2014-06-19T05:01:40.463.fits	 2014-06-19T04:55:50  	  2
        XSHOOTER.2014-06-19T05:00:28.009.fits	 2014-06-19T04:55:50  	  2
        XSHOOTER.2014-06-19T05:26:29.578.fits	 2014-06-19T05:23:09  	  2
        XSHOOTER.2014-06-19T05:28:20.452.fits	 2014-06-19T05:23:09  	  2
        XSHOOTER.2014-06-19T05:10:41.562.fits	 2014-06-19T05:09:01  	  2
        XSHOOTER.2014-06-19T05:24:46.590.fits	 2014-06-19T05:23:09  	  2
        XSHOOTER.2014-06-19T05:24:46.969.fits	 2014-06-19T05:23:09  	  2
        XSHOOTER.2014-06-19T05:25:19.503.fits	 2014-06-19T05:23:09  	  2
         
* In case a file does not contain a keyword, the output dictionary will not contain that keyword either::


    In [14]: fitsort = dfitspy.dfitsort(listfiles, ['ESO OBS ID', 'OCS ARM'])
    In [15]: fitsort
            {'XSHOOTER.2014-06-19T05:40:13.194.fits': {'ESO OBS ID': '1073005'},
         'XSHOOTER.2014-06-19T05:10:40.714.fits': {'ESO OBS ID': '1072971'},
         'XSHOOTER.2014-06-19T05:11:16.622.fits': {'ESO OBS ID': '1072971'},
         'XSHOOTER.2014-06-19T05:27:32.003.fits': {'ESO OBS ID': '1072985'},
         'XSHOOTER.2014-06-19T05:27:07.001.fits': {'ESO OBS ID': '1072985'},
         'XSHOOTER.2014-06-19T05:13:33.009.fits': {'ESO OBS ID': '1072971'},
         'XSHOOTER.2014-06-19T05:00:53.001.fits': {'ESO OBS ID': '1072941'},
         'XSHOOTER.2014-06-19T05:12:56.978.fits': {'ESO OBS ID': '1072971',
          'ESO OCS ARM': 'AGCCD'},
         'XSHOOTER.2014-06-19T05:25:18.621.fits': {'ESO OBS ID': '1072985'},
         'XSHOOTER.2014-06-19T05:13:58.001.fits': {'ESO OBS ID': '1072971'},
         'XSHOOTER.2014-06-19T05:10:41.934.fits': {'ESO OBS ID': '1072971'},
         'XSHOOTER.2014-06-19T05:11:15.667.fits': {'ESO OBS ID': '1072971'},
         'XSHOOTER.2014-06-19T05:25:19.841.fits': {'ESO OBS ID': '1072985'},
         'XSHOOTER.2014-06-19T05:24:45.749.fits': {'ESO OBS ID': '1072985'},
         'XSHOOTER.2014-06-19T05:14:45.502.fits': {'ESO OBS ID': '1072971'},
         'XSHOOTER.2014-06-19T05:11:16.887.fits': {'ESO OBS ID': '1072971'},
         'XSHOOTER.2014-06-19T05:01:40.463.fits': {'ESO OBS ID': '1072941'},
         'XSHOOTER.2014-06-19T05:00:28.009.fits': {'ESO OBS ID': '1072941'},
         'XSHOOTER.2014-06-19T05:26:29.578.fits': {'ESO OBS ID': '1072985',
          'ESO OCS ARM': 'AGCCD'},
         'XSHOOTER.2014-06-19T05:28:20.452.fits': {'ESO OBS ID': '1072985'},
         'XSHOOTER.2014-06-19T05:10:41.562.fits': {'ESO OBS ID': '1072971'},
         'XSHOOTER.2014-06-19T05:24:46.590.fits': {'ESO OBS ID': '1072985'},
         'XSHOOTER.2014-06-19T05:24:46.969.fits': {'ESO OBS ID': '1072985'},
         'XSHOOTER.2014-06-19T05:25:19.503.fits': {'ESO OBS ID': '1072985'}}

* **HIERARCH keywords**: ESO FITS Files come with a huge collection of keywords starting by the HIERARCH prefix. You can ask for them using this prefix or not::

    In [16]: fitsort = dfitspy.dfitsort(listfiles, ['HIERARCH ESO OBS ID', 'HIERARCH ESO OBS START'])
    In [17]: dfitspy.dfitsort_view(fitsort)
              filename               	        HIERARCH ESO OBS ID	HIERARCH ESO OBS START
        -------------------------------------	-------------------	----------------------
        XSHOOTER.2014-06-19T05:40:13.194.fits	      1073005      	 2014-06-19T05:34:44  
        XSHOOTER.2014-06-19T05:10:40.714.fits	      1072971      	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:11:16.622.fits	      1072971      	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:27:32.003.fits	      1072985      	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:27:07.001.fits	      1072985      	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:13:33.009.fits	      1072971      	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:00:53.001.fits	      1072941      	 2014-06-19T04:55:50  
        XSHOOTER.2014-06-19T05:12:56.978.fits	      1072971      	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:25:18.621.fits	      1072985      	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:13:58.001.fits	      1072971      	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:10:41.934.fits	      1072971      	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:11:15.667.fits	      1072971      	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:25:19.841.fits	      1072985      	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:24:45.749.fits	      1072985      	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:14:45.502.fits	      1072971      	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:11:16.887.fits	      1072971      	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:01:40.463.fits	      1072941      	 2014-06-19T04:55:50  
        XSHOOTER.2014-06-19T05:00:28.009.fits	      1072941      	 2014-06-19T04:55:50  
        XSHOOTER.2014-06-19T05:26:29.578.fits	      1072985      	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:28:20.452.fits	      1072985      	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:10:41.562.fits	      1072971      	 2014-06-19T05:09:01  
        XSHOOTER.2014-06-19T05:24:46.590.fits	      1072985      	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:24:46.969.fits	      1072985      	 2014-06-19T05:23:09  
        XSHOOTER.2014-06-19T05:25:19.503.fits	      1072985      	 2014-06-19T05:23:09  

You would have exaclty the same results with 'dfitspy.dfitsort(listfiles, ['ESO OBS ID', 'ESO OBS START'])' 

* As before, you can look in the header of different extension, simply adding the argument 'HDU='+number of the extension you want.

4 - Grepping
^^^^^^^^^^^^

The next option allows you to grep files that have a certain value in their keywords.
By default it is set to *None* but you can give a *grepping value* (**in a list**) to replace it. When doing so dfitspy will look at all the files you give in listfiles and in all the keywords you give in listkeys. **If all the grepping values are inside the keyword values the file will be kept, if not the file will be rejected.** For example here we want all the files for which HIERARCH ESO OBS ID = 439120439 ::

    In [18]: fitsortgrep = dfitspy.dfitsort(listfiles, ['ESO OBS ID', 'SEQ ARM'],
                                            grepping=['1072985'])
    In [19]: dfitspy.dfitsort_view(fitsortgrep)
                      filename               	ESO SEQ ARM	HIERARCH ESO OBS ID
        -------------------------------------	-----------	-------------------
        XSHOOTER.2014-06-19T05:27:32.003.fits	    VIS    	      1072985      
        XSHOOTER.2014-06-19T05:27:07.001.fits	    UVB    	      1072985      
        XSHOOTER.2014-06-19T05:25:18.621.fits	    UVB    	      1072985      
        XSHOOTER.2014-06-19T05:25:19.841.fits	    VIS    	      1072985      
        XSHOOTER.2014-06-19T05:24:45.749.fits	    UVB    	      1072985      
        XSHOOTER.2014-06-19T05:26:29.578.fits	    AGC    	      1072985      
        XSHOOTER.2014-06-19T05:28:20.452.fits	    NIR    	      1072985      
        XSHOOTER.2014-06-19T05:24:46.590.fits	    NIR    	      1072985      
        XSHOOTER.2014-06-19T05:24:46.969.fits	    VIS    	      1072985      
        XSHOOTER.2014-06-19T05:25:19.503.fits	    NIR    	      1072985      


We can also multi-grep. For example if you want to keep only *ESO SEQ ARM = NIR* then we must add a grepping value ::

    In [20]: fitsortgrep = dfitspy.dfitsort(listfiles, ['ESO OBS ID', 'SEQ ARM'],
                                            grepping=['1072985', 'NIR'])
    In [21]: dfitspy.dfitsort_view(fitsortgrep)
                      filename               	ESO SEQ ARM	HIERARCH ESO OBS ID
        -------------------------------------	-----------	-------------------
        XSHOOTER.2014-06-19T05:28:20.452.fits	    NIR    	      1072985      
        XSHOOTER.2014-06-19T05:24:46.590.fits	    NIR    	      1072985      
        XSHOOTER.2014-06-19T05:25:19.503.fits	    NIR    	      1072985      



 
5-Test
^^^^^^

Dfitspy comes with a unit testing suite (26 tests in total). To run it::

    In [1]: import dfitspy
    In [2]: dfitspy.test()

        ---UnitTest the command interface
        test_cli (dfitspy.cli.Interfacetest)
        This method tests the command line interface ... ok

        ----------------------------------------------------------------------
        Ran 1 test in 0.005s

        OK

        ---UnitTest the display printouts
        test_displayfinal (dfitspy.display.Testdisplayfinal)
        test the final display function ... ok
        test_displayfinal_missing_keyword (dfitspy.display.Testdisplayfinal)
        test the final display function when a keyword is missing for a file ... ok
        test_five (dfitspy.display.Testdisplaylist)
        idem with five ... ok
        test_four (dfitspy.display.Testdisplaylist)
        idem with 4 keywords ... ok
        test_six (dfitspy.display.Testdisplaylist)
        idem with six ... ok
        test_three (dfitspy.display.Testdisplaylist)
        Test if 3 keywords have to be displayed ... ok

        ----------------------------------------------------------------------
        Ran 6 tests in 0.005s

        OK

        ---UnitTest getting file names
        test_get_file_all_no_files (dfitspy.get_files_and_keys.Testgetfiles)
        Here we test the get_files function when the user does not precise the ... ok
        test_get_file_all_with_files (dfitspy.get_files_and_keys.Testgetfiles)
        Here we test the get_files function when the user does not precise the ... ok
        test_get_multi_file_goodname (dfitspy.get_files_and_keys.Testgetfiles)
        Test for multiple files ... ok
        test_get_single_file_goodname (dfitspy.get_files_and_keys.Testgetfiles)
        Test with single file when a good filename is given ... ok
        test_get_single_file_wrongname (dfitspy.get_files_and_keys.Testgetfiles)
        Test with single file when a wrong filename is given ... ok
        test_list_files (dfitspy.get_files_and_keys.Testgetfiles)
        Test for list of files as input ... ok
        test_get_multi_key (dfitspy.get_files_and_keys.Testgetkeys)
        We give three keywords and have to get the three keywords ... ok
        test_get_multi_key_with_HIERARCH (dfitspy.get_files_and_keys.Testgetkeys)
        We give three keywords and have to get the three keywords ... ok
        test_get_single_key (dfitspy.get_files_and_keys.Testgetkeys)
        We give a single keyword and have to get exaclty the same ... ok

        ----------------------------------------------------------------------
        Ran 9 tests in 0.049s

        OK

        ---UnitTest read fits and extraction functions
        test_readfile (dfitspy.readfits.Testextractheader)
        This function test the header extraction ... ok
        test_get_all_keyword (dfitspy.readfits.Testkeywordextraction)
        This function test function that extracts all the keyword of the header ... ok
        test_get_value_missing_keyword (dfitspy.readfits.Testkeywordextraction)
        This function tests the extraction of keywords without grepping values ... ok
        test_get_value_no_grep (dfitspy.readfits.Testkeywordextraction)
        This function tests the extraction of keywords without grepping values ... ok
        test_get_value_same_keyword_root (dfitspy.readfits.Testkeywordextraction)
        This function tests the extraction of keywords without grepping values ... ok
        test_get_value_same_keyword_root_but_exact (dfitspy.readfits.Testkeywordextraction)
        This function tests the extraction of keywords without grepping values ... ok
        test_get_value_true (dfitspy.readfits.Testkeywordextraction)
        This method tests the function that gets the value of the keyword in the file ... ok
        test_get_value_with_grep (dfitspy.readfits.Testkeywordextraction)
        Same as before but with grepping ... ok
        test_get_value_wrong (dfitspy.readfits.Testkeywordextraction)
        This function test function that gets the value of the keyword in the file ...    ok

        ----------------------------------------------------------------------
        Ran 9 tests in 0.029s

        OK


