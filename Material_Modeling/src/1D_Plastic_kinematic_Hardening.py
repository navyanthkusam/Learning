import numpy as np
#import matplotlib.pyplot as plt

print('''
******************************************************
1D Plasticity Isotropic and kinematic Hardening Model
******************************************************
''')

E = 1000            # Elastic Modulus 
K = 5               # Plastic Modulus 
H = 1000              # Kinematic hardening Modulus 
Y = 20              # yeild stress

#max_ITR = 100       # maximum Iterations
#Tol = 1e-4          # Error Tolerance

strain = np.array([0, 1, 2, -1, 4])*(1e-2)
size    = np.size(strain)                     # size of strain

#initiate the state variables 
''' definition here
sigma              : stress
strain             : total strain
eP                 : plastic strain
q                  : back stress
alpha              : hardening variable
psi                : relative stress (sigma-q)
f..................:yield Function
'''
sigma     = np.zeros(size,dtype=float)
eP        = np.zeros(size,dtype=float)
q         = np.zeros(size,dtype=float)
alpha     = np.zeros(size,dtype=float)


# initial conditions
eP[0]            = 0
q[0]             = 0
alpha[0]         = 0

#start the increments
inc = size-1             # total no of incs
for  n in range(0,size-1):
     # Predictor step
     eP_trial       = eP[n]
     sigma_trial    = E*(strain[n+1] - eP_trial)
     q_trial        = q[n]
     alpha_trial    = alpha[n]
     psi_trial      = sigma_trial - q_trial
     f_trial        = np.abs(psi_trial) - (Y - K*alpha_trial)

     # check if f_trial <= 0
     if f_trial <= 0:
         n=n+1
         #print('Update in Elastic step')
         sigma[n]   = sigma_trial
         eP[n]      = eP_trial
         q[n]       = q_trial
         alpha[n]   = alpha_trial

     # Return map start : Newton Raphson
     else: 
         n=n+1
         delta_gama = f_trial/(E+H+K)
         sigma[n]   = sigma_trial - (delta_gama)*(E)*(np.sign(psi_trial))
         eP[n]      = eP_trial    + (delta_gama)*(np.sign(psi_trial))
         q[n]       = q_trial     + (delta_gama)*(H)*(np.sign(psi_trial))
         alpha[n]   = alpha_trial + (delta_gama)
         
     values = np.array([strain[n], sigma_trial, sigma[n], eP[n], q[n], alpha[n]])
     print((strain[n], sigma_trial, sigma[n], eP[n], q[n], alpha[n]) )


print(strain)
print(sigma)