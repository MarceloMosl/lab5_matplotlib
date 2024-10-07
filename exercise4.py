import matplotlib.pyplot as plt 
import numpy as np 

data = np.random.normal(0, 1, 500) # 500 data points from a normal distribution

plt.hist(data, bins=25, edgecolor='green') 
plt.xlabel('X') 
plt.ylabel('Y') 
plt.title('Histogram Lab5') 
plt.show() 
