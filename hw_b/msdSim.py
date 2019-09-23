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
    # Get referenced inputs from signal generators
    ref_input = reference.square(t)
    f = fRef.sawtooth(t)
    z = zRef.sin(t)
    # set variables
    Force = [0]
    # update animation
    animation.draw_msd([z[0]])
    # dataPlot.updatePlots(t, ref_input, msd.states(), f)
    plt.pause(0.1)
    t = t + P.t_plot

# Keeps the program from closing until the user presses a button.
print('Press key to close')
plt.waitforbuttonpress()
plt.close()
