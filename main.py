from ast import While
from tkinter import *
import tkinter as tk
from tkinter import Scale
from tkinter import colorchooser,filedialog,messagebox
from PIL import ImageGrab
window = Tk()

window.state("zoomed")
window.title("Drawing & Learning")
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='palette.png'))
eraser_color = "white"
brush_color = "black"

pallete_image=PhotoImage(file=r'palette.png')
canvas = Canvas(window,bg="white",bd=5,relief=RIDGE,cursor="spraycan",height=700,width=1400)
canvas.place(x=10,y=100)

frame1=Frame(window,height=100)
frame1.pack(side=TOP,fill=X)
width_label=Label(frame1,text='x =')
width_label.place(x=920,y=22)
width_spin=tk.Spinbox(frame1,from_=5,to=1000,width=5)
width_spin.bind('<Return>',lambda e: change())
width_spin.place(x=945,y=22)

height_label=Label(frame1,text='y =')
height_label.place(x=920,y=50)
height_spin=tk.Spinbox(frame1,from_=5,to=1000,width=5)
height_spin.bind('<Return>',lambda e: change())
height_spin.place(x=945,y=50)

def change():
    width=width_spin.get()
    height=height_spin.get()
    canvas.config(width=width,height=height)
    

def canvas_color():
    global eraser_color
    color = colorchooser.askcolor()
    canvas.configure(bg=color[1])
    eraser_color = color[1]

def Save():
    file_name = filedialog.asksaveasfilename(defaultextension=".jpg")

    x= window.winfo_rootx() + canvas.winfo_rootx()
    y= window.winfo_rooty() + canvas.winfo_rooty()

    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()

    ImageGrab.grab().crop((x,y,x1,y1)).save(file_name)
    messagebox.showinfo("Notifications","image is saved as " + str(file_name))
    
def Erase():
    global brush_color
    brush_color = eraser_color

def Clear():
    canvas.delete("all")

def paint(event):
  x1,y1=(event.x-2),(event.y-2)
  x2,y2=(event.x+2),(event.y+2)
#   canvas.create_line(x1,y1,x2,y2,fill=brush_color,width=brush_size.get(),smooth=True,capstyle='round')
  canvas.create_oval(x1,y1,x2,y2,fill=brush_color,outline=brush_color,width=brush_size.get())
  


def pallete():
    global brush_color
    a=colorchooser.askcolor()
    brush_color=a[-1]
    indicator.config(bg=a[-1])
 

def select_color(col):
    global brush_color
    brush_color=col
    indicator.config(bg=col)


color_frame = LabelFrame(window,text="Colors",relief=RIDGE,bg="white",font=("Harrington",15,"bold"))
color_frame.place(x=10,y=10,width=430,height=60)

tools = LabelFrame(window,text="Tool",relief=RIDGE,bg="white",font=("Harrington",15,"bold"))
tools.place(x=450,y=10,width=200,height=60)

stroke_size = LabelFrame(window,text="Size",relief=RIDGE,bg="white",font=("Harrington",15,"bold"))
stroke_size.place(x=660,y=10,width=250,height=65)

indicator=Label(window,bg='black',width=10,height=5)
indicator.place(x=1000,y=10)


        #    red       green      blue       pink    yellow    orange  sky-color brown    white    black        grey  
colors =["#ff0000","#0d4b00","#0d14dc","#ff8fdc","#f2f542","#f57e42","#42e3f5","#964B00" ,"#FFFFFF","#000000","#808080"]

i=j=0
for color in colors :
    Button(color_frame,bd=3,bg=color,cursor="circle",relief=RIDGE,width=3,command=lambda col= color:select_color(col)).grid(row=j,column=i,padx=1)
    i=i+1
    

color_pallate=Button(color_frame,image=pallete_image,bd=3,bg="purple",cursor="circle",width=30,command=pallete,relief=RIDGE)
color_pallate.grid(row=0,column=11,padx=1)

canvas_color_btn = Button(tools , text="Canvas",bd=4,bg="white",cursor="circle",command=canvas_color,relief=RIDGE)
canvas_color_btn.grid(row=0,column=0,padx=5)

save_btn = Button(tools, text="Save",bd=4,bg="white",cursor="circle",command=Save,relief=RIDGE)
save_btn.grid(row=0,column=1,padx=1)

clear_btn = Button(tools, text="Clear",bd=4,bg="white",cursor="circle",command=Clear,relief=RIDGE)
clear_btn.grid(row=0,column=2,padx=1)

erase_btn = Button(tools,  text="Erase",bd=4,bg="white",cursor="circle",command=Erase,relief=RIDGE)
erase_btn.grid(row=0,column=3,padx=1)


brush_size = Scale(stroke_size,cursor="sizing", orient=HORIZONTAL,from_=0,to=50,length=230)
brush_size.set(1)
brush_size.grid(row=0,column=0,padx=10,pady=3)
brush_size.place(y=-6)


canvas.bind("<B1-Motion>",paint)

window.mainloop()