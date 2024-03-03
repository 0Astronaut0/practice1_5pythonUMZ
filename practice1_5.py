#amirhossein askari
#40213160281828
def show(t,l,color):
    t.color(color)
    for i in range(4):
        t.forward(l)
        t.left(90)

        
import turtle
color = input("color: ")
l = int(input("rectangle: "))
t = turtle.Turtle()  #turtle object
t.pensize(2)
wn = turtle.Screen()  #window object
wn.bgcolor("black")
wn.title("turtle practice")
show(t,l,color)
ex = input("type q to exit: ")
if(ex != 'q'):
    wn.mainloop()