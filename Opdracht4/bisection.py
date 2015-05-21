import math
#def f(x):
#    return x*x -2 #x*(x-1)-1

def findRoot(f,a,b,epsilon): #Note this algorithm does NOT always find a root even if there is one
    m = (a+b)/2
    if abs(b - a) <= epsilon:
        if f(a)*f(b) <= 0:
                    return m
        else:
            return float("inf")    
    elif findRoot(f,a,m,epsilon) < float("inf"): #optimalisatie, zoekt naar specifiek de kleinste
        return findRoot(f,a,m,epsilon)
    else:    
        return findRoot(f,m,b,epsilon)
        #findRoot complexity O(abs(a-b)/epsilon), worst and best case: O (log(abs(a-b)/epsilon))

def findAllRoots(f,a,b,epsilon): #Same as findRoot does NOT always find all roots
    results = []
    links=a
    rechts = a + epsilon
    midden = a + epsilon/2
    while midden <b:
        #print("ik kom hier")
        links += epsilon
        rechts += epsilon
        midden += epsilon
        if f(links)*f(rechts) <= 0:
            results.append(midden)
    return results
    #complexity O(abs(a-b)/epsilon)
        
#h = findAllRoots(f,-3,3.05,0.01)#(f,-3,3,.1)     
#print (h)        
