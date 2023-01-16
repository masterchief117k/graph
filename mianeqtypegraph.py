import matplotlib.pyplot as plt
import numpy as np
from sympy import *

x = symbols('x')
equation = input("Enter the equation of the graph (in terms of x): ")
y = sympify(equation)

f = lambdify(x, y, 'numpy')

x_min = float(input("Enter the minimum x value for the graph: "))
x_max = float(input("Enter the maximum x value for the graph: "))
x_vals = np.linspace(x_min, x_max, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()