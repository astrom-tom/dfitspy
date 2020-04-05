.. _installation:

|JOSS| |Python36| |Licence|

.. |JOSS| image:: http://joss.theoj.org/papers/10.21105/joss.01249/status.svg
   :target: https://doi.org/10.21105/joss.01249

.. |Licence| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
      :target: http://perso.crans.org/besson/LICENSE.html

.. |Opensource| image:: https://badges.frapsoft.com/os/v1/open-source.svg?v=103
      :target: https://github.com/ellerbrock/open-source-badges/

.. |Python36| image:: https://img.shields.io/badge/python-3.6-blue.svg
.. _Python36: https://www.python.org/downloads/release/python-360/


Installation
============

dfitspy is written in python 3.6 (and work in python 3.8.2). It needs only the following libraries:

* Numpy v1.14.3: Numerical python
* fitsio v0.9.11: fitsio library
* python-magic v0.4.15: file type checker

Other libraries are used, but they are all part of the standard python library. As such no extra installations are needed.

.. warning ::

        for Mac user you might get problem with the libmagic library.
        You might want to install py37-magic from macports.
        Thanks to A. Mehner for this.

1-from the python repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The last dfitspy version is v20.4.1 and is available in the main pypi repository. To install it::

     pip install dfitspy --user

Using this command will allow you not to have to install any other package. Pip will install what is missing for you.


2-From the local the github repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The installable package can be found in the github directory under the ''dist'' directory. Take the last version and run::

	pip install dfitspy-X.Y.Z.tar.gz --user

In the version number of dfitspy, X is the year, Y is the month, and Z is the number of revisions in that month. Therefore 19.1.5 means, fifth revision of January 2019.


This will install dfitspy.
