#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Let's import data.txt
filename = 'Data.txt'
dat = np.loadtxt(filename)
list1 = dat.flatten()

# creates histogram
n, bins, patches = plt.hist(list1, density=True, color='b', histtype='step', bins=range(4),alpha=0.75)

# plot formating options
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Plot of the data in Data.txt file')
plt.grid(axis='y', alpha=0.65)
plt.xlim(xmin=-0.5, xmax = 3.5)
plt.xticks(range(3))

#Lets plot it!
plt.savefig("plot_python.pdf", format="pdf", bbox_inches="tight")

# Tweak spacing to prevent clipping of ylabel
plt.tight_layout()

# show figure (program only ends once closed
plt.show()



