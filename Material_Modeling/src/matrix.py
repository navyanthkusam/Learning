# -*- coding: utf-8 -*-
# using concept of operator overloading +,-,*
# https://www.programiz.com/python-programming/operator-overloading
# Continuum mech ; http://www.continuummechanics.org/vectors.html



###############  Tensor  calculations #################

import numpy as np


class Tensor:
    
 #initialize matrix
    def __init__(self,data):
        
        self.ii=data[0][0]
        self.ij=data[0][1]
        self.ik=data[0][2]
        self.ji=data[1][0]
        self.jj=data[1][1]
        self.jk=data[1][2]
        self.ki=data[2][0]
        self.kj=data[2][1]
        self.kk=data[2][2]
    
    #def asArray(self):
        
  #  def __dict__(self):
        
    
# #Tensor length      
#    def mod(self):
#        
#    
# #Tensor Addition
#    def __add__(self,B):      
#      
#    
# #Tensor Subraction
#    def __sub__(self,B):
#       
  
 #conver the data in Tensot to list 
    def asArray(self):
       # Dict=vars(self)
        myArray=np.array([[self.ii,self.ij,self.ik],
                          [self.ii,self.ij,self.ik],
                          [self.ki,self.kj,self.kk]])
        return myArray
        
#works as a string whenever the class is called as  a string
    def __str__(self):
        return "([{0},{1},{2}]\n [{3},{4},{5}]\n [{6},{7},{8}]])".format\
                                     (self.ii,self.ij,self.ik,\
                                      self.ji,self.jj,self.jk,\
                                      self.ki,self.kj,self.kk)
        
#main program startssadfsdf
    
    
A= Tensor(np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]]))

print(A.ii)
print(A)


print(2*A.asArray())

#=A.dotProduct(B)
#print(A.i)
