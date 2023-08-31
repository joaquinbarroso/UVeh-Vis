while True:
    data = input("Enter filename of Qchem output: ")
    wl = input("Enter starting and final wavelength (nm) of UV-Vis spectra, separated with a comma (,): ")
    dev= input("Enter standard deviation (eV), as a suggestion use 0.4: ")
    try:
        lambda1 = wl.split(',')[0]
        lambda2 = wl.split(',')[1]
        with open(data, 'r') as file:
            lines = file.readlines()
            osc_values = []
            nm_values =[]
            c = 2.998e8  # Speed of light in m/s
            h = 6.626e-34  # Planck's constant in J*s
            ev_to_joules = 1.602e-28  # Conversion factor from eV to joules
            for num, line in enumerate(lines):
                if 'Strength   :' in line:
                    osc = float(line.split()[-1])
                    osc_values.append(osc)
                    prev_line = lines[num - 4].strip()
                    E= float(prev_line.split()[-1])
                    nm=h*c/(E*ev_to_joules)
                    nm_values.append(nm)
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
    except Exception as e:
        print("An error occurred:", e)
    break

