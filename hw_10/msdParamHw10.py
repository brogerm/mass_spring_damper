# Single link arm Parameter File
import numpy as np
# import control as cnt
import sys
sys.path.append('..')  # add parent directory
import msdParam as P

Ts = P.Ts  # sample rate of the controller
beta = P.beta  # dirty derivative
F_max = P.F_max  # limit on control signal

#  tuning parameters
tr = 2  # part (a)
zeta = 0.707
ki = 1.5  # integrator gain

# desired natural frequency
wn = 2.2/tr
alpha1 = 2.0*zeta*wn
alpha0 = wn**2

# compute PD gains
kp = alpha0**2 * P.m - P.k
kd = alpha1 * P.m - P.b

print('kp: ', kp)
print('ki: ', ki)
print('kd: ', kd)
