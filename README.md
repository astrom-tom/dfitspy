What is dfitspy?
================

The full documentation can be found here: https://astrom-tom.github.io/dfitspy/build/html/index.html

dfitspy is a small project that migrates the main dfits and fitsort capabilities to python.
It is made to search information inside header of fitsfile. The fits part of the code come from the pythion 
wrapper of the fits library CFITSIO (see below). dfitspy can be used both as an executable program and as a python
module inside another code.


What is not dfitspy?
====================
dfitspy does not read **data** inside fits file. Other libraries are doing this very efficiently and dfitspy 
is not made for that (see fitsio and astropy). It works only on the header and allows you to search/display the fits files header. It is also made to find common values in large amount of fits files in a very fast way. 


Installation?
=============

The last dfitspy version is v19.1.5 and is available in the pypi test repository. To install it::

     pip install -i https://test.pypi.org/simple/ dfitspy --user

Using this command will allow you not to have to install any other package. Pip will install what is mis
sing for you.


----

**Contribute!**
dfitspy is not perfect! It has been primarily developed for my private research and I decided to release 
in the spirit of making the research process as transparent as possible and in the hope it can be used by
other people. If you have any comment or anything you would like to be added to dfitspy, or, even better,
if you want to modify you can either do it yourself or please feel free to contact me! ---> **the.spartan.proj@gmail.com**

----


**Copyright**

dfitspy is a free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software Foundation,
version 3 of the License.

dfitspy is distributed without any warranty; without even the implied warranty of merchantability
or fitness for a particular purpose.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with the program.
If not, see http://www.gnu.org/licenses/ .

----

**Disclaimer**

dfitspy is not supported nor endorsed by the European Southern Observatory [ESO].


Acknowledgments
===============
The python wrapper of the CFITSIO library have been made for the fitsio python library (https://github.com/esheldon/fitsio) and is used in dfitspy.




