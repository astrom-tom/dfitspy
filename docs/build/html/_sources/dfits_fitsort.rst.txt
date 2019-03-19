.. _dfitsfitsort:

|JOSS| |Python36| |Licence|

.. |JOSS| image:: http://joss.theoj.org/papers/10.21105/joss.01249/status.svg
   :target: https://doi.org/10.21105/joss.01249

.. |Licence| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
      :target: http://perso.crans.org/besson/LICENSE.html

.. |Opensource| image:: https://badges.frapsoft.com/os/v1/open-source.svg?v=103
      :target: https://github.com/ellerbrock/open-source-badges/

.. |Python36| image:: https://img.shields.io/badge/python-3.6-blue.svg
.. _Python36: https://www.python.org/downloads/release/python-360/


dfits and fitsort
=================

We provide in this page the man pages of the dfits and fitsort original packages.


The `dfits <ftp://134.171.42.54/scisoft/scisoft4/linux/redhat9/eclipse/eclipse/man/html1/fitsort.html>`_ manpage::


      Name
       dfits - display FITS file header information

      Synopsis
             dfits [-x xtnum] <list>
             dfits [-x xtnum] -

      Description
             dfits  displays FITS header informations on stdout. Header
             information  can  be  found  in  the  main   header   only
             (default),  in  extensions, or in both.  See the -x option
             below.  dfits accepts multi-file input.  `dfits -' expects
             single file data coming from stdin.

      Options
             -x xtnum
                    Specifies  the  extension  to print out. Extensions
                    are numbered starting from 1. If this option is not
                    specified,  only the main header is printed out. If
                    this option specifies an extension  that  does  not
                    exist, nothing is printed out.
                    Specify 0 as extension number to get a print of the
                    main header plus all extension headers.

             Examples :
             dfits *.fits
             dfits *.fits | grep NAXIS3
             gzip -d < star.fits.gz | dfits - | more
             dfits -x 0 *.fits
             dfits -x 3 *.fits

      See Also
             fitsort can be combined with dfits output to sort out key-
             word values of a group of FITS files.

      Files
             Files shall all comply with FITS format


And the `fitsort <ftp://134.171.42.54/scisoft/scisoft4/linux/redhat9/eclipse/eclipse/man/html1/dfits.html>`_ manpage::

      Name
       fitsort  -  sort  FITS  header  information from a list of
       files

      Synopsis
             dfits <FITS files...> | fitsort <FITS keywords...>

      Description
             fitsort extract keyword values from a set of FITS  headers
             and outputs it in an ASCII table format, which is compati-
             ble with most data processing software packages. It  shall
             only be used in combination with the dfits utility.

             The  ASCII output is shown in columns. Columns are aligned
             with blank characters and also separated  by  tabulations.
             Blank alignment allows human readers to visualize the out-
             put in a pretty format, tabulations are there for  spread-
             sheet  compatibility. If you want to load out fitsort out-
             put into any spreadsheet, specify  that  fields  shall  be
             separated  by  tabulations  and entries separated by line-
             feeds.

             Examples :
             dfits *.fits | fitsort BITPIX NAXIS NAXIS1 NAXIS2

             The output would look like:
             FILE           BITPIX   NAXIS    NAXIS1   NAXIS2
             file0001.fits  16       2        128      128
             file0002.fits  32       2        512      512
             ...

             ESO specific features in the FITS  header  are  also  sup-
             ported.  To  get  values for `HIERARCH ESO' keywords, just
             give the complete names within double quotes. e.g.

             dfits *.fits | fitsort "HIERARCH ESO INS LENS"

             Another way of giving HIERARCH ESO keywords is to use  the
             short FITS notation, the above example can be given as:

             dfits *.fits | fitsort INS.LENS

             Example:  to  retrieve  the  DPR keywords from an ESO FITS
             header, you would use:

             dfits  *.fits  |  fitsort  To  be  completed...   DPR.CATG
             DPR.TYPE DPR.TECH

             This second way of requesting HIERARCH ESO keywords is not
             only shorter to type, it also avoids typing quotes or dou-
             ble-quotes on the command-line, making it easier to script
             with fitsort.

             Notice that the keywords you give on the command-line  are
             case-insensitive.  The above line is equivalent to:

             dfits *.fits | fitsort dpr.catg dpr.type dpr.tech

      Options
             -d     Do not print out the first output line. This option
                    is useful to get only the  query  results,  without
                    the  top line (giving all column names). This makes
                    it easy to script fitsort from programs like awk or
                    perl.

      Files
             Input  files  to  dfits shall all comply with FITS format.
             fitsort also supports HIERARCH ESO FITS format.

      See Also
             dfits (1)

