import turtle
import time
import random as rand
WIDTH,HEIGHT=500,500
COLORS=['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']
def get_no_of_turtles():
    racers=0
    while(True):
        racers=input("Enter number of Racers btn (2 - 10): ")
        if racers.isdigit():
            racers=int(racers)
        else:
            print("Try Again!!! Enter a Digit this time")
            continue
        if 2<=racers<=10:
            return racers
        else:
            print("Try Again!!! Enter no of Racers between (2 -10)")
def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing Game')
    screen._root.attributes('-topmost', 1)
    screen._root.update()
    screen._root.attributes('-topmost', 0)
    return screen
def create_turtles(colors):
    Turtles=[None]*len(colors)
    spacingx=WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        Turtles[i]=turtle.Turtle()
        Turtles[i].color(color)
        Turtles[i].shape('turtle')
        Turtles[i].left(90)
        Turtles[i].penup()
        Turtles[i].setpos(-WIDTH//2+((i+1)*spacingx),-HEIGHT//2+20)
        Turtles[i].pendown()
    return Turtles
def race(colors):
    Turtles=create_turtles(colors)
    while(True):
        for turtle in Turtles:
            distance=rand.randrange(1,20)
            turtle.forward(distance)
            x,y=turtle.pos()
            if y>=HEIGHT//2-10:
                time.sleep(3)
                return turtle.color()[0]

racers=get_no_of_turtles()
screen=init_turtle()
rand.shuffle(COLORS)
colors=COLORS[:racers]
winner=race(colors)
print(f"The Winner is the turtle with the color {winner}")