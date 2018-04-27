# Town distances generator for towns placed randomly on a 2d map

# -------------------------------------------------------
# "BEER-WARE LICENSED":
# As long as you retain this notice, you can do what you
# want with this. If we meet some day, and you think this
# program is worth it, you may buy me a beer in return.
#
# Author: Clint Gamlin
# Email: cdgamlin@gmail.com
# -------------------------------------------------------

# -------------------------------------------------------
# Updated to Python 3 and now complies with all PEPs
# Author: William Hingston
# -------------------------------------------------------

import os
import sys
from math import sqrt
from random import random

if len(sys.argv) != 4:
    print("Error!: Incorrect arguments")
    print("Usage: python createmap.py NUMBER_OF_TOWNS MAX_DISTANCE OUTPUT_FILE_NAME")
    exit()

num_towns = int(sys.argv[1])
max_dist = int(sys.argv[2])
file_name = sys.argv[3]

try:
    os.remove(file_name)
except OSError:
    pass

posTown = [(random() + 1j * random()) * max_dist / sqrt(2) for x in range(num_towns)]

with open(file_name, "a") as file:
    file.write(str(num_towns) + "\n")

for i in range(1, num_towns):
    for j in range(i):
        with open(file_name, "a") as file:
            file.write(str(int(abs(posTown[i] - posTown[j])) + 1) + " ")
    with open(file_name, "a") as file:
        file.write("\n")
