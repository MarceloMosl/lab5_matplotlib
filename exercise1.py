import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]


plt.plot(x, y)
plt.xlabel('Years')
plt.ylabel('Salary per Year')
plt.title("Avg Salary per Year of Experience")
plt.show()