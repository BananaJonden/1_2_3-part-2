#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
key_top_row = ["q","w","e","r","t","y","u","i","o""p"]
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
apple = trtl.Turtle()
apple.speed(1)
apple.right(90)
#-----functions-----
def apple_drop():
  apple.penup()
  apple.goto(0, -200)
def draw_letter_A():
  apple.penup()
  apple.goto(0,200)
  apple.color("black")
  apple.write("A", font=("Times New Roman", 50, "bold")) 
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
draw_letter_A()
apple.goto(0,0)
#step 14 correlate
'''
def change_position():
  newxpos = rand.randint(-150,150)
  newypos = rand.randint(-150,150)
  apple.goto(newxpos,newypos)
change_position()
'''

#-----function calls-----
wn.bgpic("background.gif")
wn.listen()
wn.onkeypress(apple_drop, "a")
apple.clear()
wn.mainloop()
