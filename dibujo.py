import turtle
import colorsys

def dibujoEstrella():
      
 estrella=turtle.Turtle()
 turtle.Screen().bgcolor("white")
 estrella.color("blue")
 for i in range(10):
     for i in range(2):
       estrella.forward(100)
       estrella.right(60)
       estrella.forward(100)
       estrella.right(120)
     estrella.right(36)

def dibujoCirculo():
      
 t=turtle.Turtle()
 s=turtle.Screen()
 s.bgcolor("white")
 t.speed(0)
 t.pensize(2)
 n=36
 h=0
 for i in range(360):
     c=colorsys.hsv_to_rgb(h, 1, 0.8)
     h+=1/n
     t.color(c)
     t.left(10)
     for j in range(5):
         t.forward(200)
         t.left(144)

def dibujoSol():
      
 sol = turtle.Turtle()
 sol.speed(20)
 sol.color("black", "orange")
 sol.begin_fill()
 for i in range(50):
     sol.forward(300)
     sol.left(170) 
 sol.end_fill()
 turtle.done()

def dibujoRosa():
 turtle.penup()
 turtle.left(90)
 turtle.fd(200)
 turtle.pendown()
 turtle.right(90)
 turtle.fillcolor("red")
 turtle.begin_fill()
 turtle.circle(10,180)
 turtle.circle(25,110)
 turtle.left(50)
 turtle.circle(60,45)
 turtle.circle(20,170)
 turtle.right(24)
 turtle.fd(30)
 turtle.left(10)
 turtle.circle(30,110)
 turtle.fd(20)
 turtle.left(40)
 turtle.circle(90,70)
 turtle.circle(30,150)
 turtle.right(30)
 turtle.fd(15)
 turtle.circle(80,90)
 turtle.left(15)
 turtle.fd(45)
 turtle.right(165)
 turtle.fd(20)
 turtle.left(155)
 turtle.circle(150,80)
 turtle.left(50)
 turtle.circle(150,90)
 turtle.end_fill()
 turtle.left(150)
 turtle.circle(-90,70)
 turtle.left(20)
 turtle.circle(75,105)
 turtle.setheading(60)
 turtle.circle(80,98)
 turtle.circle(-90,40)
 turtle.left(180)
 turtle.circle(90,40)
 turtle.circle(-80,98)
 turtle.setheading(-83)
 turtle.fd(30)
 turtle.left(90)
 turtle.fd(25)
 turtle.left(45)
 turtle.fillcolor("green")
 turtle.begin_fill()
 turtle.circle(-80,90)
 turtle.right(90)
 turtle.circle(-80,90)
 turtle.end_fill()
 turtle.right(135)
 turtle.fd(60)
 turtle.left(180)
 turtle.fd(85)
 turtle.left(90)
 turtle.fd(80)
 turtle.right(90)
 turtle.right(45)
 turtle.fillcolor("green")
 turtle.begin_fill()
 turtle.circle(80,90)
 turtle.left(90)
 turtle.circle(80,90)
 turtle.end_fill()
 turtle.left(135)
 turtle.fd(60)
 turtle.left(180)
 turtle.fd(60)
 turtle.right(90)
 turtle.circle(200,60)
 turtle.done()
  
print("1) Dibujar una estrella")
print("2) Dibujar un circulo con estrellas")
print("3) Dibujar el sol")
print("4) Dibujar una rosa")
opcion=int(input("Ingresa la opcion deseada: "))
if opcion==1:
      dibujoEstrella()
if opcion==2:
      dibujoCirculo()
if opcion==3:
      dibujoSol()
if opcion==4:
      dibujoRosa()
if opcion >4:
  print("Ingresa una opcion valida")










    
