import turtle
import random
import math
import platform

if platform.system() == "Windows":
    try:
        import winsound
    except:
        print("winsound module not available")

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("space invaders")
screen.bgpic("intro.gif")
screen.tracer(0)

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

turtle.register_shape("alien.gif")
turtle.register_shape("player.gif")
turtle.register_shape("bullet.gif")

player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
playerspeed = 15



missle = turtle.Turtle()
missle.color('red')
missle.shape('circle')
missle.penup()
missle.speed(0.25)
missle.setheading(90)
missle.shapesize(.4,.4)
missle.hideturtle()

misslespeed = 0.2
missleact ='ready'
def shootmissle():
    global missleact
    if missleact == "ready":
        missleact = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        missle.setposition(x, y)
        missle.showturtle()




#Player Movement
speedplayer = 50
def shift_left():
    x = player.xcor()
    x -= speedplayer
    if x < -300:
        x = - 300
    player.setx(x)
def shift_right():
    x = player.xcor()
    x += speedplayer
    if x > 300:
        x = 300
    player.setx(x)
    #Main game loop
#Binding Keys to an action
turtle.listen()
turtle.onkey(shift_left,"Left")
turtle.onkey(shift_right, "Right")
turtle.onkey(shootmissle, "space")
#keeps turtle window open



num_of_enemies = 30
enemies = []
for enemy in range(num_of_enemies):
    enemies.append(turtle.Turtle())
enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.color("green")
    enemy.shape("alien.gif")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50*enemy_number)
    y = enemy_start_y
    enemy.setposition(x,y)
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0
enemyspeed = 0.1
score = 0

#Draw score
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color('white')
scoreboard.penup()
scoreboard.setposition(-290,300)
scorestring = "Score: %s" %score
scoreboard.write(scorestring,False,align="left",font=('Arial',15,'normal'))
scoreboard.hideturtle()

mcontrol = turtle.Turtle()
mcontrol.speed(0)
mcontrol.color('white')
mcontrol.penup()
mcontrol.setposition(-100,25)
mstring = "WELCOME TO SPACE INVADERS"
mcontrol.write(mstring,False,align="left",font=('Arial',15,'normal'))
mcontrol.hideturtle()

lcontrol = turtle.Turtle()
lcontrol.speed(0)
lcontrol.color('white')
lcontrol.penup()
lcontrol.setposition(-75,0)
lstring = "Left key to move left"
lcontrol.write(lstring,False,align="left",font=('Arial',15,'normal'))
lcontrol.hideturtle()

rcontrol = turtle.Turtle()
rcontrol.speed(0)
rcontrol.color('white')
rcontrol.penup()
rcontrol.setposition(-75,-25)
rstring = "Right key to move Right"
rcontrol.write(rstring,False,align="left",font=('Arial',15,'normal'))
rcontrol.hideturtle()


scontrol = turtle.Turtle()
scontrol.speed(0)
scontrol.color('white')
scontrol.penup()
scontrol.setposition(-75,-50)
sstring = "Space to shoot"
scontrol.write(sstring,False,align="left",font=('Arial',15,'normal'))
scontrol.hideturtle()


def collisionTrue(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 10:
        return True
    else:
         return False

def play_sound(sound_file, time=0):
    if platform.system == "windows":
        winsound.PlaySound(laser.wav, winsound.SND_ASYNC)


while True:
    screen.update()
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if missleact == "fire":
            y = missle.ycor()
            y += misslespeed
            missle.sety(y)
        if missle.ycor () > 275:
            missle.hideturtle()
            missleact = "ready"
        if collisionTrue(missle,enemy):
            missle.hideturtle()
            missleact = "ready"
            missle.setposition(0,-400)
            enemy.setposition(0,100000)
            score += 10
            scorestring = "score: %s" %score
            scoreboard.clear()
            scoreboard.write(scorestring, False, align="left", font=('Arial', 15, 'normal'))
        if score >= 10:
            mcontrol.clear()
            lcontrol.clear()
            rcontrol.clear()
            scontrol.clear()
        if collisionTrue(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("game over")
            break


turtle.mainloop()
