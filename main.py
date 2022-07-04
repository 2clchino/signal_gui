from json import tool
import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import func

# ----------------------------------------

p_count = 20
active = False
interval = 1000
frames = int(100000 / interval)
x_data = []
y_data = []

# ----------------------------------------

def _stop():
    global active
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
        ax.set_ylim(min(y_data)-0.5, max(y_data)+0.5)
    ax.plot(frame, y, "o")

def _set_interval():
    global interval
    interval = int(tf_inter.get())

def _set_plc():
    global p_count
    p_count = int(tf_plc.get())

def _start():
    global ani, fig, active
    print("START")
    ani = animation.FuncAnimation(fig, update, frames=range(frames), interval=interval)
    ani._start()
    active = True

def _reload():
    global x_data, y_data, ani
    x_data = []
    y_data = []
    ax.cla()
    ani._stop()
    ani = None
    ani = animation.FuncAnimation(fig, update, frames=range(frames), interval=interval)
    ani._start()

# ----------------------------------------

root = tkinter.Tk()
root.wm_title("Embedding in Tk anim")
fig = plt.figure()
canvas = FigureCanvasTkAgg(fig, master=root)
toolbar = NavigationToolbar2Tk(canvas, root)
ani = None
ax = fig.add_subplot(111)
canvas.get_tk_widget().pack()

stop_button = tkinter.Button(master=root, text="START", command=_start)
stop_button.pack(side=tkinter.LEFT)
stop_button = tkinter.Button(master=root, text="|▶", command=_stop)
stop_button.pack(side=tkinter.LEFT)
stop_button = tkinter.Button(master=root, text="↻", command=_reload)
stop_button.pack(side=tkinter.LEFT)

inter_button = tkinter.Button(master=root, text="Set Interval", command=_set_interval)
inter_button.pack(side=tkinter.LEFT)
tf_inter = tkinter.Entry(width=20)
tf_inter.insert(tkinter.END,"100")
tf_inter.pack(side=tkinter.LEFT)

inter_button = tkinter.Button(master=root, text="PlotCnt", command=_set_plc)
inter_button.pack(side=tkinter.LEFT)
tf_plc = tkinter.Entry(width=20)
tf_plc.insert(tkinter.END,"20")
tf_plc.pack(side=tkinter.LEFT)
tkinter.mainloop()
