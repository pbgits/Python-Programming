import turtle
window = turtle.Screen()
window.bgcolor("black")
window.title("Turtle")
t = turtle.Turtle()
my_pen = turtle.Pen()
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for x in range(1060):
    my_pen.pencolor(colors[x % 6])
    my_pen.width(x/100 + 1)
    my_pen.backward(x)
    my_pen.right(60)
turtle.done()
