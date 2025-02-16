import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

WHITE = (255,255,255)
GREEN = (0,255,0)

score = 0
lives = 3

racquet = Actor("tennis raqcuet")
racquet.pos = (WIDTH //2,HEIGHT-60)

balls = []
enemies = []

for i in range(8):
    enemy=Actor("fire")
    enemy.x = random.randint(0, WIDTH -100)
    enemy.y = random.randint(-100,0)
    enemies.append(enemy)

direction = 1

speed = 5

def display_score():
    global score, lives
    screen.draw.text(f"Score: {score}",(50,30))
    screen.draw.text(f"Lives: {lives}",(50,60))


def on_key_down(key):
    if key == keys.SPACE:
        #create a new ball
        ball=Actor("tennis ball")
        ball.x = racquet.x
        ball.y = racquet.y - 50
        balls.append(ball)


def update():
    global lives
    global score
    global direction

    if keyboard.right:
        racquet.x += speed
        if racquet.x >= WIDTH:
            racquet.x = WIDTH
    elif keyboard.left:
        racquet.x -= speed
        if racquet.x <= 0:
            racquet.x = 0