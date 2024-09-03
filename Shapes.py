import pgzrun 
from random import randint

TITLE = "Draw"
HEIGHT = 500
WIDTH = 500 

r = randint(0,255)
g = randint(0,255)
b = randint(0,255)


def draw():
    screen.fill("Blue")
    screen.draw.circle((300,300), 50, (r,g,b))
    box = Rect((200,200), (100,100))
    screen.draw.rect((box),(r,g,b))





pgzrun.go()