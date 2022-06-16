import tkinter as tk
import threading
import time

def start():
    thread = threading.Thread(target=count)
    thread.start()

def count():
    global flg
    i = 0
    while 1:
        if flg == False:
            print("動作を途中停止します。")
            flg = True
            break
        else:
            print("カウント",i)
            time.sleep(2)
            i += 1

def stop():
    global flg
    flg = False

root = tk.Tk()

flg = True

btn1 = tk.Button(text="開始",command=start)
btn1.grid(row=0,column=0)

btn2 = tk.Button(text="停止",command=stop)
btn2.grid(row=1,column=0)

root.mainloop()