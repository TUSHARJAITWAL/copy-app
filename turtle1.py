# import turtle library
import turtle             
my_wn = turtle.Screen()
turtle.speed(11)
for i in range(30):
   turtle.circle(5*i)
   turtle.circle(-5*i)
   turtle.left(i)
   turtle.bgcolor("black")
   turtle.pencolor("white")
   turtle.pensize(1)
turtle.exitonclick()