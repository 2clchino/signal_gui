from json import tool
import tkinter
from turtle import color
import matplotlib
import numpy as np
print(matplotlib.__version__)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
import matplotlib.animation as animation
import read

# ----------------------------------------

p_count = 20
active = False
interval = 100
frames = int(10000000 / interval)
line = True
plot = True
tim40_ofst = 0
tim100_ofst = 0

cnt40=np.empty(0)
cnt100=np.empty(0)
tim40=np.empty(0)
tim100=np.empty(0)
link=0

t_frames = []

# ----------------------------------------

def _stop():
    global active
    if (active):
        ani.event_source.stop()
    else:
        ani.event_source.start()
    active = not active

def update(frame):
    update_value()
    y_data40 = np.diff(cnt40).tolist()
    y_data100 = np.diff(cnt100).tolist()
    t_frames.append(frame)
    x_data = t_frames
    ax.cla()
    ax.set_ylim(-0.1, max(max(y_data40), max(y_data100)))
    if (len(x_data) > p_count):
        y_data40 = y_data40[len(y_data40)-p_count-1:len(y_data40)-1]
        y_data100 = y_data100[len(y_data100)-p_count-1:len(y_data100)-1]
        x_data = x_data[len(x_data)-p_count-1:len(x_data)-1]
    if line:
        ax.plot(x_data, y_data40, color = "blue")
        ax.plot(x_data, y_data100, color = "orange")
    if plot:
        ax.plot(x_data, y_data40, "o")
        ax.plot(x_data, y_data100, "x")

def update_value():
    global link, cnt40, tim40, cnt100, tim100, tim40_ofst, tim100_ofst
    values = read.value()
    if (tim40_ofst == 0 and tim100_ofst == 0):
        tim40_ofst = values[2]
        tim100_ofst = values[3]
    cnt40 = np.append(cnt40, values[0] * 32 / interval / 1000000)
    cnt100 = np.append(cnt100, values[1] * 32 / interval / 1000000)
    tim40 = np.append(tim40, values[2] - tim40_ofst)
    tim100 = np.append(tim100, values[3] - tim100_ofst)
    link = values[4]

def _set_interval():
    global interval, frames
    interval = int(tf_inter.get())
    frames = int(100000 / interval)

def _set_plc():
    global p_count
    p_count = int(tf_plc.get())

def _init_anim():
    global ani, fig, active, cnt40, cnt100, tim40, tim100, t_frames
    cnt40=np.empty(0)
    cnt100=np.empty(0)
    tim40=np.empty(0)
    tim100=np.empty(0)
    t_frames = []
    ani = animation.FuncAnimation(fig, update, frames=range(frames), init_func=update_value, interval=interval)
    ani._start()
    active = True

def _reload():
    global ani
    ax.cla()
    ani._stop()
    ani = None
    _init_anim()

def _save_gif():
    global ani
    ani.save("test.gif", writer = 'pillow')

def _show_line():
    global line
    line = not line

def _show_plot():
    global plot
    plot = not plot

# ----------------------------------------

root = tkinter.Tk()
root.wm_title("Signal GUI")
fig = plt.figure()
canvas = FigureCanvasTkAgg(fig, master=root)
#toolbar = NavigationToolbar2Tk(canvas, root)
ani = None
ax = fig.add_subplot(111)
ax.grid()
canvas.get_tk_widget().pack()

stop_button = tkinter.Button(master=root, text="START", command=_init_anim)
stop_button.pack(side=tkinter.LEFT)
#stop_button = tkinter.Button(master=root, text="ss", command=_stop)
#stop_button.pack(side=tkinter.LEFT)
stop_button = tkinter.Button(master=root, text="RESET", command=_reload)
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

stop_button = tkinter.Button(master=root, text="line", command=_show_line)
stop_button.pack(side=tkinter.LEFT)
stop_button = tkinter.Button(master=root, text="plot", command=_show_plot)
stop_button.pack(side=tkinter.LEFT)
stop_button = tkinter.Button(master=root, text="EXIT", command=root.quit)
stop_button.pack(side=tkinter.LEFT)
#inter_button = tkinter.Button(master=root, text="SaveGIF", command=_save_gif)
#inter_button.pack(side=tkinter.LEFT)
tkinter.mainloop()
