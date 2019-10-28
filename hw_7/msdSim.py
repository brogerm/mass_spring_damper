import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('..')  # add parent directory
import msdParam as P
from msdController import msdController
from signalGenerator import signalGenerator
from msdAnimation import msdAnimation
from msdDynamics import msdDynamics
from plotData import plotData


# instantiate reference input classes
msd = msdDynamics()
ctrl = msdController()
reference = signalGenerator(amplitude=1, frequency=0.05)

# instantiate the simulation plots and animation
dataPlot = plotData()
animation = msdAnimation()

t = P.t_start  # time starts at t_start
while t < P.t_end:  # main simulation loop
    r = reference.square(t)

    t_next_plot = t + P.t_plot
    while t < t_next_plot:  # updates control and dynamics at faster simulation rate
        u = ctrl.update(r[0], msd.states())
        msd.propagateDynamics(u)  # Propagate the dynamics
        t = t + P.Ts  # advance time by Ts

    # update animation
    animation.draw_msd(msd.states())
    dataPlot.updatePlots(t, r, msd.states(), u)
    plt.pause(P.t_plot)

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
