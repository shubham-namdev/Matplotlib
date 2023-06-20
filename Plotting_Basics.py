"""
-> Matplotlib - Used for plotting and visualization
"""

#~ Plotting Mathematical Function

import numpy as np
import matplotlib.pyplot as plt

#>> To plot function we need input and output values

x = np.linspace(0, 20, 1000)

#y = np.sin(x)
#
#plt.plot(x, y)
#plt.show()

# y = (10x - 20)^2

#y = (10 * x - 20) ** 2
#
#plt.plot(x, y)
#plt.show()


#~ Visoualizing Values

#nums = np.random.random(100)
#plt.plot(nums, "g^") # green triangles
#plt.show()


#~ Plotting Multiple Graphs

#x = np.linspace(0, 5, 200)
#y1 = 2 * x
#y2 = x ** 2
#y3 = np.log(x)
#
#plt.plot(x, y1)
#plt.plot(x, y2)
#plt.plot(x, y3)
#plt.show()


#~ Subplots
#>>plots that are shown in the same window but independently from each other.
x = np.linspace(0, 5, 200)
y1 = np.sin(x)
y2 = np.log(x)

#plt.subplot(211) #>> 2 rows 1 col 1st position
#plt.plot(x, y1, 'r-')
#
#plt.subplot(212)
#plt.plot(x, y2, 'b--')
#
#plt.show()

#~ Mutliple Plotting Windows & Title - Suptitle & Labeling Axes

#plt.figure("Sine Wave")
#plt.suptitle("Sine Wave of X")
#plt.xlabel("X-Values")
#plt.ylabel("Sin(xi)")
#plt.plot(x, y1, 'b--')
#
#plt.figure("Log")
#plt.suptitle("Log of X")
#plt.xlabel("X-Values")
#plt.ylabel("Log(xi)")
#plt.plot(x, y2, 'g--')
#
#plt.show()


#~ Legends

x = np.linspace(10, 50, 200)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.log(x)

plt.plot(x, y1, 'r-', label = "Sine")
plt.plot(x, y2, 'b-', label = "Cosine")
plt.plot(x, y3, 'g-', label = "Logarithm")
plt.legend(loc = "upper left")
plt.show()

plt.savefig("plot.png")