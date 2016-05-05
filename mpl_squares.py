#first import pyplot module using alias
import matplotlib.pyplot as plt

#must define input values that start with 1,
# python assumes the x-value when not defined is 0
input_values = [1, 2, 3, 4, 5]
#pass squares into plot function
squares = [1, 4, 9, 16, 25]

#available customizations to improve readability of plot
#linewidth controls thickness of line that the plot generates
plt.plot(input_values, squares, linewidth=5)

#set chart title and label axes
#fontsize control size of tex on the chart
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#set size of tick labels
plt.tick_params(axis='both', labelsize=14)

#show() opens up the viewer
plt.show()