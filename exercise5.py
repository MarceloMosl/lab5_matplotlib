import matplotlib.pyplot as plt 
import numpy as np
x = np.random.rand(50) # 50 random x-values between 0 and 1
y = np.random.rand(50) # 50 random y-values between 0 and 1

plt.scatter(x,y) 
plt.xlabel('Something on the X-Axis') 
plt.ylabel('Something else on the Y-Axis') 
plt.title('Scatter Plot Lab5') 
plt.show() 

