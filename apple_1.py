#   a123_apple_1.py
import turtle as trtl
import random as rand
#-----setup-----
pear_image = "pear.gif" # Store the file name of your shape
apple_image = "apple.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(pear_image) # Make the screen aware of the new file
wn.addshape(apple_image)

apple = trtl.Turtle()
apple1 = trtl.Turtle()
apple2 = trtl.Turtle()
apple3 = trtl.Turtle()
apple4 = trtl.Turtle()

apple2.hideturtle()
apple2.penup()
apple2.shape(apple_image)
apple2.goto(-90,120)
apple2.showturtle()
apple2.speed(1)

apple3.hideturtle()
apple3.penup()
apple3.shape(apple_image)
apple3.goto(40,100)
apple3.showturtle()
apple3.speed(1)

apple4.hideturtle()
apple4.penup()
apple4.shape(apple_image)
apple4.goto(100,60)
apple4.showturtle()
apple4.speed(1)

apple.hideturtle()
apple.penup()
apple.shape(apple_image)
apple.goto(-100,60)
apple.showturtle()

# Apple speed

apple.speed(0)
apple1.speed(0)
apple2.speed(0)
apple3.speed(0)
apple4.speed(0)
apple1.right(90)
#-----functions-----
# Making the apple fall.
def apple_fall():
  apple1.penup()
  apple1.clear()
  apple1.goto(0, -150)
  apple1.hideturtle()

def apple1_fall():
  apple.penup()
  apple.clear()
  apple.goto(-90,-150)
  apple.hideturtle()

def apple2_fall():
  apple2.penup()
  apple2.clear()
  apple2.goto(-90,-150)
  apple2.hideturtle()

def apple3_fall():
  apple3.penup()
  apple3.clear()
  apple3.goto(40,-150)
  apple3.hideturtle()

def apple4_fall():
  apple4.penup()
  apple4.clear()
  apple4.goto(100,-150)
  apple4.hideturtle()

# Drawing the letters

def draw_a_L():
  apple.penup()
  apple.goto(-300,150)
  apple.color("black")
  apple.write("L", font=("Arial", 50))
  apple.goto(-90,60)

def draw_an_I():
  apple1.penup()
  apple1.goto(-200,150)
  apple1.color("black")
  apple1.write("I", font=("Arial", 50)) 
  apple1.goto(0,0)

def draw_a_S():
  apple2.penup()
  apple2.goto(0,150)
  apple2.color("black")
  apple2.write("S", font=("Arial", 50))
  apple2.goto(-80,125)

def draw_a_A():
  apple3.penup()
  apple3.goto(200,150)
  apple3.color("black")
  apple3.write("A", font=("Arial", 50))
  apple3.goto(45,120)


def draw_an_K():
  apple4.penup()
  apple4.goto(300,150)
  apple4.color("black")
  apple4.write("K", font=("Arial", 50))
  apple4.goto(100,70)



# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

draw_apple(apple1)
draw_a_L()
draw_an_I()
draw_a_S()
draw_a_A()
draw_an_K()

# Apple speed

apple.speed(1)
apple1.speed(1)
apple2.speed(1)
apple3.speed(1)
apple4.speed(1)
#-----function calls-----

wn.bgpic("background.gif")
wn.listen()
wn.onkeypress(apple1_fall, "l")
wn.onkeypress(apple_fall, "i")
wn.onkeypress(apple2_fall, "s")
wn.onkeypress(apple3_fall, "a")
wn.onkeypress(apple4_fall, "k")
wn.mainloop()
