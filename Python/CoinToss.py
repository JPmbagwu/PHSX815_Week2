#!/usr/bin/env python3

# imports of external packages to use in our code
import sys
import numpy as np

# import our Random class from python/Random file
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

    # default single coin-toss probability for "1"
    prob1 = 0.43
    
    # default single coin-toss probability for "2"
    prob2 = 0.43

    # default number of coin tosses (per experiment)
    Ntoss = 1

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-prob1' in sys.argv:
        p1 = sys.argv.index('-prob1')
        ptemp1 = float(sys.argv[p1+1])
        if ptemp1 >= 0 and ptemp1 <= 1:
            prob1 = ptemp1
    if '-prob2' in sys.argv:
        p2 = sys.argv.index('-prob2')
        ptemp2 = float(sys.argv[p2+1])
        if ptemp2 >= 0 and ptemp2 <= 1:
            prob2 = ptemp2    
    if '-Ntoss' in sys.argv:
        p = sys.argv.index('-Ntoss')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Ntoss = Nt
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
        for e in range(0,Nexp):
            for t in range(0,Ntoss):
                outfile.write(str(random.Categorical(prob1,prob2))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        for e in range(0,Nexp):
            for t in range(0,Ntoss):
                print(random.Categorical(prob1,prob2), end=' ')
            print(" ")

