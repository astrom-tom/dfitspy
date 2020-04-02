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


The command line interface help
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can start dfitspy from a terminal. dfitspy comes with a command line interface which includes a 'help' that you can display in your terminal using the help command. It must be called like this::

           [user@machine]$ dfitspy --help

This command will display the help of the program::

    usage: dfitspy [-h] [-file [FILE [FILE ...]]] [-key KEY] [--list] 
              [--grep GREP] [--save] [--test] [--version] [--docs]

    dfitspy: dfits|fitsort in python, version 20.3.2, Licence: GPL

    optional arguments:
      -h, --help            show this help message and exit

    Mandatory arguments if you want to dfitsort your files:
      -file [FILE [FILE ...]]
                            a file, a list of file separated by coma, *.fits is accepted, * as well, test* as well,
                            testdir/test* as well
      -key KEY              Header keyword or list of header keywords (separated by coma)

    Optional arguments:
      --list                List all keywords in a given file (if a list of file is given the first one is used)
      --grep GREP           Restrain the files to the one with a given value of a given parameter. It can be used
                            multiple times with different values
      --save                Save the list of files into an ascii file
      --test                Start the testing of the program
      --version             Display the version of the program
      --docs                Diplay the online or local documentation program





In details it means:

dfitspy has few optionnal arguments and 2 semi mandatory arguements. You can not start dfitspy without any argument:
	
* -h and '- -help': Display this help in the terminal.

If you want to dfits | fitsort
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* -file: This is where you feed dfitspy with your files. You have multiple option how to give values to this argument:

    * A single file:  **-file test.fits**
    * Multiple particular files: **-file test.fits,test2.fits**. They must be separated with comas and **without spaces**
    * You can use the 'all' argument: **-file all**
    * You can use the '*' solution: **-file** *
    * Semi complete names: **-file test*** or **-file *test.fits** or with path: **-file /test/*test.fits**.


.. warning::
	
    The directory that is considered here is the current directory where dfitspy is started.

* -key: this is where you ask dfitspy to look for particular keywords in the headers. Here again you have multiple option
  
    * a single keyword: **-key OBJECT**
    * multiple arguments: **-key OBJECT,LST**. They must be separated by comas and **without spaces**.

.. warning::

    Two things you must be careful of:

    * If your keywords contain spaces (ex: ESO OBS ID) you must replace it by dots: ESO.OBS.ID
    
An example of output is the following (running the command: **dfitspy -f * -k HIERARCH.ESO.OBS.ID,EXPTIME**)::

        [Command: dfitspy -f * -k HIERARCH.ESO.OBS.ID,EXPTIME]
        
        [DFITSPY INFO]> 48 fits files will be considered 



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

	[DFITSPY INFO]> 48 files used in output


First dfitspy gives you the number of files that was considered with the command, this number depends on what you give through the '-f' argument. Then it displays the header always starting with the filename and then all the keywords the user requires to be displayed. And It displays the list of all the filenames and fits header values. Finally, it gives you the number of files in the list.

GREPPING option
^^^^^^^^^^^^^^^

dfitspy offers you the possibility to display files with particular values that you are expecting. This is done using the option *- - grep* (double dash) and giving as argument an expected value of a keyword given with the *-key* option. Doing so will tell dfitspy to consider the files only if one of the keyword that the user ask to display as the grepping value. 

Simple grepping
---------------
Taking the same command as above, one might want to get only the files with HIERARCH.ESO.OBS.ID = 439120439. This is easily done using: **dfitspy -f * -k HIERARCH.ESO.OBS.ID,EXPTIME - -grep 439120439**  and produce the output in terminal::

        [command: dfitspy -f * -k HIERARCH.ESO.OBS.ID,EXPTIME,HIERARCH.ESO.PRO.CATG --grep 439120439]
        
        [DFITSPY INFO]> 48 fits files will be considered 

        filename                                     	     HIERARCH ESO OBS ID      EXPTIME    HIERARCH ESO PRO CATG
        ---------------------------------------------	     -------------------      -------    ---------------------
        r.NACO.2919-99-05T05:57:00_tpl-A01_0001.fits 		439120439             234.0             nac1 
        r.NACO.2919-99-05T05:57:03_tpl-A01_0001.fits 		439120439             234.0             nac2
        r.NACO.2919-99-05T05:57:06_tpl-A01_0001.fits 		439120439             234.0             nac3

	[DFITSPY INFO]> 3 files used in output



Multi grepping
--------------

In the previous command we see that one file as a different HIERARCH ESO PRO CATG value as the other ones. If we want to remove select for example only HIERARCH ESO PRO CATG = nac2, we must **add a grepping option** and take only files with HIERARCH ESO PRO CATG='nac2', like this::

        [command: dfitspy -f * -k HIERARCH.ESO.OBS.ID,EXPTIME,HIERARCH.ESO.PRO.CATG --grep 439120439 --grep nac2]
        
        [DFITSPY INFO]> 48 fits files will be considered 

        filename                                     	     HIERARCH ESO OBS ID      EXPTIME    HIERARCH ESO PRO CATG
        ---------------------------------------------	     -------------------      -------    ---------------------

        r.NACO.2919-99-05T05:57:03_tpl-A01_0001.fits 		439120439             234.0             nac2


	[DFITSPY INFO]> 1 files used in output


Extra arguments
^^^^^^^^^^^^^^^
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

