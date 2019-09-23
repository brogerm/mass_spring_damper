import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')  # add parent directory
import msdParam as P
from signalGenerator import signalGenerator
from msdAnimation import msdAnimation
from msdDynamics import msdDynamics
from plotData import plotData


# instantiate reference input classes
msd = msdDynamics()
reference = signalGenerator(amplitude=0.01, frequency=0.02)
fRef = signalGenerator(amplitude=5, frequency=.5)
zRef = signalGenerator(amplitude=2, frequency=0.1)

# instantiate the simulation plots and animation
dataPlot = plotData()
animation = msdAnimation()

t = P.t_start  # time starts at t_start
while t < P.t_end:  # main simulation loop
    # set variables
    Force = [0]

    t_next_plot = t + P.t_plot
    while t < t_next_plot:  # updates control and dynamics at faster simulation rate
        msd.propagateDynamics(Force)  # Propagate the dynamics
        t = t + P.Ts  # advance time by Ts

    # update animation
    animation.draw_msd(msd.states())
    plt.pause(P.t_plot)

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
