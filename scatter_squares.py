import matplotlib.pyplot as plt

#plots a single point, must pass (x,y) value
#s argument sets the size of the dots
# plt.scatter(2, 4, s=200)

#set multiple values
# matplotlib reads one value from each list as it plots each point
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.scatter(x_values, y_values, s=100)

#instead of writing out lists, we can use loops to do calculations
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

#using edgecolor='none' removes black outlines that may mash together
# we will only see a blue line
#using c='red' will change color of plot points to red
# you can also define a color using an RGB formula/tuple
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=40)

#set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

#set the range for each axis
# requires 4 values, min and max values for x-axis and
# min and max values for y-axis
plt.axis([0, 1100, 0, 1100000])

plt.show()