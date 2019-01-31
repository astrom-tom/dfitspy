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
The fits format (Flexible Image Transport System) [@Hanisch:2001] is a widely used format to
store astronomical data. It has been developed in the late 1970 to reach its 
final form almost two decades ago. It is able to store the data themselves as
well as the metadata describing the data tables.

Accessing and displaying metadata inside the FITS file is important to get an overview
of what is inside the files. It is particularly usefull when dealing with large amount
of files at once. This have been already publicly available for years with the dfits 
and fitsort algorithms (the documentation is available here https://www.eso.org/sci/
software/eclipse/eug/eug/node8.html). The main limitation is that they are stand-alone 
programs useable only in a terminal. They can not be used natively inside a another 
program. 

dfitspy was designed to port the dfits and fitsort capabilities to one of the most used 
language used in science: python. It can be used as an executable (as the original 
programs) but also, and it is its strenghth, as a python module. Therefore fits file 
can be selected in an efficient and fast way based on their metadata values inside 
python programs.


# References
