# Libraries from which we would be writing our code are tkinter and time
#tkinker is used for applications
from tkinter import Label, Tk, Grid
import time

# we'll now define our application size an title, geometry and since we want the app to be resizeable we wouuld set True(1,1)
clock_window = Tk()
clock_window.title('My Digital Clock')
# Specifying the widget of the app
clock_window.geometry("500x250")
clock_window.resizable(1,1)
#Defining the font, color of the time, it's width and background colour of our clock
text_font = ('Arial',68, 'bold')
foreground = '#00FF00'
background ="#FFFFFF"
border_width = 20

label= Label(clock_window, font=text_font, bg=background, fg = foreground, bd=border_width, width=10, height=2)
grid =Grid()
label.grid(row=0, column=1)
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
   
label.after(200,digital_clock)
clock_window.mainloop()