#!/bin/bash

curl -O https://raw.githubusercontent.com/joaquinbarroso/UVeh-VIs/main/ReadES2.py
curl -O https://raw.githubusercontent.com/joaquinbarroso/UVeh-VIs/main/Plot.py

chmod +x Plot.py ReadES2.py

python3 Plot.py

rm Plot.py ReadES2.py
