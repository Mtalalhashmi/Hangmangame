import random
import tkinter as tk
from tkinter import messagebox

score = 0
run = True

while run:
    root = tk.Tk()
    root.geometry('905x700')
    root.title('HANG MAN')
    root.config(bg = '#E7FFFF')
    count = 0
    win_count = 0
     
    index = random.randint(0,858)
    file = open("d:\Python project\words.txt","r")
    l = file.readlines()
    selected_word = l[index].strip('\n')


    x = 250
    for i in range(0,len(selected_word)):
        x += 60
        exec('d{}=tk.Label(root,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))

    al=['a','b','c']
    for let in al:
        exec('{} = tk.PhotoImage(file="{}.png")'.format(let,let))
        

       
        
        

    
    root.mainloop()