#datos de entrada 14
"""5 6 2 8 4 9 1 7 3
5 1 4 9 7 2 8 3 6
5 6 9 8 1 4 3 7 2
6 1 8 3 5 2 9 4 7
1 9 4 2 7 8 5 6 3
3 4 1 5 7 2 9 8 6
4 5 7 3 8 9 1 6 2
5 9 7 4 3 6 8 1 2
3 7 1 2 5 4 8 9 6
2 3 9 8 1 5 6 7 4
2 7 6 9 5 1 4 3 8
3 8 4 9 5 7 1 2 6
3 6 4 8 2 5 1 9 7
5 4 1 7 9 6 3 2 8"""

from turtle import *

setup(600, 600, 400,20)
title("TIC TAC TOE")
hideturtle()
#lines tictact
pensize(5)
penup()
goto(100, 230)
pendown()
goto(100, -230)

penup()
goto(-100, 230)
pendown()
goto(-100, -230)

#lines horiz
penup()
goto(-230, -70)
pendown()
goto(230, -70)

penup()
goto(-230, 70)
pendown()
goto(230,70)

#textos cuadrantes
penup()
m=-150
y=100
#active
es1=0
es2=0
es3=0
es4=0
es5=0
es6=0
es7=0
es8=0
es9=0
posx1=''
posx2=''
posx3=''
posx4=''
posx5=''
posx6=''
posx7=''
posx8=''
posx9=''
poso1=''
poso2=''
poso3=''
poso4=''
poso5=''
poso6=''
poso7=''
poso8=''
poso9=''
for i in range(1,10):
	goto(m, y)
	write(i, False,"right", ("arial", 20, "bold italic"))
	m+=150
	if(i%3==0):
		y-=120
		m=-150
#comandos

penup()
goto(120, -270)
pencolor("brown")
write("Abre la consola de comandos,y digita la posición:[1...9] ", False,"right", ("arial", 12, "bold italic"))
for j in range(1,10):
	#Tic Para X
	if(j%2!=0):

		print("TURNO: ",j)
		pos=int(input("Posición [1...9] 'X': "))
		if(pos==1 and es1==0):
			penup()
			goto(-120, 50)
			pencolor("brown")
			write("X", False,"right", ("arial", 80, "bold italic"))
			es1=1
			posx1='x'

		if(pos==2 and es2==0):
			penup()
			goto(30, 50 )
			pencolor("brown")
			write("X", False,"right", ("arial", 80, "bold italic"))
			es2=1
			posx2='x'

		if(pos==3 and es3==0):
			penup()
			goto(180, 50)
			pencolor("brown")
			write("X", False,"right", ("arial", 80, "bold italic"))
			es3=1
			posx3='x'

		if(pos==4 and es4==0):
			penup()
			goto(-120, -70)
			pencolor("brown")
			write("X", False,"right", ("arial", 80, "bold italic"))
			es4=1
			posx4='x'

		if(pos==5 and es5==0):
			penup()
			goto(30, -70)
			pencolor("brown")
			write("X", False,"right", ("arial", 80, "bold italic"))
			es5=1
			posx5='x'

		if(pos==6 and es6==0):
			penup()
			goto(180, -70)
			pencolor("brown")
			write("X", False,"right", ("arial", 80, "bold italic"))
			es6=1
			posx6='x'

		if(pos==7 and es7==0):
			penup()
			goto(-120, -190)
			pencolor("brown")
			write("X", False,"right", ("arial", 80, "bold italic"))
			es7=1
			posx7='x'

		if(pos==8 and es8==0):
			penup()
			goto(30, -190)
			pencolor("brown")
			write("X", False,"right", ("arial", 80, "bold italic"))
			es8=1
			posx8='x'

		if(pos==9 and es9==0):
			penup()
			goto(180, -190)
			pencolor("brown")
			write("X", False,"right", ("arial", 80, "bold italic"))
			es9=1
			posx9='x'
	if(posx3=='x' and posx5=='x' and posx7=='x'):
		goto(-10,-50)
		pencolor("green")
		write("GANA X!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	if(posx9=='x' and posx8=='x' and posx7=='x'):
		goto(-10,-50)
		pencolor("green")
		write("GANA X!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	if(posx4=='x' and posx5=='x' and posx6=='x'):
		goto(-10,-50)
		pencolor("green")
		write("GANA X!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	if(posx1=='x' and posx2=='x' and posx3=='x'):
		goto(-10,-50)
		pencolor("green")
		write("GANA X!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	if(posx1=='x' and posx4=='x' and posx7=='x'):
		goto(-10,-50)
		pencolor("green")
		write("GANA X!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	if(posx2=='x' and posx5=='x' and posx8=='x'):
		goto(-10,-50)
		pencolor("green")
		write("GANA X!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	if(posx3=='x' and posx6=='x' and posx9=='x'):
		goto(-10,-50)
		pencolor("green")
		write("GANA X!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()

	if(posx1=='x' and posx5=='x' and posx9=='x'):
		goto(-10,-50)
		pencolor("green")
		write("GANA X!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	#tac para O

	if(j%2==0):
		print("TURNO: ",j)
		pos=int(input("Posición [1...9] 'O': "))
		if(pos==1 and es1==0):
			penup()
			goto(-120, 50)
			pencolor("blue")
			write("O", False,"right", ("arial", 80, "bold italic"))
			es1=1
			poso1='o'

		if(pos==2 and es2==0):
			penup()
			goto(30, 50)
			pencolor("blue")
			write("O", False,"right", ("arial", 80, "bold italic"))
			es2=1
			poso2='o'

		if(pos==3 and es3==0):
			penup()
			goto(180, 50)
			pencolor("blue")
			write("O", False,"right", ("arial", 80, "bold italic"))
			es3=1
			poso3='o'

		if(pos==4 and es4==0):
			penup()
			goto(-120, -70)
			pencolor("blue")
			write("O", False,"right", ("arial", 80, "bold italic"))
			es4=1
			poso4='o'

		if(pos==5 and es5==0):
			penup()
			goto(30, -70)
			pencolor("blue")
			write("O", False,"right", ("arial", 80, "bold italic"))
			es5=1
			poso5='o'

		if(pos==6 and es6==0):
			penup()
			goto(180, -70)
			pencolor("blue")
			write("O", False,"right", ("arial", 80, "bold italic"))
			es6=1
			poso6='o'

		if(pos==7 and es7==0):
			penup()
			goto(-120, -190)
			pencolor("blue")
			write("O", False,"right", ("arial", 80, "bold italic"))
			es7=1
			poso7='o'

		if(pos==8 and es8==0):
			penup()
			goto(30, -190)
			pencolor("blue")
			write("O", False,"right", ("arial", 80, "bold italic"))
			es8=1
			poso8='o'

		if(pos==9 and es9==0):
			penup()
			goto(180, -190)
			pencolor("blue")
			write("O", False,"right", ("arial", 80, "bold italic"))
			es9=1
			poso9='o'
	if(poso9=='o' and poso8=='o' and poso7=='o'):
		goto(-10,-50)
		pencolor("red")
		write("GANA O!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	if(poso4=='o' and poso5=='o' and poso6=='o'):
		goto(-10,-50)
		pencolor("red")
		write("GANA O!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	if(poso1=='o' and poso2=='o' and poso3=='o'):
		goto(-10,-50)
		pencolor("red")
		write("GANA O!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	if(poso1=='o' and poso4=='o' and poso7=='o'):
		goto(-10,-50)
		pencolor("red")
		write("GANA O!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	if(poso2=='o' and poso5=='o' and poso8=='o'):
		goto(-10,-50)
		pencolor("red")
		write("GANA O!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	if(poso3=='o' and poso6=='o' and poso9=='o'):
		goto(-10,-50)
		pencolor("red")
		write("GANA O!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	if(poso1=='o' and poso5=='o' and poso9=='o'):
		goto(-10,-50)
		pencolor("red")
		write("GANA O!", False,"center", ("arial", 100, "bold italic"))

		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
	
	if(poso3=='o' and poso5=='o' and poso7=='o'):
		goto(-10,-50)
		pencolor("red")
		write("GANA O!", False,"center", ("arial", 100, "bold italic"))
		goto(0, -285)
		write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))
		exitonclick()
    

#cerrar programa
penup()
goto(0, -285)
write("Click derecho para cerrar", False,"right", ("arial", 6, "bold italic"))

exitonclick()

#solución 8 8 5 6 5 8 7 5 0 8 7 6 7 5