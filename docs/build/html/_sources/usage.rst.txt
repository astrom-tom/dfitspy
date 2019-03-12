.. _Usagecli:


|Python36| |zenodo| |Licence|


.. |Licence| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
      :target: http://perso.crans.org/besson/LICENSE.html

.. |Opensource| image:: https://badges.frapsoft.com/os/v1/open-source.svg?v=103
      :target: https://github.com/ellerbrock/open-source-badges/

.. |zenodo| image:: https://zenodo.org/badge/150992970.svg
   :target: https://zenodo.org/badge/latestdoi/150992970

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

	dfitspy: dfits|fitsort in python, version 18.10.5, Licence: GPL

	optional arguments:
	  -h, --help            show this help message and exit
	  --list                List all keywords in a given file (if a list of file
		                is given the first one is used)
	  --grep GREP           Restrain the files to the one with a given value of a
		                given parameter. It can be used multiple times with
		                different values
	  --save                Save the list of files into an ascii file
	  --test                Start the testing of the program
	  --version             Display the version of the program
	  --docs                Diplay the online or local documentation program

	Mandatory arguments if you want to dfitsort your files:
	  -file [FILE [FILE ...]]
		                a file, a list of file separated by coma, *.fits is
		                accepted, * as well, test* as well, testdir/test* as
		                well
	  -key KEY              Header keyword or list of header keywords (separated
		                by coma)



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

    * ESO keywords may contain the 'HIERARCH' prefix. This is ignored by dfitspy therefore you cannot use this prefix. For example, if you have the following keywords HIERARCH ESO PRO CATG you must call it with ESO.PRO.CATG 
    * If your keywords contain spaces (ex: ESO OBS ID) you must replace it by dots: ESO.OBS.ID
    
An example of output is the following (running the command: **dfitspy -f Test_data/* -k OBJECT,LST,ESO.OBS.ID**)::

        [Command: dfitspy -f Test_data/* -k OBJECT,LST,ESO.OBS.ID]
        
	[DFITSPY INFO]> 34 fits files will be considered 

	filename                                         	OBJECT      	LST      	ESO OBS ID
	-------------------------------------------------	------------	---------	----------
	r.XSHOO.2099-14-59T09:53:43.577_tpl-A01_0000.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:43.577_tpl-A01_0001.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:43.577_tpl-A01_0002.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:43.577_tpl-A02_0000.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:43.577_tpl-A02_0001.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:43.577_tpl-A02_0002.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:43.577_tpl-A03_0000.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:43.577_tpl-A03_0001.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:43.577_tpl-A03_0002.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:44.797_tpl-A01_0000.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:44.797_tpl-A01_0001.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:44.797_tpl-A01_0002.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:44.797_tpl-A02_0000.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:44.797_tpl-A02_0001.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:44.797_tpl-A02_0002.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:44.797_tpl-A03_0000.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:44.797_tpl-A03_0001.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:44.797_tpl-A03_0002.fits	LAMP,AFC    	78684.245	2025011   
	r.XSHOO.2099-14-59T09:53:45.055_tpl-A01_0000.fits	LAMP,AFC    	78685.247	2025011   
	r.XSHOO.2099-14-59T09:53:45.055_tpl-A01_0001.fits	LAMP,AFC    	78685.247	2025011   
	r.XSHOO.2099-14-59T09:53:45.055_tpl-A01_0002.fits	LAMP,AFC    	78685.247	2025011   
	r.XSHOO.2099-14-59T09:53:45.055_tpl-A02_0000.fits	LAMP,AFC    	78685.247	2025011   
	r.XSHOO.2099-14-59T09:53:45.055_tpl-A02_0001.fits	LAMP,AFC    	78685.247	2025011   
	r.XSHOO.2099-14-59T09:53:45.055_tpl-A02_0002.fits	LAMP,AFC    	78685.247	2025011   
	r.XSHOO.2099-14-59T09:53:45.055_tpl-A03_0000.fits	LAMP,AFC    	78685.247	2025011   
	r.XSHOO.2099-14-59T09:53:45.055_tpl-A03_0001.fits	LAMP,AFC    	78685.247	2025011   
	r.XSHOO.2099-14-59T09:53:45.055_tpl-A03_0002.fits	LAMP,AFC    	78685.247	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0000.fits	STD,TELLURIC	79056.26 	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0001.fits	STD,TELLURIC	79056.26 	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0002.fits	STD,TELLURIC	79056.26 	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0003.fits	STD,TELLURIC	79056.26 	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0004.fits	STD,TELLURIC	79056.26 	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0005.fits	STD,TELLURIC	79056.26 	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0006.fits	HD 205828   	79056.26 	2025011   

	[DFITSPY INFO]> 34 files used in output 


First dfitspy gives you the number of files that was considered with the command, this number depends on what you give through the '-f' argument. Then it displays the header always starting with the filename and then all the keywords the user requires to be displayed. And It displays the list of all the filenames and fits header values. Finally, it gives you the number of files in the list.

GREPPING option
^^^^^^^^^^^^^^^

dfitspy offers you the possibility to display files with particular values that you are expecting. This is done using the option *- - grep* (double dash) and giving as argument an expected value of a keyword given with the *-key* option. Doing so will tell dfitspy to consider the files only if one of the keyword that the user ask to display as the grepping value. 

Simple grepping
---------------
Taking the same command as above, one might want to get only the files with LST = 79056.26. This is easily done using: **dfitspy -f Test_data/* -k OBJECT,LST,ESO.OBS.ID - -grep 79056.26**  and produce the output in terminal::

        [command: dfitspy -f Test_data/* -k OBJECT,LST,ESO.OBS.ID --grep 79056.26]
        
        [DFITSPY INFO]> 34 fits files will be considered 

	filename                                         	OBJECT      	LST     	ESO OBS ID
	-------------------------------------------------	------------	--------	----------
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0000.fits	STD,TELLURIC	79056.26	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0001.fits	STD,TELLURIC	79056.26	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0002.fits	STD,TELLURIC	79056.26	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0003.fits	STD,TELLURIC	79056.26	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0004.fits	STD,TELLURIC	79056.26	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0005.fits	STD,TELLURIC	79056.26	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0006.fits	HD 205828   	79056.26	2025011   

	[DFITSPY INFO]> 7 files used in output



Multi grepping
--------------

In the previous command we see that one file as a different OBJECT value as the other ones. If we want to remove it, we must **add a grepping option** and take only files with OBJECT='STD,TELLURIC', like this::

    	[Command: dfitspy -f Test_data/* -k OBJECT,LST,ESO.OBS.ID --grep 79056.26 --grep STD,TELLURIC]

	[DFITSPY INFO]> 34 fits files will be considered 

	filename                                         	OBJECT      	LST     	ESO OBS ID
	-------------------------------------------------	------------	--------	----------
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0000.fits	STD,TELLURIC	79056.26	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0001.fits	STD,TELLURIC	79056.26	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0002.fits	STD,TELLURIC	79056.26	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0003.fits	STD,TELLURIC	79056.26	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0004.fits	STD,TELLURIC	79056.26	2025011   
	r.XSHOO.2099-14-59T09:59:57.509_tpl-A01_0005.fits	STD,TELLURIC	79056.26	2025011   

	[DFITSPY INFO]> 6 files used in output


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

