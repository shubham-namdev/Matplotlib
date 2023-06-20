"""
-> Pie Charts
Pie charts are used to display proportions of numbers.
"""

import matplotlib.pyplot as plt
import numpy as np


#>> Plotting how many percent students like which sport

sports = ("Cricket", "Football", "Basket-Ball", "Hockey", "None")

values = (45, 23, 20, 10, 2)

plt.pie(values, labels=sports, autopct="%.2f%%", shadow=False, colors=("blue", "yellow", "orange", "green", "red"))
plt.title("Sport Preference")
plt.show()
