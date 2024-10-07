import matplotlib.pyplot as plt
import numpy as np


categories = ['Group 1', 'Group 2', 'Group 3']
value1 = np.array([5, 7, 3])
value2 = np.array([6, 8, 4])
value3 = np.array([4, 3, 5])

# Use the categories , value1 , value2 , and value3 lists above.
# Create a stacked bar plot where each category has the three different
# values stacked.
# Add labels for the x-axis and y-axis.
# Add a legend to indicate the different parts of the stack.


plt.bar(categories, value1, color='r')
plt.bar(categories, value2, bottom=value1, color='b')
plt.bar(categories, value3, bottom=value1+value2, color='g')

plt.xlabel("Teams")
plt.ylabel("Score")
plt.legend(["Group 1", "Group 2", "Group 3"])
plt.title("Scores by Teams in 4 Rounds")

plt.show()