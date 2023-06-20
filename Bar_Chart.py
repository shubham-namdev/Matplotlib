"""
-> Bar Charts
"""
#>> Plotting result of students

import matplotlib.pyplot as plt
import numpy as np

subjects = ("English", "Maths", "Science", "Civics")

ben = (75, 65, 80, 84)
gwen = (85, 90, 92, 72)
julie = (95, 86, 90, 85)
kevin = (70, 95, 95, 90)

index = np.arange(4)
width = 0.2

plt.bar(index, ben, width=width, label = "Ben", color = "green")
plt.bar(index + width, gwen, width=width, label = "Gwen", color = "pink")
plt.bar(index + 2 * width, julie, width=width, label = "Julie" , color = "blue")
plt.bar(index + 3 * width, kevin, width=width, label = "Kevin", color = "black")


plt.xticks(index + width, subjects)

plt.ylim(0, 100)
plt.title("Exam Results")
plt.ylabel("Obtained Marks")
plt.xlabel("Subjects")
plt.legend(loc = "upper left")
plt.show()



