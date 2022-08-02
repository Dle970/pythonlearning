import turtle

window = turtle.Screen()
pen = turtle.Turtle()
window.title("Input Shape")

print("Shapes: Circle, Square, Triangle")
shape = input("What shape do you want? ")

if shape.lower() == "circle":
    pen.circle(50)
elif shape.lower() == "square":
    i = 0
    while i < 4:
        pen.forward(100)
        pen.right(90)
        i = i + 1
elif shape.lower() == "triangle":
    pen.setpos(50, -10)
    pen.setpos(100, -10)
    pen.setpos(0,0)
else:
    print("You are gay!")
turtle.done()