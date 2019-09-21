import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np 
import msdParam as P


class msdAnimation:
    '''
        Create vtol animation
    '''
    def __init__(self):
        self.flagInit = True                  # Used to indicate initialization
        self.fig, self.ax = plt.subplots()    # Initializes a figure and axes object
        self.handle = []                      # Initializes a list object that will
                                              # be used to contain handles to the
                                              # patches and line objects.
        self.blockWidth = P.blockWidth        # block width
        self.blockHeight = P.blockHeight      # block height
        plt.axis([-6*self.blockWidth, 6*self.blockWidth, -0.1, 6*self.blockHeight]) # Change the x,y axis limits
        plt.plot([-4*self.blockWidth, 4*self.blockWidth], [0,0], 'b--')    # Draw a base line
        plt.xlabel('z')

        # Draw vtol is the main function that will call the functions:
        # drawBlock, drawSpring, and drawDamper to create the animation.
    def draw_msd(self, u):
        # Process inputs to function
        z = u[0]        # Horizontal position of block, m

        self.draw_block(z)
        self.draw_wall(z)
        self.draw_spring(z)
        self.draw_damper(z)
        self.ax.axis('equal') # This will cause the image to not distort

        # After each function has been called, initialization is over.
        if self.flagInit == True:
            self.flagInit = False

    def draw_block(self, z):
        x = z - self.blockWidth/2    # x coordinate of lower left corner
        y = 0    # y coordinate of lower left corner
        xy = (x, y)  # Center of block

        # When the class is initialized, a Rectangular patch object will
        # be created and added to the axes. After initialization, the
        # Rectangular patch object will only be updated.
        if self.flagInit == True:
            # Create the Rectangle patch and append its handle
            # to the handle list
            self.handle.append(mpatches.Rectangle(xy,
                width=self.blockWidth, height=self.blockHeight,
                angle=0, fill=True,
                fc='limegreen', ec='black'))
            self.ax.add_patch(self.handle[0])  # Add the patch to the axes
        else:
            self.handle[0].xy = xy

    def draw_wall(self, z):
        x = -6    # x coordinate of lower left corner
        y = 0    # y coordinate of lower left corner
        xy = (x, y)  # Center of block

        # When the class is initialized, a Rectangular patch object will
        # be created and added to the axes. After initialization, the
        # Rectangular patch object will only be updated.
        if self.flagInit == True:
            # Create the Rectangle patch and append its handle
            # to the handle list
            self.handle.append(mpatches.Rectangle(xy,
                width=self.blockWidth/2, height=self.blockHeight + 1,
                angle=0, fill=True,
                fc='black'))
            self.ax.add_patch(self.handle[1])  # Add the patch to the axes
        else:
            self.handle[1].xy = xy

    def draw_spring(self, z):
        wall = -6 + self.blockWidth / 2     # x coordinate of right face of wall
        dx = -wall + z - self.blockWidth / 2  # distance between wall and left face of block
        y = self.blockHeight / 2 * 1.5
        ll = 0.5                                    # link length
        coils = 12                                  # the number of spring coils (must be evenly divisible by 3)
        dy = np.sqrt([ll**2 - (dx / (coils*4))**2])     # change in y
        print(dy)

        X = [wall]
        Y = []

        i = 1
        while i < coils:
            X.append(wall + i*dx/coils)
            i+=1

        j = 1
        while j <= coils/4:
            Y.append(y)
            Y.append(y+dy[0])
            Y.append(y)
            Y.append(y-dy[0])
            j+=1

        # When the class is initialized, a line object will be
        # created and added to the axes. After initialization, the
        # line object will only be updated.
        if self.flagInit == True:
            # Create the line object and append its handle
            # to the handle list.
            spring, = self.ax.plot(X, Y, lw=2, c='black')
            self.handle.append(spring)
        else:
            self.handle[2].set_xdata(X)  # Update the spring
            self.handle[2].set_ydata(Y)

    def draw_damper(self, z):
        x = -6 + self.blockWidth/2
        y = self.blockHeight / 2 * 0.5
        dx = -x + z - self.blockWidth / 2  # distance between wall and left face of block
        xy = (x, y)  # Center of block

        # When the class is initialized, a Rectangular patch object will
        # be created and added to the axes. After initialization, the
        # Rectangular patch object will only be updated.
        if self.flagInit == True:
            # Create the Rectangle patch and append its handle
            # to the handle list
            self.handle.append(mpatches.Rectangle(xy,
                width=dx, height=self.blockHeight/12,
                angle=0, fill=True,
                fc='blue'))
            self.ax.add_patch(self.handle[3])  # Add the patch to the axes
        else:
            self.handle[3].xy = xy


# Used see the animation from the command line
if __name__ == "__main__":

    simAnimation = msdAnimation()    # Create Animate object
    z = 1.5                             # Position of cart, m
    simAnimation.draw_msd([z])  # Draw the mass spring damper system
    #plt.show()
    # Keeps the program from closing until the user presses a button.
    print('Press key to close')
    plt.waitforbuttonpress()
    plt.close()