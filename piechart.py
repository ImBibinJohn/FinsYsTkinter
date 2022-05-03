5# Import libraries
from matplotlib import pyplot as plt
import numpy as np
from tkinter import *
# import tkinter.font as font
# import tkinter as tk
# root = tk.Tk()
# root.title('fynsYs')
# root.geometry("700x700")
# root['bg']='#2f516a'

# Creating dataset
cars = ['AUDI', 'BMW', 'FORD',
		'TESLA', 'JAGUAR', 'MERCEDES']

data = [23, 17, 35, 29, 12, 41]

# Creating plot
fig = plt.figure(figsize =(10, 7))
# fig, ax = plt.subplots()
# ax.set_facecolor((1.0, 0.47, 0.42))
fig.patch.set_facecolor('#243e55')
plt.pie(data, labels = cars)

# show plot
plt.show()


