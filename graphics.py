import turtle



turtle.bgcolor('black')

turtle.speed(0)
turtle.pensize(2)
turtle.pencolor('red')
 

def circle(r):
      for i in range(10):
        turtle.circle(r)
        r=r-4
 
def design():
      for i in range(10):
        circle(150)
        turtle.right(36)

design()
turtle.done()


