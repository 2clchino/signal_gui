import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import signal
import time
import threading

class Application(tk.Frame):
    index = 0
    data_x = []
    data_y = []
    input = True
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('matplotlib graph')

        #-----------------------------------------------

        # matplotlib配置用フレーム
        frame = tk.Frame(self.master)
        
        # matplotlibの描画領域の作成
        fig = Figure()
        # 座標軸の作成
        self.ax = fig.add_subplot(1, 1, 1)
        # matplotlibの描画領域とウィジェット(Frame)の関連付け
        self.fig_canvas = FigureCanvasTkAgg(fig, frame)
        # matplotlibのツールバーを作成
        self.toolbar = NavigationToolbar2Tk(self.fig_canvas, frame)
        # matplotlibのグラフをフレームに配置
        self.fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # フレームをウィンドウに配置
        frame.pack()
        for i in range(5):
            self.data_x.append(self.index)
            self.data_y.append(self.index)
            self.index+=1
        # グラフの描画
        self.ax.plot(self.data_x, self.data_y)
        # 表示
        self.fig_canvas.draw()
        # ボタンの作成
        draw_button = tk.Button(self.master, text = "Draw Graph", command = self.button_click)
        stop_button = tk.Button(self.master, text = "Signal Stop", command = self.signal_stop)
        # 配置
        draw_button.pack(padx=20, side = 'left')
        stop_button.pack(padx=20, side = 'left')
        #signal.signal(signal.SIGALRM, self.task)
        #signal.setitimer(signal.ITIMER_REAL, 0.1, 1)
        #while True:
        #    time.sleep(1)
        #    self.task()
        #    signal.signal(signal.SIGALRM, self.task)
        #-----------------------------------------------

    def button_click(self):
        # 表示するデータの作成
        self.input = True
        thread = threading.Thread(target=self.plot)
        thread.start()
        
    def plot(self):
        while 1:
            time.sleep(1)
            self.data_x.append(self.index)
            self.data_y.append(self.index)
            if (len(self.data_x)>10):
                cnt = 10
            else:
                cnt = len(self.data_x)
            self.ax.plot(self.data_x[-(cnt-1):], self.data_y[-(cnt-1):])
            self.index+=1
            self.fig_canvas.draw()

    def signal_stop(self):
        self.input = False

root = tk.Tk()
app = Application(master=root)
app.mainloop()