import numpy as np
import matplotlib.pyplot as plt

x = range(0, 20)
y = [value ** 2 for value in x]

plt.plot(x,y)

plt.annotate("Lowest Point of Something", (0, 0), textcoords="offset points", xytext=(10, 10), ha='center')

highest_x = 19
highest_y = highest_x ** 2
plt.annotate("Highest Point of the same Something", (highest_x, highest_y), textcoords="offset points", xytext=(-50, 2), ha='center')


plt.title("Plot line w/ anotation")
plt.xlabel("X for something")
plt.ylabel("Y for something else")

plt.show()
