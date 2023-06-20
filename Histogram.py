"""
-> HISTOGRAMS - represent the distribution of numerical values
"""
#~ Distribution of weights of students in a school

import matplotlib.pyplot as plt
import numpy as np

mu = 50   #>> Average Weight
sigma = 5 #>> Standard Deviation

x = mu + sigma * np.random.randn(10000)

plt.hist(x, 100, density= True, facecolor = "green" )
plt.xlabel("Weight")
plt.ylabel("Probability")
plt.text(40, 0.125, "µ = 50, 'σ' = 5")
plt.axis([30, 70, 0, 0.15])
plt.grid(True)
plt.show()

#>> The above plot shows a Gaussian Bell Curve which is typical for Standard Normal Distribution
