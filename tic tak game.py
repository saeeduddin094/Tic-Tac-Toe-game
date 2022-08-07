from tkinter import *
import tkinter.messagebox as tmg
from PIL import Image,ImageTk
root=Tk()
root.geometry("400x200")
c=Canvas(root,bg="white",width="400",height="200")
c.grid()
global x
rows, cols = (3, 3)
l=[['1','2','3'],['4','5','6'],['7','8','9']]
x=0
image=Image.open("C:\\Users\\SAEED UDDIN\\Downloads\\images.jpg")
resized_image= image.resize((300,80), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(resized_image)
Label(c,image=photo).place(x=75,y=0)
def checK():
  if (x % 2 == 0):
    Label(c, text="Player saeed turn",font='bold').place(x=0, y=100)
  else:
    Label(c, text="Player zaid turn",font='bold').place(x=0, y=100)
  global flag
  flag=0
  if ((l[0][0]==l[0][1]) and l[0][1]==l[0][2]):
    flag=l[0][0]
    b = Button(c, text="", width=9,bg="red")
    b.place(x=0, y=0)
  elif ((l[1][0]==l[1][1]) and l[1][1]==l[1][2]):
    b = Button(c, text="", width=9, bg="red")
    b.place(x=0, y=25)
    flag= l[1][0]
  elif ((l[2][0]==l[2][1]) and l[2][1]==l[2][2]):
    b = Button(c, text="", width=9, bg="red")
    b.place(x=0, y=50)
    flag = l[2][0]
  elif ((l[0][0]==l[1][0]) and l[1][0]==l[2][0]):
    b = Button(c, text="",width=2, height=4, bg="red")
    b.place(x=0, y=0)
    flag = l[0][0]
  elif ((l[0][1]==l[1][1]) and l[1][1]==l[2][1]):
    b = Button(c, text="", width=2, height=4, bg="red")
    b.place(x=25, y=0)
    flag = l[0][1]
  elif ((l[0][2]==l[1][2]) and l[1][2]==l[2][2]):
    b = Button(c, text="", width=2, height=4, bg="red")
    b.place(x=50, y=0)
    flag = l[0][2]
  elif ((l[0][0]==l[1][1]) and l[1][1]==l[2][2]):
    print("saeed")
    b = Button(c, text="",width=2 , bg="red")
    b.place(x=0, y=0)
    b = Button(c, text="",width=2 , bg="red")
    b.place(x=25, y=25)
    b = Button(c, text="",width=2  ,bg="red")
    b.place(x=50, y=50)
    flag = l[0][0]
  elif ((l[0][2]==l[1][1]) and l[1][1]==l[2][0]):
    print("saeed")
    b = Button(c, text="", width=2, bg="red")
    b.place(x=50, y=0)
    b = Button(c, text="", width=2, bg="red")
    b.place(x=25, y=25)
    b = Button(c, text="", width=2, bg="red")
    b.place(x=0, y=50)
    flag = l[0][2]
  if flag=='X':
    tmg.showinfo(title="message",message="player saeed won")
    Label(c, text="GAME FINISHED", font="bold").place(x=0, y=100)
  elif flag=='0' :
    tmg.showinfo(title="message", message="player zaid won")
    Label(c, text="GAME FINISHED", font="bold").place(x=0, y=100)
  elif(x==9)   :
    tmg.showinfo(title="message", message="match draw")
    Label(c,text="GAME FINISHED",font="bold").place(x=0,y=100)
def c9(event):
  global x
  if x%2==0:
    x=x+1
    b= Button(c, text="X", width=2)
    b.place(x=50, y=50)
    l[2][2]='X'
    checK()
  else:
    x=x+1
    b = Button(c, text="0", width=2)
    b.place(x=50, y=50)
    l[2][2]='0'
    checK()
def c8(event):
  global x
  if x % 2 == 0:
    x = x + 1
    b = Button(c, text="X", width=2)
    b.place(x=25, y=50)
    l[2][1] = 'X'
    checK()
  else:
    x = x + 1
    b = Button(c, text="0", width=2)
    b.place(x=25, y=50)
    l[2][1] = '0'
    checK()
def c7(event):
  global x
  if x % 2 == 0:
    x = x + 1
    b = Button(c, text="X", width=2)
    b.place(x=0, y=50)
    l[2][0] = 'X'
    checK()
  else:
    x = x + 1
    b = Button(c, text="0", width=2)
    b.place(x=0, y=50)
    l[2][0] = '0'
    checK()
def c6(event):
  global x
  if x % 2 == 0:
    x = x + 1
    b = Button(c, text="X", width=2)
    b.place(x=50, y=25)
    l[1][2] = 'X'
    checK()
  else:
    x = x + 1
    b = Button(c, text="0", width=2)
    b.place(x=50, y=25)
    l[1][2] = '0'
    checK()
def c5(event):
  global x
  if x % 2 == 0:
    x = x + 1
    b = Button(c, text="X", width=2)
    b.place(x=25, y=25)
    l[1][1] = 'X'
    checK()
  else:
    x = x + 1
    b = Button(c, text="0", width=2)
    b.place(x=25, y=25)
    l[1][1] = '0'
    checK()
def c4(event):
  global x
  if x % 2 == 0:
    x = x + 1
    b = Button(c, text="X", width=2)
    b.place(x=0, y=25)
    l[1][0] = 'X'
    checK()
  else:
    x = x + 1
    b = Button(c, text="0", width=2)
    b.place(x=0, y=25)
    l[1][0] = '0'
    checK()
def c3(event):
  global x
  if x % 2 == 0:
    x = x + 1
    b = Button(c, text="X", width=2)
    b.place(x=50, y=0)
    l[0][2] = 'X'
    checK()
  else:
    x = x + 1
    b = Button(c, text="0", width=2)
    b.place(x=50, y=0)
    l[0][2] = '0'
    checK()
def c2(event):
  global x
  if x % 2 == 0:
    x = x + 1
    b = Button(c, text="X", width=2)
    b.place(x=25, y=0)
    l[0][1] = 'X'
    checK()
  else:
    x = x + 1
    b = Button(c, text="0", width=2)
    b.place(x=25, y=0)
    l[0][1] ='0'
    checK()
def c1(event):
  global x
  if x % 2 == 0:
    x = x + 1
    b = Button(c, text="X", width=2)
    b.place(x=0, y=0)
    l[0][0] = 'X'
    checK()
  else:
    x = x + 1
    b = Button(c, text="0", width=2)
    b.place(x=0, y=0)
    l[0][0] = '0'
    checK()
b1=Button(c,text="",width=2)
b1.place(x=0,y=0)
b1.bind('<Button-1>',c1)
b2=Button(c,text="",width=2)
b2.place(x=25,y=0)
b2.bind('<Button-1>',c2)
b3=Button(c,text="",width=2)
b3.place(x=50,y=0)
b3.bind('<Button-1>',c3)
b4=Button(c,text="",width=2)
b4.place(x=0,y=25)
b4.bind('<Button-1>',c4)
b5=Button(c,text="",width=2)
b5.place(x=25,y=25)
b5.bind('<Button-1>',c5)
b6=Button(c,text="",width=2)
b6.place(x=50,y=25)
b6.bind('<Button-1>',c6)
b7=Button(c,text=" ",width=2)
b7.place(x=0,y=50)
b7.bind('<Button-1>',c7)
b8=Button(c,text="",width=2)
b8.place(x=25,y=50)
b8.bind('<Button-1>',c8)
b9=Button(c,text="",width=2)
b9.place(x=50,y=50)
b9.bind('<Button-1>',c9)
if(x%2==0):
  Label(c,text="Player saeed turn",font='bold').place(x=0,y=100)
else:
  Label(c,text="Player zaid turn",font='bold').place(x=0,y=100)
mainloop()