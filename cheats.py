import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
from playsound import playsound

class Funkcje:
    def idll():
        print("Error use the Process Hacker v2 or Extreme injector to inject dll :/")
    def macro(chance = random.randint(0,10)):
        if chance == 10:
            print("Now record macro.")
        else:
            print("damn something went wrong try again later :/")
    def infinitejump():
        print("First inject dll idiot")
    def how():
        playsound('resources\how.wav')
        messagebox.askyesno("XD", "Cute dog right?")
    def destroy():
        if(name != ""):
            print("Level Destroyed for 5 minutes!")
    def noclip():
        print("Error x32d23dd. You Don't Have Permissions to Delete System32")
        print("Retry? Y/Y")
        i = input()

        if i == "Y":
            print("Don't Restart pc Becouse you'r pc has been destroyed")

    

root = tk.Tk()
root.title("Logeric v1")
root.geometry("400x400")
root.iconbitmap(r'icon\v1.ico')
root.configure(bg="#424242")

#top
id = tk.Button(root, text="Inject DLL", command=Funkcje.idll)
id.pack(side=tk.TOP)

ij = tk.Button(root, text="Infinite Jump", command=Funkcje.infinitejump)
ij.pack(side=tk.TOP)

dl = tk.Label(root, text="Destroy Level (Enter Level Name)", bg="#424242")
dl.pack(side=TOP)

name = Entry(root, width=20)
name.pack(side=TOP)

dl2 = tk.Button(root, text="Destroy", command=Funkcje.destroy, bg="#aa00ff")
dl2.pack(side=TOP)

#left
Macro = tk.Label(root, text="Record Macro", bg="#424242")
Macro.pack(side=tk.LEFT)

playback = tk.Radiobutton(root, text="Playback", value=1, bg="#424242")
playback.pack(side=LEFT)

record = tk.Radiobutton(root, text="Record", value=2, bg="#424242")
record.pack(side=LEFT)

disable = tk.Radiobutton(root, text="Disable", value=3, bg="#424242")
disable.pack(side=LEFT)

#right
xd = tk.Button(root, text="Funny Dog", command=Funkcje.how)
xd.pack(side=RIGHT)

noclip = tk.Button(root, text="Noclip", command=Funkcje.noclip)
noclip.place(x=250, y=357)


root.mainloop()