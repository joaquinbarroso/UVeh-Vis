## About
UVeh_Vis is a utility designed for plotting UV-Vis spectra from QChem output files (and additional features coming soon). This tool operates by entry the relevant file(s), specifying the initial and final wavelength, and providing the standard deviation.

## Getting the source code

Clone the repository:
```bash
$ git clone https://github.com/joaquinbarroso/UVeh-Vis.git
```

This will featch the entire repository called *UVeh-Vis*. 
By default it checks out the main branch.

## UVeh-Vis requieres:
- Python 3
- Matplotlib

## Citations:
Please cite as:__
"Emanuel Contreras-Cuevas, Humberto Estrada-Lara, Joaquín Barroso-Flores, "UVeh-Vis: a python tool for plotting UV-Vis spectra from excited states calculations" (2023) Git Hub https://github.com/joaquinbarroso/UVeh-Vis"

## Instructions
After getting the source code: 
+ Run ./setup
+ Copy the final line from output
+ Go to /home/_username_
+ Paste the line into ".bashrc" file
+ Exit terminal
+ Open a new terminal and type
```bash
$ UVeh-Vis -h
```
+ Start using it

