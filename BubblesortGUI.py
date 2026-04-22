from tkinter import *
import tkinter as tk
import random

root = tk.Tk()
root.geometry("580x580")
root.title("Sort GUI program")
root.config(background="#FFFFFF")

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

data = [random.randint(50, 350) for _ in range(20)]

def draw(data, color="blue"):
    canvas.delete("all")
    for i, h in enumerate(data):
        canvas.create_rectangle(i*20, 400-h, (i+1)*20, 400, fill=color)
    root.update()

def reset():
    global data
    data = [random.randint(50, 350) for _ in range(20)]
    draw(data)
    start_btn.config(state=tk.NORMAL)
    restart_btn.config(state=tk.DISABLED)

def sort():
    global data
    start_btn.config(state=tk.DISABLED)
    
    # Bubble sort with visualization
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            draw(data, "blue")
            root.after(50)  # Delay for visualization
    
    draw(data, "green")
    restart_btn.config(state=tk.NORMAL)

start_btn = tk.Button(root, text="Start", command=sort)
start_btn.pack(side=tk.LEFT)
restart_btn = tk.Button(root, text="Restart", command=reset, state=tk.DISABLED)
restart_btn.pack(side=tk.LEFT)

draw(data)
root.mainloop()