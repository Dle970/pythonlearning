import turtle

window = turtle.Screen()
pen = turtle.Turtle()
window.title("Drawing Graphics with Turtle")



def poweritself(operand):
    operand **= operand
    return operand


print(poweritself(10))


user_input = input("What color do you want the line to be? ")
pen.color(user_input)
far = int(input("How far do you want it to be? "))
pen.forward(far)
pen.pensize(20)
pen.color("cyan")
i = 0
while i < 4:
    pen.forward(100)
    pen.right(90)
    i = i + 1
pen.up()
pen.forward(50)
pen.down()
pen.right(180)
pen.fillcolor("yellow")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

## circle
pen.color("brown")
pen.fillcolor("brown")
pen.begin_fill()
pen.right(90)
pen.forward(100)
pen.left(90)
pen.forward(30)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(30)
pen.end_fill()
pen.backward(15)
pen.right(180)
pen.color("green")
pen.fillcolor("green")
pen.begin_fill()
pen.circle(150)
pen.end_fill()
pen.up()
pen.forward(150)
pen.down()
pen.fillcolor("green")
pen.begin_fill()
pen.circle(75)
pen.end_fill()
pen.right(180)
pen.up()
pen.forward(300)
pen.down()
pen.right(180)
pen.fillcolor("green")
pen.begin_fill()
pen.circle(75)
pen.end_fill()


#set position

pen.setpos(0,100)
pen.setpos(50,200)
pen.setpos(0,0)


pen.forward(300)
pen.right(90)
pen.forward(200)

pen.circle(50)

pen.up()
pen.right(90)
pen.forward(100)
pen.down()
pen.circle(50)
turtle.done()