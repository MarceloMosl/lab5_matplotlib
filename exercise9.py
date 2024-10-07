import numpy as np
import matplotlib.pyplot as plt



dataset1 = np.random.normal(60, 10, 100) # 100 data points around mean 60
dataset2 = np.random.normal(70, 15, 100) # 100 data points around mean 70
dataset3 = np.random.normal(80, 5, 100) # 100 data points around mean 80

plt.boxplot([dataset1, dataset2, dataset3])

plt.title("Marcelo's Box Plot")
plt.ylabel("Values")
plt.xticks([1, 2, 3], ["Group A - Mean 60", "Group B - Mean 70", "Group C - Mean 80"])

plt.show()

