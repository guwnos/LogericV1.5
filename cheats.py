import tkinter as tk
from tkinter import *
import random

class Funkcje:
    def idll():
        print("Error use the Process Hacker v2 or Extreme injector to inject dll :/")
    def macro(chance = random.randint(0,10)):
        if chance == 10:
            print("Now record macro.")
        else:
            print("damn something went wrong try again later :/")
    def infinitejump():
        print("This is fake")

    

root = tk.Tk()
root.title("Logeric v1")
root.geometry("400x400")
root.iconbitmap(r'icon\v1.ico')

#top
id = tk.Button(root, text="Inject DLL", command=Funkcje.idll)
id.pack(side=tk.TOP)

ij = tk.Button(root, text="Infinite Jump", command=Funkcje.infinitejump)
ij.pack(side=tk.TOP)

#left
Macro = tk.Label(root, text="Record Macro")
Macro.pack(side=tk.LEFT)

playback = tk.Radiobutton(root, text="Playback", value=1)
playback.pack(side=LEFT)

record = tk.Radiobutton(root, text="Record", value=2)
record.pack(side=LEFT)

disable = tk.Radiobutton(root, text="Disable", value=3)
disable.pack(side=LEFT)


root.mainloop()