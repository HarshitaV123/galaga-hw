import pgzrun
import random


WIDTH = 1200
HEIGHT = 600
center_x=WIDTH/2
center_y=HEIGHT/2


WHITE = (255,255,255)
BLACK = (0,0,0)


score = 0
lives = 3


#creating the racquet
racquet = Actor("tennis raqcuet")
racquet.pos = (WIDTH //2,HEIGHT-60)


balls = []
enemies = []


#creating the enemies
for i in range(8):
    enemy=Actor("fire")
    enemy.x = random.randint(0, WIDTH -100)
    enemy.y = random.randint(-100,0)
    enemies.append(enemy)


#set enemy movement direction
direction = 1


#set enemy movement speed
speed = 5


#function to display score
def display_score():
    global score, lives
    screen.draw.text(f"Score: {score}",(50,30))
    screen.draw.text(f"Lives: {lives}",(50,60))


#function to handle key down events
def on_key_down(key):
    if key == keys.SPACE:
        #create a new ball
        ball=Actor("tennis ball")
        ball.x = racquet.x
        ball.y = racquet.y - 50
        balls.append(ball)


#function to update the game
def update():
    global lives
    global score
    global direction
    global enemies


    #move the racquet left or right
    if keyboard.right:
        racquet.x += speed
        if racquet.x >= WIDTH:
            racquet.x = WIDTH
    elif keyboard.left:
        racquet.x -= speed
        if racquet.x <= 0:
            racquet.x = 0


    #move the balls
    for ball in balls:
        if ball.y <=0:
            balls.remove(ball)
        else:
            ball.y -=10
        
    #move enemies
    for enemy in enemies:
        enemy.y += 3
        if enemy.y> HEIGHT:
            enemy.x = random.randint(0,WIDTH-80)
            enemy.y = random.randint(-100,0)


        #check for collisions with the balls
        for ball in balls:
            if enemy.colliderect(ball):
                score +=100
                balls.remove(ball)
                enemies.remove(enemy)


        #check for collisions with the racquet
        if enemy.colliderect(racquet):
            lives = lives - 1
            enemies.remove(enemy)
            if lives == 0:
                game_over()
    if len(enemies)<8:
        enemy = Actor("fire")
        enemy.x = random.randint(0,WIDTH-80)
        enemy.y= random.randint(-100,0)
        enemies.append(enemy)


#function to draw the game state
def draw():
    if lives > 0:
        screen.clear()
        screen.fill(BLACK)
        for ball in balls:
            ball.draw()
        for enemy in enemies:
            enemy.draw()
        racquet.draw()
        display_score()
    else:
        game_over_screen()


def game_over():
    pass


def game_over_screen():
    screen.clear()
    screen.fill(BLACK)
    screen.draw.text("Game Over",(center_x,center_y),fontsize=50,color=WHITE)
    screen.draw.text(f"End Score: {score}",(center_x,center_y + 50),fontsize=50,color=WHITE)
    screen.draw.text("Press space to play again",(center_x,center_y-100),fontsize=50,color=WHITE)


    if keyboard.SPACE:
        restart_game()
    
#function to restart game
def restart_game():
    global balls, score, lives, enemies
    score = 0
    lives = 3
    balls = []
    enemies = []
    for i in range(8):
        enemy = Actor("fire")
        enemy.x = random.randint(0,WIDTH - 80)
        enemy.y = random.randint(-100,0)
        enemies.append(enemy)






pgzrun.go()
