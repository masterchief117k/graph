import matplotlib.pyplot as plt

x = []
y = []

num_points = int(input("How many points would you like to plot on the graph? "))

for i in range(num_points):
    x_val = float(input("Enter the x value for point {}: ".format(i+1)))
    y_val = float(input("Enter the y value for point {}: ".format(i+1)))
    x.append(x_val)
    y.append(y_val)

plt.plot(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()