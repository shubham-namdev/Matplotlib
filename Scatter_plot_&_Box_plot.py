"""
-> Scatter Plot
~ scatter plots are used to represent two-dimensional data using dots.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)
plt.show()


#-> Box Plot
#~ Boxplot diagrams are used, in order to split data into quartiles . We do that
#~ to get information about the distribution of our values. The question we
#~ want to answer is: How widely spread is the data in each of the quartiles.


import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 172 , 4

values = np.random.normal(mu,sigma, 200 )

plt.boxplot(values)
plt.title( "Student's Height" )
plt.ylabel( "Height" )
plt.show()

#>> It only gives information about the spread of the values in the individual quartiles. 