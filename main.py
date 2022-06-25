import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pylab as plt
import numpy as np
import func

# ----------------------------------------

p_count = 4
active = True
x_data = []
y_data = []

# ----------------------------------------

def _stop():
    global active
    print(active)
    if (active):
        ani.event_source.stop()
    else:
        ani.event_source.start()
    active = not active

def update(frame):
    x_data.append(frame)
    y = func.data(frame)
    y_data.append(y)
    if (len(x_data) > p_count):
        ax.lines.pop(0)
        x_data.pop(0)
        y_data.pop(0)
        ax.set_xlim(x_data[0]-0.5, x_data[len(x_data)-1]+0.5)
        ax.set_ylim(y_data[0]-0.5, y_data[len(y_data)-1]+0.5)
    ax.plot(frame, y, "o")

# ----------------------------------------

root = tkinter.Tk()
root.wm_title("Embedding in Tk anim")
fig = plt.figure()
canvas = FigureCanvasTkAgg(fig, master=root)
ax = fig.add_subplot(111)
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=1000)
toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack()
button = tkinter.Button(master=root, text="Stop", command=_stop)
button.pack()
tkinter.mainloop()
