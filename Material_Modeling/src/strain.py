# (Matrix oprations) : https://www.programiz.com/python-programming/matrix 

"""
Understanding strain

"""

import numpy as np
import plotFunctionFile




#undeformed
X=np.array([[0,0],
            [1,0],
            [1,1],
            [0,1]])

X_pos=X[:,0]  
Y_pos=X[:,1]

noNodes=len(X_pos)

plotFunctionFile.plotFunction(X_pos,Y_pos,'undeformed',321)

u=np.zeros((noNodes,2))
x=np.zeros(noNodes)

x=X+u
x_pos=x[:,0]  
y_pos=x[:,1]


plotFunctionFile.plotFunction(x_pos,y_pos,'exx',322)


u=np.ones((noNodes,2))
x=X+u
x_pos=x[:,0]  
y_pos=x[:,1]

plotFunctionFile.plotFunction(x_pos,y_pos,'eyy',323)

u=2*np.ones((noNodes,2))
x=X+u
x_pos=x[:,0]  
y_pos=x[:,1]

plotFunctionFile.plotFunction(x_pos,y_pos,'ezz',324)



print(u)
