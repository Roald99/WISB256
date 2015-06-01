import math
from array import array
class Vector():
    __slots__ = {"vector","n"}
    
    def __init__(self,n=1,m=0.0):
        if isinstance(m, list):
            self.vector = array('d',[0.0]*n)
            j=0
            while j<n:
                self.vector[j] = m[j]
                j+=1
            self.n = len(m)
        elif isinstance(m,array):
            self.vector = m
            self.n = len(m)
        else:
            self.vector = array('d',[m]*n)
            self.n = n
    def __str__(self):
        result = ""
        for x in self.vector:
            result += str(x) + "\n"
        result = result[:-1]
        return result
    def scalar(self,alpha):
        lenself = self.n
        result = Vector(lenself)
        i =0
        while i < lenself:
            result.vector[i] = self.vector[i]* alpha
            i+=1
        return result
    def __mul__(self,other):
        if isinstance(other,Vector):
            return self.inner(other)
        else:
            return self.scalar(other)
    def __mulr__(self,other):
        if isinstance(other,Vector):
            return self.inner(other)
        else:
            return self.scalar(other)
    def __add__(self,other):
        lenself = self.n
        lenother = other.n
        if lenself > lenother:
            longest = lenself
            smallest = lenother
        else:
            longest = lenother
            smallest = lenself
        i=0
        result = Vector(longest)
        while i< smallest:
            result.vector[i] = self.vector[i] + other.vector[i]
            i+=1
        if lenself > lenother:
            while i < longest:
                result.vector[i] = self.vector[i]
                i+=1
        else:
            while i < longest:
                result.vector[i] = other.vector[i]
                i+=1
        return result
    def lincomb(self,other,alpha,beta):
        return self.scalar(alpha) + other.scalar(beta)
    def inner(self,other):
        result = 0
        lenself = self.n
        lenother = other.n
        if lenself > lenother:
            smallest = lenother
        else:
            smallest = lenself
        i=0
        while i < smallest:
            result += self.vector[i] * other.vector[i]
            i+=1
        return result
    def norm(self):
        result = 0
        for x in self.vector:
            result += x*x
        return math.sqrt(result)
        
    def project(self,other):
        return self.scalar(self.inner(other) / self.inner(self))
    def projlist(self, others):
        result = Vector(self.n,0.0)
        for x in others:
            result += self.project(x)
        return result
    def clone(self):
        return Vector(self.n,self.vector)
#def GrammSchmidt(v): #v is een
#    k = len(v)
#    j=0
#    result = [Vector(1,0.0)]*k
#    result[0]=v[0].clone()
##    while j<k:
#        result[j] =(result[j]).projlist(v[0:j-1])#result[j] + (result[j]).projlist(v[0:j-1])).scalar(-1)
#        j +=1
##    j=0
#    while j<k:
#        result[j] = (1/result[j].norm()) * result[j]
#        j+=1
#    return result
        
v0 = Vector(2,[3,1])
v1 = Vector(2,[2,2])
u = Vector(3,[2.0,3.14, -5])
#w = GrammSchmidt([v0,v1])
print(u.inner(u))
#print(v1)
#v = Vector(3,3)
#u = Vector(3,array('d',[1,3,4]))
#u.vector = array('d',[1,3,4])
#print(u)
#print(u.norm())
#print(u.lincomb(v,2,1))
