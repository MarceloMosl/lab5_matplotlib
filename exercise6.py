import matplotlib.pyplot as plt 
import numpy as np

x = [1, 2, 3, 4, 5]  
y = [1, 4, 9, 16, 25]
categories = ['A', 'B', 'C', 'D', 'E'] 
values = [5, 7, 3, 8, 6]
data = np.random.randn(1000) 
x_scatter = np.random.rand(50) 
y_scatter = np.random.rand(50)

fig, graphs = plt.subplots(2,2)

graphs[0,0].plot(x,y, color='green')
graphs[0,0].set_title("Line Graph")


graphs[0, 1].bar(categories, values)
graphs[0, 1].set_title('Bar Graph')
graphs[1, 0].hist(data, bins=24, edgecolor='black', color='purple')


graphs[1, 0].set_title('Hist')
graphs[1, 1].scatter(x_scatter, y_scatter, color="red")
graphs[1, 1].set_title('Scatter Graph')

plt.tight_layout()
plt.show()