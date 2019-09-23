# Inverted Pendulum Parameter File
import numpy as np
import control as cnt

# Physical parameters of the block
m = 5       # kg
k = 3       # N/m
b = 0.5     # N m s

# Parameters for animation of block
blockWidth = 2  # units
blockHeight = 2   # units

# Initial conditions
z0 = 1    # initial displacement (m)
zdot0 = 0     # initial velocity (m/s)

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 50.0  # End time of simulation
Ts = 0.01  # sample time for simulation
t_plot = 0.1  # the plotting and animation is updated at this rate

# saturation limits
F_max = 5.0                # Max Force, N

