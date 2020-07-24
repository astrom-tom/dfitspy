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

dfitspy as an executable
========================

.. note::

   All the files used in the examples below are public and accessible via the ESO archive.

1-The command line interface help
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can start dfitspy from a terminal. dfitspy comes with a command line interface which includes a 'help' that you can display in your terminal using the help command. It must be called like this::

           [user@machine]$ dfitspy --help

This command will display the help of the program::

        usage: dfitspy [-h] [-file [FILE [FILE ...]]] [-key KEY] [--list] [--grep GREP] [--exact] [--HDU HDU]
                       [--save] [--test] [--version] [--docs]

        dfitspy: dfits|fitsort in python, version 20.7.0, Licence: GPL

        optional arguments:
          -h, --help            show this help message and exit

        Mandatory arguments if you want to dfitsort your files:
          -file [FILE [FILE ...]]
                                a file, a list of file separated by coma, *.fits is accepted, * as well, test* as
                                well, testdir/test* as well
          -key KEY              Header keyword or list of header keywords (separated by coma)

        Optional arguments:
          --list                List all keywords in a given file (if a list of file is given the first one is
                                used)
          --grep GREP           Restrain the files to the one with a given value of a given parameter. It can be
                                used multiple times with different values
          --exact, -e           Consider only exact matches for keywords
          --HDU HDU, -H HDU     HDU extension, default is 0 (primary header)
          --save                Save the list of files into an ascii file
          --test                Start the testing of the program
          --version             Display the version of the program
          --docs                Diplay the online or local documentation program

In details it means:

dfitspy has few optionnal arguments and 2 semi mandatory arguements. You can not start dfitspy without any argument:
	
* -h and '- -help': Display this help in the terminal.

2-Giving files
^^^^^^^^^^^^^^

The argument '-file' [or the shorter version '-f'] is where you feed dfitspy with your files. You have multiple option how to give values to this argument:

    * A single file:  **-file test.fits**
    * Multiple particular files: **-file test.fits,test2.fits**. They must be separated with comas and **without spaces**
    * You can use the 'all' argument: **-file all**
    * You can use the '*' solution: **-file** *
    * Semi complete names: **-file test*** or **-file *test.fits** or with path: **-file /test/*test.fits**.


.. warning::
	
    The directory that is considered here is the current directory where dfitspy is started.

3-Giving keywords
^^^^^^^^^^^^^^^^^


The argument '-key' [or the shorter version '-k'] is where you precise what keywords dfitspy must retrieve in the headers. Here again you have multiple option
  
    * a single keyword: **-key OBJECT**
    * multiple arguments: **-key OBJECT,LST**. They must be separated by comas and **without spaces**.

.. warning::

    Two things you must be careful of:

    * If your keywords contain spaces, ex: HIERARCH ESO OBS ID, you must replace it by dots: HIERARCH.ESO.OBS.ID
    
An example of output is the following (running the command: **dfitspy -f * -k HIERARCH.ESO.OBS.ID,EXPTIME**)::

        [Command: dfitspy -f * -k ESO.OBS.ID,EXPTIME]
                
        [DFITSPY INFO]> Current directory: /home/romain/Documents/tests/dfitspy 
        [DFITSPY INFO]> 24 fits files will be considered 
        [DFITSPY INFO]> We look in HDU 0 

                      filename               	ESO OBS ID	EXPTIME
        -------------------------------------	----------	-------
        XSHOOTER.2014-06-19T05:00:28.009.fits	 1072941  	 300.0 
        XSHOOTER.2014-06-19T05:00:53.001.fits	 1072941  	 250.0 
        XSHOOTER.2014-06-19T05:01:40.463.fits	 1072941  	 150.0 
        XSHOOTER.2014-06-19T05:10:40.714.fits	 1072971  	 10.0  
        XSHOOTER.2014-06-19T05:10:41.562.fits	 1072971  	  5.0  
        XSHOOTER.2014-06-19T05:10:41.934.fits	 1072971  	  1.5  
        XSHOOTER.2014-06-19T05:11:15.667.fits	 1072971  	 10.0  
        XSHOOTER.2014-06-19T05:11:16.622.fits	 1072971  	  5.0  
        XSHOOTER.2014-06-19T05:11:16.887.fits	 1072971  	  1.5  
        XSHOOTER.2014-06-19T05:12:56.978.fits	 1072971  	  0.0  
        XSHOOTER.2014-06-19T05:13:33.009.fits	 1072971  	 300.0 
        XSHOOTER.2014-06-19T05:13:58.001.fits	 1072971  	 250.0 
        XSHOOTER.2014-06-19T05:14:45.502.fits	 1072971  	 150.0 
        XSHOOTER.2014-06-19T05:24:45.749.fits	 1072985  	 10.0  
        XSHOOTER.2014-06-19T05:24:46.590.fits	 1072985  	  5.0  
        XSHOOTER.2014-06-19T05:24:46.969.fits	 1072985  	  1.5  
        XSHOOTER.2014-06-19T05:25:18.621.fits	 1072985  	 10.0  
        XSHOOTER.2014-06-19T05:25:19.503.fits	 1072985  	  5.0  
        XSHOOTER.2014-06-19T05:25:19.841.fits	 1072985  	  1.5  
        XSHOOTER.2014-06-19T05:26:29.578.fits	 1072985  	  0.0  
        XSHOOTER.2014-06-19T05:27:07.001.fits	 1072985  	 300.0 
        XSHOOTER.2014-06-19T05:27:32.003.fits	 1072985  	 250.0 
        XSHOOTER.2014-06-19T05:28:20.452.fits	 1072985  	 150.0 
        XSHOOTER.2014-06-19T05:40:13.194.fits	 1073005  	 150.0 

        [DFITSPY INFO]> 24 files used in output 


First dfitspy reminds you what directory we are in, then it tells you the number of files that were considered with the command, this number depends on what you give through the '-f' argument, and finally it will gives what is the HDU we are looinkg for. Then it displays the header always starting with the filename and then all the keywords the user requires to be displayed. And It displays the list of all the filenames and fits header values. Finally, it gives you the number of files in the list.


**It is important to understand the following things to fully understand the output of dfitspy:**

* By default, dfitspy will look for all the header keywords **that contain** the one you gave with the '-k' argument. Using the file in the previous example, if I want the keyword NAXIS, dfitspy will retrieve **ALL** the following keywords: NAXIS, NAXIS1 and NAXIS2::

        [Command: dfitspy -f * -k ESO.OBS.ID,NAXIS]

        [DFITSPY INFO]> Current directory: /home/romain/Documents/tests/dfitspy
        [DFITSPY INFO]> 24 fits files will be considered
        [DFITSPY INFO]> We look in HDU 0

                      filename               	ESO OBS ID	NAXIS	NAXIS1	NAXIS2
        -------------------------------------	----------	-----	------	------
        XSHOOTER.2014-06-19T05:00:28.009.fits	 1072941  	  2  	 2144 	 3000
        XSHOOTER.2014-06-19T05:00:53.001.fits	 1072941  	  2  	 2106 	 4000
        XSHOOTER.2014-06-19T05:01:40.463.fits	 1072941  	  2  	 2048 	 1100
        XSHOOTER.2014-06-19T05:10:40.714.fits	 1072971  	  2  	 1000 	 1000
        XSHOOTER.2014-06-19T05:10:41.562.fits	 1072971  	  2  	 2048 	 1100
        XSHOOTER.2014-06-19T05:10:41.934.fits	 1072971  	  2  	 1000 	 1000
        XSHOOTER.2014-06-19T05:11:15.667.fits	 1072971  	  2  	 1000 	 1000
        XSHOOTER.2014-06-19T05:11:16.622.fits	 1072971  	  2  	 2048 	 1100
        XSHOOTER.2014-06-19T05:11:16.887.fits	 1072971  	  2  	 1000 	 1000
        XSHOOTER.2014-06-19T05:14:45.502.fits	 1072971  	  2  	 2048 	 1100
        XSHOOTER.2014-06-19T05:40:13.194.fits	 1073005  	  2  	 2048 	 1100
        .
        .
        .[This has been cut]

This has been implemented so you can 'search' for keywords without knowing their exact names. If you happen to know the exact name of the keyword and you don't want the other ones, you can use the '--exact' argument [or the shorter version '-e'] and you will have only the keywords matching exactly the ones you asked for::


        [Command: dfitspy -f * -k ESO.OBS.ID,NAXIS -e]

        [DFITSPY INFO]> Current directory: /home/romain/Documents/tests/dfitspy 
        [DFITSPY INFO]> 24 fits files will be considered 
        [DFITSPY INFO]> We look in HDU 0 

              filename               	        ESO OBS ID	NAXIS
        -------------------------------------	----------	-----
        XSHOOTER.2014-06-19T05:00:28.009.fits	 1072941  	  2  
        XSHOOTER.2014-06-19T05:00:53.001.fits	 1072941  	  2  
        XSHOOTER.2014-06-19T05:01:40.463.fits	 1072941  	  2  
        XSHOOTER.2014-06-19T05:10:40.714.fits	 1072971  	  2  
        XSHOOTER.2014-06-19T05:10:41.562.fits	 1072971  	  2  
        XSHOOTER.2014-06-19T05:13:58.001.fits	 1072971  	  2  
        XSHOOTER.2014-06-19T05:14:45.502.fits	 1072971  	  2  
        .
        .
        .
        .[This has been cut]

* In case a file does not contain the keyword you are requesting, its value in the table will be replaced by '-'::

        [Command: dfitspy -f * -k ESO.OBS.ID,OCS.ARM]
        
        [DFITSPY INFO]> Current directory: /home/romain/Documents/tests/dfitspy
        [DFITSPY INFO]> 24 fits files will be considered
        [DFITSPY INFO]> We look in HDU 0

                      filename               	ESO OBS ID	ESO OCS ARM
        -------------------------------------	----------	-----------
        XSHOOTER.2014-06-19T05:00:28.009.fits	 1072941  	     -
        XSHOOTER.2014-06-19T05:00:53.001.fits	 1072941  	     -
        XSHOOTER.2014-06-19T05:01:40.463.fits	 1072941  	     -
        XSHOOTER.2014-06-19T05:10:40.714.fits	 1072971  	     -
        XSHOOTER.2014-06-19T05:11:16.622.fits	 1072971  	     -
        XSHOOTER.2014-06-19T05:11:16.887.fits	 1072971  	     -
        XSHOOTER.2014-06-19T05:12:56.978.fits	 1072971  	   AGCCD
        XSHOOTER.2014-06-19T05:13:33.009.fits	 1072971  	     -
        .
        .
        .[This has been cut]

* **HIERARCH keywords**: ESO FITS files come with huge collection of keywords starting by the HIERARCH prefix. You can ask for them using the HIERARCH prefix or without it::

        [Command: dfitspy -f * -k HIERARCH.ESO.OBS.ID,NAXIS -e]

        [DFITSPY INFO]> Current directory: /home/romain/Documents/tests/dfitspy
        [DFITSPY INFO]> 24 fits files will be considered
        [DFITSPY INFO]> We look in HDU 0

                      filename               	HIERARCH ESO OBS ID	NAXIS
        -------------------------------------	-------------------	-----
        XSHOOTER.2014-06-19T05:00:28.009.fits	      1072941      	  2
        XSHOOTER.2014-06-19T05:00:53.001.fits	      1072941      	  2
        XSHOOTER.2014-06-19T05:01:40.463.fits	      1072941      	  2
        XSHOOTER.2014-06-19T05:10:40.714.fits	      1072971      	  2
        XSHOOTER.2014-06-19T05:10:41.562.fits	      1072971      	  2
        XSHOOTER.2014-06-19T05:10:41.934.fits	      1072971      	  2
        XSHOOTER.2014-06-19T05:11:15.667.fits	      1072971      	  2
        .
        .
        .[This has been cut]

You will have the same result by issuing the following command: **dfitspy -f * -k ESO.OBS.ID,NAXIS -e**


4-GREPPING option
^^^^^^^^^^^^^^^^^

dfitspy offers you the possibility to display files with particular values that you are expecting. This is done using the option *- - grep* (double dash) and giving as argument an expected value of a keyword given with the *-key* option. Doing so will tell dfitspy to consider the files only if one of the keyword that the user asks to display has the grepping value. 

Simple grepping
---------------
Taking the same command as above, one might want to get only the files with ESO.OBS.ID = 1072985. This is easily assing the following flag: **- -grep 1072985** [double dash without space]. This will produce the following output in terminal::

        [command: dfitspy -f * -k ESO.OBS.ID,NAXIS,SEQ.ARM --grep 1072985]
        
        [DFITSPY INFO]> Current directory: /home/romain/Documents/tests/dfitspy 
        [DFITSPY INFO]> 24 fits files will be considered 
        [DFITSPY INFO]> We look in HDU 0 

                      filename               	ESO OBS ID	ESO SEQ ARM	NAXIS	NAXIS1	NAXIS2
        -------------------------------------	----------	-----------	-----	------	------
        XSHOOTER.2014-06-19T05:24:45.749.fits	 1072985  	    UVB    	  2  	 1000 	 1000 
        XSHOOTER.2014-06-19T05:24:46.590.fits	 1072985  	    NIR    	  2  	 2048 	 1100 
        XSHOOTER.2014-06-19T05:24:46.969.fits	 1072985  	    VIS    	  2  	 1000 	 1000 
        XSHOOTER.2014-06-19T05:25:18.621.fits	 1072985  	    UVB    	  2  	 1000 	 1000 
        XSHOOTER.2014-06-19T05:25:19.503.fits	 1072985  	    NIR    	  2  	 2048 	 1100 
        XSHOOTER.2014-06-19T05:25:19.841.fits	 1072985  	    VIS    	  2  	 1000 	 1000 
        XSHOOTER.2014-06-19T05:26:29.578.fits	 1072985  	    AGC    	  2  	 562  	 528  
        XSHOOTER.2014-06-19T05:27:07.001.fits	 1072985  	    UVB    	  2  	 2144 	 3000 
        XSHOOTER.2014-06-19T05:27:32.003.fits	 1072985  	    VIS    	  2  	 2106 	 4000 
        XSHOOTER.2014-06-19T05:28:20.452.fits	 1072985  	    NIR    	  2  	 2048 	 1100 

        [DFITSPY INFO]> 10 files used in output 

Multi grepping
--------------

We can add this flag multiple time. In the previous command, if we want only the files for the NIR arm we must add another grepping flag::

        [command: dfitspy -f * -k HIERARCH.ESO.OBS.ID,NAXIS,SEQ.ARM --grep 1072985 --grep NIR]
        
        [DFITSPY INFO]> Current directory: /home/romain/Documents/tests/dfitspy 
        [DFITSPY INFO]> 24 fits files will be considered 
        [DFITSPY INFO]> We look in HDU 0 

                      filename               	ESO SEQ ARM	HIERARCH ESO OBS ID	NAXIS	NAXIS1	NAXIS2
        -------------------------------------	-----------	-------------------	-----	------	------
        XSHOOTER.2014-06-19T05:24:46.590.fits	    NIR    	      1072985      	  2  	 2048 	 1100 
        XSHOOTER.2014-06-19T05:25:19.503.fits	    NIR    	      1072985      	  2  	 2048 	 1100 
        XSHOOTER.2014-06-19T05:28:20.452.fits	    NIR    	      1072985      	  2  	 2048 	 1100 

        [DFITSPY INFO]> 3 files used in output 


5-Files with multi extension headers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The '--HUD' arguement [or the shorter -H] allows you to explore headers of different extensions. dfitspy will read **only** the header of the extension given by --HDU, and this for all files. By default, the primary header (HDU=0) is used. An example with the header of the first extension::

        [Command dfitspy -f tfn0m410-kb98-2100-x00.fits.fz -H 1 -k POLARMOX,SUNALT,MOONDIST]

        [DFITSPY INFO]> Current directory: /home/romain/Documents/tests/lcogtdata-20200722-1 
        [DFITSPY INFO]> 1 fits files will be considered 
        [DFITSPY INFO]> We look in HDU 1 

                       filename                	 MOONDIST 	POLARMOX	  SUNALT   
        ---------------------------------------	----------	--------	-----------
        tfn0m410-kb98-2100-x00.fits.fz	        99.9823565	 0.1979 	-23.9730277

        [DFITSPY INFO]> 1 files used in output 

If a file does not have this extension, dfistpy will report an error and quit. The error looks like: 'ValueError: HDU 1 not in XSHOOTER.2014-06-19T05:00:28.009.fits'


6-Extra arguments
^^^^^^^^^^^^^^^^^
Few extra arguments can be used:

* '- -test': This runs the tests (written with unittest library) of dfitspy. 
* '- -list': **This must be used with the -file option described above**. It takes the first file given by '-file' and display a list of all the arguments in a 3 columns fashion. Example::


    [DFITSPY INFO]>keywords in r.XSHOO.2099-14-59T09:53:43.577_tpl-A01_0000.fits 
    --------------------------------------------------------------------------------
    SIMPLE                         | BITPIX                         | NAXIS                         
    EXTEND                         | COMMENT                        | DATE                          
    ORIGIN                         | TELESCOP                       | INSTRUME                      
    OBJECT                         | RA                             | DEC                           
    EQUINOX                        | RADECSYS                       | MJD-OBS                       
    DATE-OBS                       | UTC                            | LST                           
    PI-COI                         | OBSERVER                       | ARCFILE                       
    DATAMD5                        | PIPEFILE                       | ESO OBS AIRM                  
    ESO OBS AMBI FWHM              | ESO OBS AMBI TRANS             | ESO OBS ATM                   
    ESO OBS CONTAINER ID           | ESO OBS CONTAINER TYPE         | ESO OBS CONTRAST              
    ESO OBS DID                    | ESO OBS EXECTIME               | ESO OBS GRP                   
    ESO OBS ID                     | ESO OBS MOON DIST              | ESO OBS MOON FLI              
    ESO OBS NAME                   | ESO OBS NTPL                   | ESO OBS OBSERVER              
    ESO OBS PI-COI ID              | ESO OBS PI-COI NAME            | ESO OBS PROG ID               
    ESO OBS START                  | ESO OBS STREHLRATIO            | ESO OBS TARG NAME             
    ESO OBS TPLNO                  | ESO OBS TWILIGHT               | ESO OBS WATERVAPOUR           
    ESO TPL DID                    | ESO TPL EXPNO                  | ESO TPL ID                    
    ESO TPL NAME                   | ESO TPL NEXP                   | ESO TPL PRESEQ                
    ESO TPL START                  | ESO TPL VERSION                | ESO TEL AIRM END              
    ESO TEL AIRM START             | ESO TEL ALT                    | ESO TEL AMBI FWHM END         
    ESO TEL AMBI FWHM START        | ESO TEL AMBI IRSKY TEMP        | ESO TEL AMBI IWV END          
    ESO TEL AMBI IWV START         | ESO TEL AMBI IWV30D END        | ESO TEL AMBI IWV30D START     
    ESO TEL AMBI IWV30DSTD END     | ESO TEL AMBI IWV30DSTD START   | ESO TEL AMBI IWVSTD END       
    ESO TEL AMBI IWVSTD START      | ESO TEL AMBI PRES END          | ESO TEL AMBI PRES START       
    ESO TEL AMBI RHUM              | ESO TEL AMBI TAU0              | ESO TEL AMBI TEMP             
    ESO TEL AMBI WINDDIR           | ESO TEL AMBI WINDSP            | ESO TEL AZ                    
    ESO TEL CHOP ST                | ESO TEL DATE                   | ESO TEL DID                   
      
* '- -save': This function save the list of files (without all the parameters) into a file called 'dfitspy_file_list.txt'. An example is given below::

	
	##file produced by dfitspy 2018-10-03 21:16:42.133299
	##Current directory: /home/alien/Desktop/Test_data
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0000.fits
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0001.fits
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0002.fits
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0003.fits
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0004.fits
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0005.fits


* '- -docs': Display in the web browser the documentation of the code. If you have a valid internet connection it will open the online documentation, if not it will open the local documentation.
* '- -version': Display in terminal the current version of the software.

