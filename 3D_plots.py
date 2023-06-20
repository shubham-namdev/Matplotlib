"""
#-> 3D Plotting using matplotlib

"""
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d #~ This module is needed for 3d plotting
import numpy as np


z = np.linspace(0, 20, 100)
x = np.sin(z)
y = np.cos(z) 

ax = plt.axes(projection = "3d")
ax.plot3D(x, y, z)
plt.show()


#~ Surface Plots

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d #~ This module is needed for 3d plotting
import numpy as np

ax = plt.axes(projection = "3d")

def z_fun(x, y) :
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y) #~converting the x- and y-vectors into matrices using the meshgrid function

Z = z_fun(X, Y)
ax.plot_surface(X, Y, Z)
plt.show()
