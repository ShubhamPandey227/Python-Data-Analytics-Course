# for inserting png images without background
import pgzrun
music.play('thor')
music.set_volume(0.3)

b = Actor('cars', (80,60))
vx , vy= 3, 2

def draw() :
    screen.fill('white')
    b.draw()

def update() :
    global vx, vy
    b.x += vx
    b.y += vy
    if b.right > 800 or b.left < 0 :
        vx = -vx
        sounds.retro.play()
    if b.bottom > 600 or b.top < 0 :
        vy = -vy
        sounds.retro.play()
pgzrun.go()