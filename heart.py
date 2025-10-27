import turtle
import math

kat = turtle.Turtle()
wn = turtle.Screen()
kat.pensize(2)
kat.color("pink")
kat.speed(2)

kat_length = 145
kat_height = 100

kat.up()
kat.setheading(180 + math.degrees(math.atan(50/72.5)))
kat.forward(math.sqrt(50**2 + 72.5**2))
kat.setheading(0)
kat.down()

#Draw K
kat.left(90)
kat.forward(100)
kat.right(90)
kat.up()
kat.forward(30)
kat.setheading(math.degrees(math.atan(50/30)) + 180)
kat.down()
kat.forward(math.sqrt(30**2 + 50**2))
kat.setheading(-math.degrees(math.atan(50/30)))
kat.forward(math.sqrt(30**2 + 50**2))
kat.up()

#draw A
kat.setheading(0)
kat.forward(15)
kat.down()
kat.setheading(math.degrees(math.atan(100/20)))
kat.forward(math.sqrt(100**2 + 20**2))
kat.setheading(math.degrees(math.atan(-100/20)))
kat.forward(math.sqrt(100**2 + 20**2))
kat.right(180)
kat.forward(0.5 * math.sqrt(100**2 + 20**2))
kat.setheading(180)
kat.forward(20)
kat.up()
kat.setheading(math.degrees(math.atan(-50/30)))
kat.forward(math.sqrt(50**2+30**2))

# draw T
kat.setheading(0)
kat.forward(35)
kat.down()
kat.left(90)
kat.forward(100)
kat.right(90)
kat.forward(25)
kat.right(180)
kat.forward(50)
#end pos = (22, 50)

#start position of heart
kat.color("red")
kat.up()
kat.setheading(180 + math.degrees(math.atan(250/32)))
kat.forward(math.sqrt(250**2 + 32**2))
kat.down()

#right half
kat.setheading(math.degrees(math.atan(250/125)))
kat.forward(math.sqrt(250**2 + 125**2))

kat.setheading(180 + math.degrees(math.atan(-75/47.875)))
kat.forward(math.sqrt(75**2 + 47.875**2))

kat.setheading(180 + math.degrees(math.atan(50/77.125)))
kat.forward(math.sqrt(50**2 + 77.125**2))

#left half
kat.setheading(-180 - math.degrees(math.atan(50/77.125)))
kat.forward(math.sqrt(50**2 + 77.125**2))

kat.setheading(-180 - math.degrees(math.atan(-75/47.875)))
kat.forward(math.sqrt(75**2 + 47.875**2))

kat.setheading(-math.degrees(math.atan(250/125)))
kat.forward(math.sqrt(250**2 + 125**2))

kat.hideturtle()

wn.exitonclick()