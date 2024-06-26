import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

# getting user input for # of Recers
def get_number_of_recers():
    racers = 0
    while True:
        racers = input('Enter the nuber of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else: 
            print('Input is not numeric...Try Again!')
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print('Number not in range (2 - 10)... Try Again!')

# racing our turtle
def race(colors):
    turtles = create_turtles(colors)  

    while True:
        for racer in  turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


# creating turtles and their properties
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)                      # now its face towars north after turning left 90 degree
        racer.penup()
        # turtle starting position
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles

# setting up tutle and the turle screen
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')

racers = get_number_of_recers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers] 

winner = race(colors)
print("The winner is the turtle with color: ", winner)
time.sleep(5)
