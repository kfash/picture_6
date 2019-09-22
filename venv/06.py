from graph import *
brushColor(220,220,220)
penColor("white")
rectangle(0,0,9999,250)
c=canvas()
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




c.create_oval(400,300,500,700)
brushColor("white")
penColor("white")
rectangle(400,400,500,700)
brushColor(150,90,50)
rectangle(400,400,500,390)
rectangle(440,390,460,310)


c.create_oval(425,270,475,310)
c.create_oval(430,280,470,305)
c.create_oval(415,380,435,430)
c.create_oval(465,380,485,430)
c.create_oval(400,420,435,430)
c.create_oval(465,420,500,430)
c.create_oval(430,330,360,340)
c.create_oval(470,330,540,340)
penSize(3)
penColor("black")
line(370,300,370,400)
penSize(1)


c.create_oval(100,400,300,450)
c.create_oval(80,360,140,420)
c.create_oval(100,400,300,450)
c.create_oval(110,430,130,500)
c.create_oval(130,430,150,500)
c.create_oval(240,430,260,500)
c.create_oval(260,430,280,500)
polygon([(260,410),(275,390),(300,370),(340,350),(346,354),(347,360),(320,390),(285,410),(265,415)])
polygon([(95,340),(90,365),(105,360)])
polygon([(120,340),(115,360),(130,365)])
run()