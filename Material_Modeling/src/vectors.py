# -*- coding: utf-8 -*-
# using concept of operator overloading +,-,*
# https://www.programiz.com/python-programming/operator-overloading
# Continuum mech ; http://www.continuummechanics.org/vectors.html



###############  vector  calculations #################

import numpy as np


class Vector:
    
 #initialize vector 
    def __init__(self,data):
        self.i=data[0]
        self.j=data[1]
        self.k=data[2]
    
 #vectorlength      
    def mod(self):
        return np.sqrt((self.i)**2+(self.j)**2+(self.k)**2)
    
 #vector Addition
    def __add__(self,b):      
        return Vector([self.i+b.i,self.j+b.j,self.k+b.k])
    
 #vector Subraction
    def __sub__(self,b):
        return Vector([self.i-b.i,self.j-b.j,self.k-b.k])
   
#works as a string whenever the class is called as  a string
    def __str__(self):
        return "[{0},{1},{2}]".format(self.i,self.j,self.k)
    
#Dot product     
    def dot(self,b):
        return self.i*b.i+self.j*b.j+self.k*b.k
     
#Cross product    
    def cross(self,b):
        c=Vector([0,0,0])
        c.i=self.j*b.k-self.k*b.j
        c.j=self.k*b.i-self.i*b.k
        c.k=self.i*b.j-self.j*b.i
        return c
        

#main program starts
    
    
a=Vector([1,2,3])
b=Vector([3,4,5])

print(a)
print(a.mod())
print(a+b)
print(a-b)
print(a.dot(b))
print(a.cross(b))

#=A.dotProduct(B)
#print(A.i)