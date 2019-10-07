import numpy as np
import msdParam as P
import sys
sys.path.append('..')  # add parent directory
#from PDControl import PDControl


class msdController:

    def __init__(self):
        # Instantiates the PD object
        self.kp = P.kp
        self.kd = P.kd
        self.limit = P.F_sat

    def update(self, z_r, u):
        # y_r is the referenced input
        # y is the current state
        z = u[0]
        zdot = u[1]

        # linearized force using PD control
        f = self.kp * (z_r - z) - self.kd * zdot

        f = self.saturate(f)
        return [f]

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u






