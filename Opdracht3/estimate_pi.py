import random
import sys
import math
inputs=sys.argv
ninputs = len(inputs)

def drop_needle(L):
    # uniform in [0,1]
    x = random.random()
    # uniform in [0,2pi]
    a = random.vonmisesvariate(0,0)
    if x + math.cos(a)*L > 1 or x + math.cos(a)*L < 0:
        return 1
    return 0

if (ninputs != 3 and ninputs != 4):
    print("Use : estimate_pi.py N L")
elif (inputs[1].isdigit()!=True):
    print("amount of tries is not an integer")
elif (ninputs==4 or ninputs==3):
    if(ninputs == 4):
        if(inputs[3].isdigit()):
            random.seed(int(inputs[3]))
        else: 
            print("seed is not an integer, using random seed")
    tries = int(inputs[1])
    length = float(inputs[2])
    hits = 0
    count =0
    for x in range(0, tries):
        hits += drop_needle(length)
        count +=1
    print(hits,"hits in", count, "tries")
    kans = hits/float(tries)
    if(length > 1):
        if(kans !=1):
            pi = (2*length - 2*(math.sqrt(length*length -1)  + math.asin(1/length)))/(kans-1)
            print("Pi =", pi)
        else:
            print("Pi is found to be infite, try a larger amount of tries or a different seed")
        
    else:
        print("Pi =", 2*length/kans)
