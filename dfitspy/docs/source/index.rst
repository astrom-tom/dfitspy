.. dfitspy documentation master file, created by
   sphinx-quickstart on Sat Sep 29 09:54:57 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to dfitspy's documentation!
===================================

|JOSS| |Python36| |Licence|

.. |JOSS| image:: http://joss.theoj.org/papers/10.21105/joss.01249/status.svg
   :target: https://doi.org/10.21105/joss.01249

.. |Licence| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
      :target: http://perso.crans.org/besson/LICENSE.html

.. |Opensource| image:: https://badges.frapsoft.com/os/v1/open-source.svg?v=103
      :target: https://github.com/ellerbrock/open-source-badges/

.. |Python36| image:: https://img.shields.io/badge/python-3.6-blue.svg
.. _Python36: https://www.python.org/downloads/release/python-360/


.. figure:: dfitspy.png
    :width: 750px
    :align: center
    :alt: GUI


Content
=======

.. toctree::
   :maxdepth: 1

   Home <self>
   installation
   usage
   usage_module
   modules
   dfits_fitsort


Change log
==========

**20.7.1**:
        **MAJOR CHANGES!**

        * Move from fitsio to astropy 4.0 as FITS header reading library
        * Bug fix for terminal display when one of the keywords is not found in the fits header. It is replaced by '-'.
        * You can now use *.fits.fz files [thanks to @vertighel for proposing this change!]
        * You can now access the headers from different extenstions! (default is header 0, primary header)

        Thanks to C. Herenz for the two tickets on github that triggered some changes in this version!

        * Bug fix when there is an empty file next to the fits files and the '-f *' or '-f all' is called.
        * Add a '-e' or '- -exact' flag to enforce the extracted keywords to **exactly** match the user-provided one (it will not take all the keywords containing the one given by the user). 

**20.4.1**:
        * Bug fix in display of one of the files does not have all the keywords

**20.3.2**:
        * change in keyword query
        * update in documentation

**19.6.1**:
        * Bug fix with grepping

**19.4.0**:
        * The fitsio library v1.0.1 causes problem for the moment. The version 0.9.11 is therefore forced for the moment until a workaround is found.

**19.3.4:** 
        *.FST*, *.fst* and compressed FITS files (just compressed data, not the header), are allowed.

What is dfitspy?
================

`dfitspy <https://github.com/astrom-tom/dfitspy>`_ is a small project that migrates the main dfits and fitsort capabilities to python.
It is made to search information inside the header of FITS files. The FITS part of the code come from the python 
wrapper of the fits library CFITSIO (see below). dfitspy can be used both as an executable program and as a python
module inside another code.

What is not dfitspy?
====================
dfitspy does not read data inside fits file. Other libraries are doing this very efficiently and dfitspy is not made for that (see fitsio and astropy). It works only on the header and allows you to find common values in an efficient and convenient way. 


Acknowldgements and citation
============================
The python wrapper of the CFITSIO library has been made for the fitsio python library (`fitsio <https://github.com/esheldon/fitsio>`_) and is used in dfitspy.

If you get to use dfitspy for your work, please quote the JOSS `Paper <http://joss.theoj.org/papers/10.21105/joss.01249>`_ [Journal of Open Source software]. Thanks!

----

**Contribute!**
dfitspy is not perfect! It has been primarily developed for my private research and I decided to release i
n the spirit of making the research process as transparent as possible and in the hope it can be used by
other people. If you have any comment or anything you would like to be added to dfitspy, or, even better,
if you want to modify it, you can either do it yourself or please feel free to contact me! ---> **rthomas@eso.org, the.spartan.proj@gmail.com**. In any case, you can find the source code `here <https://github.com/astrom-tom/dfitspy>`_.

----

.. warning::

	**Copyright**

	dfitspy is a free software: you can redistribute it and/or modify it under
	the terms of the GNU General Public License as published by the Free Software Foundation,
	version 3 of the License.

	dfitspy is distributed without any warranty; without even the implied warranty of merchantability
	or fitness for a particular purpose.  See the GNU General Public License for more details.

	You should have received a copy of the GNU General Public License along with the program.
	If not, see http://www.gnu.org/licenses/ .

----

.. warning::

	**Disclaimer**

	dfitspy is not supported nor endorsed by the European Southern Observatory [ESO].
