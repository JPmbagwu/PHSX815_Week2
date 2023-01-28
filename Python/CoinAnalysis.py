#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

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
    # default single coin-toss probability for hypothesis 0
    p0 = 0.5

    # default single coin-toss probability for hypothesis 1
    p1 = 0.9

    haveH0 = False
    haveH1 = False

    if '-prob0' in sys.argv:
        p = sys.argv.index('-prob0')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p0 = ptemp
    if '-prob1' in sys.argv:
        p = sys.argv.index('-prob1')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p1 = ptemp
    if '-input0' in sys.argv:
        p = sys.argv.index('-input0')
        InputFile0 = sys.argv[p+1]
        haveH0 = True
    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True
    if '-h' in sys.argv or '--help' in sys.argv or not haveH0:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -input0 [filename]  name of file for H0 data")
        print ("   -input1 [filename]  name of file for H1 data")
        print ("   -prob0 [number]     probability of 1 for single toss for H0")
        print ("   -prob1 [number]     probability of 1 for single toss for H1")
        print
        sys.exit(1)
    
    Ntoss = 1
    Npass0 = []
    LogLikeRatio0 = []
    Npass1 = []
    LogLikeRatio1 = []

    Npass_min = 1e8
    Npass_max = -1e8
    LLR_min = 1e8
    LLR_max = -1e8
        
    with open(InputFile0) as ifile:
        for line in ifile:
            lineVals = line.split()
            Ntoss = len(lineVals)
            Npass = 0
            LLR = 0
            for v in lineVals:
                Npass += float(v)
                # adding LLR for this toss
                if float(v) >= 1:
                    LLR += math.log( p1/p0 )
                else:
                    LLR += math.log( (1.-p1)/(1.-p0) )
                    
            if Npass < Npass_min:
                Npass_min = Npass
            if Npass > Npass_max:
                Npass_max = Npass
            if LLR < LLR_min:
                LLR_min = LLR
            if LLR > LLR_max:
                LLR_max = LLR
            Npass0.append(Npass)
            LogLikeRatio0.append(LLR)

    if haveH1:
        with open(InputFile1) as ifile:
            for line in ifile:
                lineVals = line.split()
                Ntoss = len(lineVals)
                Npass = 0
                LLR = 0
                for v in lineVals:
                    Npass += float(v);
                    # adding LLR for this toss
                    if float(v) >= 1:
                        LLR += math.log( p1/p0 )
                    else:
                        LLR += math.log( (1.-p1)/(1.-p0) )

                if Npass < Npass_min:
                    Npass_min = Npass
                if Npass > Npass_max:
                    Npass_max = Npass
                if LLR < LLR_min:
                    LLR_min = LLR
                if LLR > LLR_max:
                    LLR_max = LLR
                Npass1.append(Npass)
                LogLikeRatio1.append(LLR)

    title = str(Ntoss) +  " tosses / experiment"
    
    # make Npass figure
    plt.figure()
    plt.hist(Npass0, Ntoss+1, density=True, facecolor='b', alpha=0.5, label="assuming $\\mathbb{H}_0$")
    if haveH1:
        plt.hist(Npass1, Ntoss+1, density=True, facecolor='g', alpha=0.7, label="assuming $\\mathbb{H}_1$")
        plt.legend()

    plt.xlabel('$\\lambda = N_{pass}$')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid(True)

    plt.show()

    # make LLR figure
    plt.figure()
    plt.hist(LogLikeRatio0, Ntoss+1, density=True, facecolor='b', alpha=0.5, label="assuming $\\mathbb{H}_0$")
    if haveH1:
        plt.hist(LogLikeRatio1, Ntoss+1, density=True, facecolor='g', alpha=0.7, label="assuming $\\mathbb{H}_1$")
        plt.legend()

    plt.xlabel('$\\lambda = \\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid(True)

    plt.show()
    
