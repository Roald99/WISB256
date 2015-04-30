import sys
import time
import math

def sieve(n, outputfile):
    primes = open(outputfile,'w')
    T1 = time.perf_counter()
    list = [False] + (n-2)*[True]
    counter=0
    i=2
    while i <math.sqrt(n) +1:
        if list[i-1] == True:
            counter+=1
            primes.write(str(i)) #kan ook met + maar dit is sneller
            primes.write('\n')
            j=2
            while j*i < n:
                list[j*i-1]=False
                j=j+1
        i+=1
    while i <n:
        if list[i-1]:
            counter+=1
            primes.write(str(i))
            primes.write('\n')
        i+=1
    print(counter)
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    T2 = time.perf_counter()
    print((T2 - T1))
sieve(int(sys.argv[1]), sys.argv[2])
