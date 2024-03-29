# Inverted Pendulum Parameter File
import numpy as np
import control as cnt

# Physical parameters of the block
m = 5.0       # kg
k = 3.0       # N/m
b = 0.5     # N m s

# Parameters for animation of block
blockWidth = 2  # units
blockHeight = 2   # units

# Initial conditions
z0 = 1.5    # initial displacement (m)
zdot0 = 0     # initial velocity (m/s)

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 50.0  # End time of simulation
Ts = 0.01  # sample time for simulation
t_plot = 0.1  # the plotting and animation is updated at this rate

# PD gains
kp = 4.5
kd = 14.5

# dirty derivative parameters
sigma = 0.05  # cutoff freq for dirty derivative
beta = (2.0*sigma-Ts)/(2.0*sigma+Ts)  # dirty derivative gain

# saturation limit
F_sat = 6
F_max = F_sat
