


from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os
from stegano import lsb


# functions
def showImage():
    global filename

    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=(("PNG file","*.png"),("JPG file","*.jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    label.configure(image=img,width=250,height=250,)
    label.image=img

def hideMessage():
    global secret

    msg=text1.get(1.0,END)
    secret = lsb.hide(str(filename),msg)

def showMessage():
    clear_msg=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_msg)

def save():
    secret.save("hidden.png")

root = Tk()
root.title("Steganography_Tool-Images")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#FFDB58")
root.iconphoto(False, PhotoImage(file='D:\PythonInstallation\MyFolder\SteganoProject\steganCode\school.png'))

# frame for heading 
Label(root,text="Steganography_Tool",font="arial 15 bold", bg="#FFDB58", fg="black").place(x=200,y=20)


# first frame 
frame1 = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
frame1.place(x=10,y=80)
label = Label(frame1, bg="black")
label.place(x=40, y=10)

# second frame 
frame2 = Frame(root, bd=3, bg="white", width=340, height=280, relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Robote 15", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# third frame 
frame3 = Frame(root, bd=3, bg="grey", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)
    # button 
button = Button(frame3,text="Open Image", width=10, height=2, font="arial 12 bold", command=showImage).place(x=20, y=30)
button = Button(frame3,text="Save Image", width=10, height=2, font="arial 12 bold", command=save).place(x=180, y=30)

# fourth frame 
frame4 = Frame(root, bd=3, bg="grey", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)
    #button 
button = Button(frame4,text="Hide Message", width=13, height=2, font="arial 12 bold", command=hideMessage).place(x=20, y=30)
button = Button(frame4,text="Show Message", width=13, height=2, font="arial 12 bold", command=showMessage).place(x=180, y=30)















root.mainloop()