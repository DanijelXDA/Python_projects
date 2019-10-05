import tkinter
import random # For random functions
 
window = tkinter.Tk()
 
def RandomNumber():
    MyRandom = random.randint(1,10)
    dice_thrown.configure(text="Broj: " + str(MyRandom))
 
MyTitle = tkinter.Label(window, text="Generator brojeva",font="Helvetica 20 bold", pady=20)
MyTitle.pack()

window.geometry("300x180")

MyButton = tkinter.Button(window, text="Generisanje", command=RandomNumber, font="Helvetica 16")
MyButton.pack()
 
dice_thrown = tkinter.Label(window, font="Helvetica 20 bold", pady=20)
dice_thrown.pack()
 
window.mainloop()