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
- Python 3 Pip

## Citations:
Please cite as:  
*Emanuel Contreras-Cuevas, Humberto Estrada-Lara, Joaquín Barroso-Flores, "UVeh-Vis: a python tool for plotting UV-Vis spectra from excited states calculations" (2023) Git Hub https://github.com/joaquinbarroso/UVeh-Vis*

## Instructions
After getting the source code: 
1. Run
```bash
$ ./setup
```
2. Copy the final line from output
3. Go to /home/_username_
4. Paste the line into `.bashrc` file
5. Exit terminal
6. Open a new terminal and type
```bash
$ UVeh-Vis -h
```
+ Start using it

