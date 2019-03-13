---
title: 'dfitspy: a dfits|fitsort implementation in python'
tags:
  - fits files
  - Python
  - Astronomy
authors:
  - name: Romain Thomas
    orcid: 0000-0001-8385-3276
    affiliation: 1
affiliations:
 - name: European Southern Observatory, Av. Alonso de Córdoa 3107, 7630355 Vitacura, Santiago, Chile
   index: 1
date: 28 January 2019
bibliography: paper.bib
---

# Summary
The FITS format (Flexible Image Transport System) [@Hanisch:2001] is a widely used format to
store astronomical data. It is used to store a lot of different types of data such as 1D or 2D spectra, 
3D data cubes. It has been developed in the late 1970 to reach its final form almost two decades ago. 
FITS files are built with two components. The data themselves are stored as tables and contains 
any types of data. A header is built containing set of keywords-value pairs aiming at describing 
the data themselves.

Accessing and displaying metadata inside the FITS file is important to get an overview
of what is inside the files. It is particularly useful when dealing with large amount
of files at once. Tools have been already publicly available for years with the dfits 
and fitsort algorithms (the documentation is available here 
https://www.eso.org/sci/software/eclipse/eug/eug/node8.html). The main limitation is 
that they are stand-alone programs useable only in a terminal. They can not be used natively 
inside another program. 

The present python module, dfitspy, is a project that migrates the main dfits 
and fitsort capabilities to python. It is a metadata searcher/displayer for FITS files. 
As dfits and fitsort, dfitspy is able to display in the terminal the result of a metadata 
search and is able to grep certain values of keywords inside large samples of files. 
Therefore it can be used directly with the command line interface. Nevertheless, 
dfitspy can be, and it is its strength, imported as a python module the user can 
use these functionnalities inside another python code or the python interpretor.


Examples:

# dfitspy as a terminal command
A command line interface has been included in dfitspy so it can be used as a Terminal command. A typical command is:\\

``dfitspy -f Test_data/* -k author,time,type --grep 79098.26 --grep STD,TELLURIC``\\

This command will search is all the FITS file contained in the \textit{Test_data} directory. Dfitspy will search for three keywords in the header: author, time and type. Finally, the terminal will display only the file where both 79098.26 and STD,TELLURIC are in the keyword values.

# dfitspy as a Python module


# Availability

dfitspy is an GPL licensed software and the source code is available at https://github.com/astrom-tom/dfitspy. The full documentation is available at https://astrom-tom.github.io/dfitspy/build/html/index.html .

# Acknowledgements

The author would like to thank the Journal of Open Source Software to give the opportunity to researchers to publish software and to the referee of this paper for helpful comments.


# References
