---
title: 'UVeh-Vis: A Python program for Absorption spectra plotting from QC calculations'
tags:
  - Python
  - Chemistry
  - Excited States
  - C
  - Absorption Spectra
authors:
  - name: Emanuel Contreras-Cuevas
    orcid: 0009-0000-8406-0665
    equal-contrib: true
    affiliation: 1
  - name: Humberto Estrada-Lara
    equal-contrib: true 
    affiliation: 1
  - name: Joaquin Barroso-Flores
    orcid: 0000-0003-0554-7569
    corresponding: true
    affiliation: 2
affiliations:
 - name: Centro Conjunto de Investigación en Química Sustentable UAEM-UNAM, Universidad Autónoma del Estado de México, México
   index: 1
 - name: Centro Conjunto de Investigación en Química Sustentable UAEM-UNAM, Universidad Nacional Autónoma de México, México
   index: 2
date: 22 May 2024
bibliography: paper.bib
---


# Summary

Absorption spectroscopy is one of the most used analytical techniques due to
the important information that can be obtained from the resulting spectra for 
cualitative and cuantitative purposes. It is based on the absorption of electromagnetic
radiation by a molecular system, this implies the transition from an electronic 
ground state to a higher energy state, an excited state [@Ceroni2014]. The characterization 
and theoretical prediction of such states have been widely studied, the influence of
an enormous amount of factors over their properties, and therefore, its spectrum,
have turned the comparizon between absorption spectra into a powerful tool to describe 
not only properties of molecular systems, but also the accurateness of theoretical
methods. Here we present `UVeh-Vis`, a python program to extract and treat excited states
information from quantum chemical calculations in oder to plot UV-Vis spectra.

# Statement of need

Excited states and UV-Vis spectra calculations have become a daily basis task done 
when working with light-driven reactions or processes in molecular systems, it 
comes with a constant task of comparising between UV-Vis spectra of different systems 
(or methods), for this, `UVeh-Vis` is a very useful python program that facilitates
such tasks, it is focused on the obtention of UV-Vis spectra using excited states
information extracted from quantum chemical output files through an easy-to-use
and customizable execution. Through an auxiliary C-based code, it accelerates its
reading and writting routines. Several projects with the same objective have
been published on github or gitlab, but, none of them offers the variety of options
and personalization that our code offers.

`UVeh-Vis` is capable of processing several files obtained from renowned quantum
chemistry packages, such as Orca, Gaussian and Q-chem, and produce an UV-Vis plot
from extracted data using other option to modify and fit such plot as needed. Our
program offers an easy-to-use execution and installation for Computational chemistry
related and non-related users. Currently, `UVeh-Vis` can handle excited states information
coming from TDA/TDDFT and RAS-CI calculations.



