import sys
#import time
import math
def count(inputfile):
    #T1 = time.perf_counter()
    primes = [] #the list of primes
    fin = open(inputfile, 'r') #open file
    filetext = fin.read(-1) #convert file to string
    atext = filetext.split('\n') # atext means adjusted text (it's a list)
    atext.pop() # delete last place since it is empty
    for  t in atext: #convert the string-integers to int
        primes.append(int(t))
    p1=0
    p2=0
    i=0
    while i < len(primes)-1: #count twinprimes
        if(primes[i]+2==primes[i+1]): #this is the condition for a twin prime
            p2+=1
        i+=1
    lp=primes[-1] # largest prime    
    #output as specified, constants occuring multiple times are given a name
    print('Largest Prime =  ', str(lp))
    print('--------------------------------')
    print('pi(N)         =  ', str(len(primes)))
    logn= math.log(lp)
    nlogn = float(lp)/logn
    print('N/log(N)      =  ', str(nlogn))
    ratio =float(len(primes))/nlogn
    print('ratio         =  ', str(ratio))
    print('--------------------------------')
    print('pi_2(N)       =  ', str(p2))
    c = 0.6601618
    cnlogn = 2*c*float(lp)/(logn*logn)
    print('2CN/log(N)^2  =  ', str(cnlogn))
    print('ratio         =  ', str(float(p2)/cnlogn))
    #T2 = time.perf_counter()
    #print(T2-T1)
count(sys.argv[1])
