import random
import tkinter as tk
from tkinter import *
root= tk.Tk()
root.geometry("312x324")
k = tk.Entry(root, width=40)
k.pack(pady=10)
def passg(k):
    x=[]
    for i in range(33,126):
        x.append(chr(i))
    paswd=''
    for i in range(k):
        paswd+=random.choice(x)
    
    