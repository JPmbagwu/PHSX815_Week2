#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:18:46 2023

@author: johnpaulmbagwu
"""

# imports of external packages to use in our code
import sys
import numpy as np

# import our Random class from python/Random.py file
sys.path.append(".")
import Random as rng

# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # default rate parameter for cookie disappearance (cookies per day)
    rate = 1.

    # default number of time measurements (time to next missing cookie) - per experiment
    Nmeas = 1

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-rate' in sys.argv:
        p = sys.argv.index('-rate')
        ptemp = float(sys.argv[p+1])
        if ptemp > 0:
            rate = ptemp
    if '-Nmeas' in sys.argv:
        p = sys.argv.index('-Nmeas')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Nmeas = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # class instance of our Random class using seed
    random = rng.Random(seed)

    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        outfile.write(str(rate)+" \n")
        for e in range(0,Nexp):
            for t in range(0,Nmeas):
                outfile.write(str(random.Exponential(rate))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        print(rate)
        for e in range(0,Nexp):
            for t in range(0,Nmeas):
                print(random.Exponential(rate), end=' ')
            print(" ")