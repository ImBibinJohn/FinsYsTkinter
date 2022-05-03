# We start by importing matplotlib
import matplotlib.pyplot as plt

from tkinter import *
import tkinter.font as font
import tkinter as tk
root = tk.Tk()
root.title('fynsYs')
root.geometry("700x700")
root['bg']='#2f516a'

# Plotting a figure of width 6 and height 3
plt_1 = plt.figure(figsize=(6, 3))


# Let's plot the equation y=2*x
x = [1, 2, 3, 4, 5]

y = [3,8,4,10,7]


# plt.plot() specifies the arguments for x-axis
# and y-axis to be plotted
plt.plot(x, y)

# To show this figure object, we use the line,
# fig.show()
plt.show()
