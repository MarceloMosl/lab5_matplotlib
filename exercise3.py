import matplotlib.pyplot as plt

categories = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']
values = [10, 15, 7, 12, 5]

plt.bar(categories, values)
plt.xlabel('Fruit Categories')
plt.ylabel('Quantity')
plt.title("Fruit Quantity Distribution")
plt.show()