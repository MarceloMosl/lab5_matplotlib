import matplotlib.pyplot as plt 

categories = ['Marketing', 'Development', 'Sales', 'Support']
values = [20, 35, 25, 20]

plt.pie(values, labels=categories)

plt.title("Pizza Chart")

plt.show()