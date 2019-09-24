from graph import *
from tkinter import*
brushColor(220,220,220)
penColor("white")
rectangle(0,0,9999,250)
c=canvas()
c.pack
brushColor("grey")
c.create_oval(50,200,300,350,fill="grey")
brushColor("white")
penColor("white")
rectangle(50,275,300,400)
penColor("black")
line (50,275,300,275)
line (57,250,296,250)
line (80,225,270,225)
line (120,210,240,210)
for i in range (-1,11):
	line (80+i*20,275,80+i*20,250)
for i in range (1,11):
	line (70+i*20,225,70+i*20,250)
for i in range (2,9):
	line (80+i*20,210,80+i*20,225)
line (195,200,195,210)
line (175,200,175,210)
line (155,200,155,210)


c.create_oval(400,300,500,700,fill='brown')
brushColor("white")
penColor("white")
rectangle(400,400,500,700)



c.create_oval(425,270,475,310,fill='brown',outline='brown')
c.create_oval(430,280,470,305,fill='grey')
c.create_oval(415,380,435,430,fill='brown',outline='brown')
c.create_oval(465,380,485,430,fill='brown',outline='brown')
c.create_oval(400,420,435,430,fill='brown',outline='brown')
c.create_oval(465,420,500,430,fill='brown',outline='brown')
brushColor(150,90,50)
penColor(150,90,50)
rectangle(400,400,500,390)
rectangle(440,390,460,310)
c.create_oval(430,330,360,340,fill='brown',outline='brown')
c.create_oval(470,330,540,340,fill='brown',outline='brown')
c.create_oval(436,286,446,293,fill='white')
c.create_oval(455,286,465,293,fill='white')
penSize(3)
penColor("black")
line(370,300,370,400)
penSize(1)


c.create_oval(100,400,300,450,fill='brown',outline='brown')
c.create_oval(80,360,140,420,fill='brown',outline='brown')
c.create_oval(100,400,300,450,fill='brown',outline='brown')
d=c.create_oval(110,430,130,500,fill='brown',outline='brown')
f=c.create_oval(130,430,150,500,fill='brown',outline='brown')
b=c.create_oval(240,430,260,500,fill='brown',outline='brown')
a=c.create_oval(260,430,280,500,fill='brown',outline='brown')
c.create_oval(90,380,100,390,fill='white')
c.create_oval(120,380,130,390,fill='white')
polygon([(260,410),(275,390),(300,370),(340,350),(346,354),(347,360),(320,390),(285,410),(265,415)])
polygon([(95,340),(90,365),(105,360)])
polygon([(120,340),(115,360),(130,365)])

m = circle (400, 100, 50)
mb1 = circle (400 + 20, 100 + 10, 20)
mb2 = circle (400 - 20, 100 - 20, 20)
mr = c.create_arc(400 - 40, 100 - 40, 400 + 40, 100 + 40, start = 180, exten = 90, style = ARC, outline = 'black', width = 2)
r1 = 40
dr = 1.015
r = 50
z = 20

data = list()
brushColor('white')
for i in range (1, 15):
    g = circle (50+i*20, 50, 20)
    data.append(g)
    h = circle (78+i*20, 78, 20)
    data.append(h)

def update():
    global dr
    global r
    global m
    global mb1
    global mb2
    global mr
    global r1
    global z
    
    if ((xCoord(a)<270)and(yCoord(a)<437)):
    	moveObjectBy(a,1,0)
    elif (yCoord(a)<437):
    	moveObjectBy(a,0,1)
    elif (xCoord(a)>260):
    	moveObjectBy(a, -1, 0)
    elif (yCoord(a)>430):
    	moveObjectBy(a,0,-1)
    	
    	
    if ((xCoord(b)<251)and(yCoord(b)<437)):
    	moveObjectBy(b,1,0)
    elif (yCoord(b)<437):
    	moveObjectBy(b,0,1)
    elif (xCoord(b)>240):
    	moveObjectBy(b, -1, 0)
    elif (yCoord(b)>430):
    	moveObjectBy(b,0,-1)
    	
    if ((xCoord(d)<120)and(yCoord(d)<437)):
    	moveObjectBy(d,1,0)
    elif (yCoord(d)<437):
    	moveObjectBy(d,0,1)
    elif (xCoord(d)>110):
    	moveObjectBy(d, -1, 0)
    elif (yCoord(d)>430):
    	moveObjectBy(d,0,-1)
    	
    if ((xCoord(f)<141)and(yCoord(f)<437)):
    	moveObjectBy(f,1,0)
    elif (yCoord(f)<437):
    	moveObjectBy(f,0,1)
    elif (xCoord(f)>130):
    	moveObjectBy(f, -1, 0)
    elif (yCoord(f)>430):
    	moveObjectBy(f,0,-1)
    r = r*dr
    z = z*dr
    r1 = r1*dr  	
    deleteObject(m)
    deleteObject(mb1)
    deleteObject(mb2)
    deleteObject(mr)
    m = circle (400, 100, r)
    mb1 = circle (400 + z, 100 + z, z)
    mb2 = circle (400 - z, 100 - z, z)
    mr = c.create_arc(400 - r1*dr, 100 - r1*dr, 400 + r1*dr, 100 + r1*dr, start = 180, exten = 90, style = ARC, outline = 'black', width = 2)
    if r > 90:
    	dr = 2 - dr
    if r < 40:
    	dr = 2 - dr
    
    global data
    for i in range (1, 29):
    	moveObjectBy (data[i-1], -5, 0)
    	if xCoord(data[i-1]) < -40:
    		deleteObject(data[i-1])
    		if (i - 1)%2 == 0:
    			data [i-1] = circle (550, 50, 20)
    		else:
    				data[i-1] = circle (550, 78, 20)
    				
			
onTimer(update,50)

run()
