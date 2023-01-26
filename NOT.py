import tkinter
from tkinter import *
from tkinter import filedialog
win= tkinter.Tk()
# ==================================1
win.title("notpad App")
win.geometry("400x500")
win.resizable(FALSE,FALSE)
# ==================================2
def open_text():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = filedialog.askopenfilename(title='Open a file', initialdir='C:/Users/rizrayaneh/Desktop', filetypes=filetypes)
    f=open(filename)
    tex.insert(END,f.read())
# ===========================================3
def sav_user():
    file = open('Failed.text', 'w')
    file.write('whatever')
    file.close()
    
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = filedialog.asksaveasfilename(title='savfile', initialdir='C:/Users/rizrayaneh/Desktop', filetypes=filetypes)
    f=open(filename,"w")
    f.write(tex.get("0.0",END))
    f.close()
with open('Failed.py', 'w') as file:
    
    file.write('whatever')
# ===========================================4
def yaddasht():
    help_win=Toplevel(win)
    help_win.resizable(FALSE,FALSE)
    help_win.config(bg="burlywood")
    help_win.geometry("300x100")
    lam= Label(help_win,text="amirhosenvahidi6@gmail.com",bg="burlywood",font=("Ebrima",15))
    lam.pack()
# ===========================================5
def donothing():
    filewin = Toplevel(win)
    button = Button(win, text="Do nothing button")
    button.pack()
   
menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_text)
filemenu.add_command(label="Save", command=sav_user)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=win.quit)

menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

editmenu.add_separator()

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=yaddasht)
menubar.add_cascade(label="Help", menu=helpmenu)
win.config(menu=menubar)
# =================================================================6
tex= Text(win,font=("Consolas",11),height=200,bg="beige")
tex.pack()
# =================================================================7







win.mainloop()