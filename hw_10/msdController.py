import numpy as np
import msdParamHw10 as P10
from PIDControl import PIDControl
import sys
sys.path.append('..')  # add parent directory
import msdParam as P

class msdController:

    def __init__(self):
        # Instantiates the PD object
        self.zCtrl = PIDControl(P10.kp, P10.ki, P10.kd, P10.F_max, P.beta, P.Ts)
        self.limit = P10.F_max

    def update(self, z_r, u):
        # y_r is the referenced input
        # y is the current state
        z = u[0]
        zdot = u[1]

        # feedback linearized force
        f_fl = 0

        f_tilde = self.zCtrl.PID(z_r, z, False)
        f = f_fl + f_tilde
        f = self.saturate(f)
        return [f]

    def saturate(self, u):
        if abs(u) > self.limit:
            u = self.limit*np.sign(u)
        return u






