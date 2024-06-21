'''from tkinter import *
win=Tk()   #this is a class
win.geometry('600x400')
# win.resizable(0,0)+++
win.title("SWITCHBLADE")
# lbl.pack()
#first entry
lbl=Label(win,text="Your Name",font=('Arial',20))
lbl.config(fg="black",bg="red")
lbl.grid(row=0,column=0,padx=10,pady=10)
ent1=Entry(win,font=('Arial',20))
ent1.grid(row=0,column=1,padx=10,pady=10)

#second entry 

lbl1=Label(win,text="Your Roll no.",font=('Arial',20))
lbl1.config(fg="black",bg="light blue")
lbl1.grid(row=1,column=0,padx=10,pady=10)
ent2=Entry(win,font=('Arial',20))
ent2.grid(row=1,column=1,padx=10,pady=10)

#third entry

lbl2=Label(win,text="Gender",font=('Arial',20))
lbl2.config(fg="black",bg="red")
lbl2.grid(row=2,column=0,padx=10,pady=10)
#radio button
     #for male
a=StringVar()
a.set(" ")
rad=Radiobutton(win,text="male",font=("Jokerman",20),variable=a,value="male")
rad.grid(row=2,column=1,padx=70,pady=10,sticky="w")
#radio button 
     #for female
rad1=Radiobutton(win,text="Female",font=("Jokerman",20),variable=a,value="Female")
rad1.grid(row=2,column=1,padx=70,pady=10,sticky="e")  

#forth entry

lbl2=Label(win,text="Language",font=('Arial',20))
lbl2.config(fg="black",bg="red")
lbl2.grid(row=3,column=0,padx=10,pady=10)
#LABLE FOR LANGUAGE
c=BooleanVar()
chk1=Checkbutton(win,text="C",font=("Arial",20),variable=c)
chk1.grid(row=3,column=1,padx=10,pady=10,sticky="w")

d=BooleanVar()
chk1=Checkbutton(win,text="C++",font=("Arial",20),variable=d)
chk1.grid(row=3,column=1,padx=70,pady=10,sticky="w")

e=BooleanVar()
chk1=Checkbutton(win,text="Python",font=("Arial",20),variable=e)
chk1.grid(row=3,column=1,padx=155,pady=10,sticky="w")

#fifth entry

def click():
     name=ent1.get()
     print("Your name is:"name)
     roll=ent2.get()
     print("Your rollno."roll)
     sex=a.get()
     print("Gender:"sex)
     Language =[]
     if c.get:
          Language.append("C")
     if d.get:
          Language.append("C++")     
     if e.get:
          Language.append("Python")
     print("Language: , ".join(Language))
     # lan=chk1.get()
     # print(lan)
     print("I am done")
but=Button(win,text="Submit",font=("Arial",20),command=click)
but.grid(row=6,column=0,columnspan=2,pady=20)

win.mainloop()'''


# ###################################### # # # #######################
# from tkinter import*

# from tkinter.ttk import Combobox
# win=Tk()
'''from tkinter import*
from tkinter.ttk import Combobox

win=Tk()
win.title("combobox Example")
win.resizable(0,0)
win.geometry('800x200')

def combobox_selected(event):
     c= cmb.get()
     if c=="opt1":
          lbl.config(bg="red",text=f"i am {c}")
     if c=="opt2":
          lbl.config(bg="yellow",text=f"i am {c}")   
     if c=="opt3":
          lbl.config(bg="blue",text=f"i am {c}")  

lbl=Label(win,font=("Arial",20))
lbl.pack()

lst=['opt1','opt2','opt3']
cmb=Combobox(win,value=lst)
cmb.set("Chosse")
cmb.pack()
cmb.bind("<<ComboboxSelected>>",combobox_selected)
print(win.mainloop())'''


################################################################
"""CLICK BOX"""
'''from tkinter import*
from tkinter.ttk import Combobox

win=Tk()
win.title("combobox Example")
win.resizable(0,0)
win.geometry('800x200')

def click():
     roll=ent.get()
     name=ent2.get()
     gen=a.get()
     st=" "
     if c.get()==1:
          st=st+"C"
     if c.get()==1:
          st=st+"C++"
     if c.get()==1:
          st=st+"Python"
     sem=combobox.get()  
     print(roll,name,gen,st)   
but=Button(win,text="subumit",font=("Arial",20),command=click)   
but.grid(row=6,column=0,columnspan=2)  '''

#################################
from tkinter import*
from tkcalendar import DateEntry

win=Tk()
win.title("Data Picker Example")
win.geometry("800x200")

data_entry = DateEntry(win)
data_entry.pack()
win.mainloop()


