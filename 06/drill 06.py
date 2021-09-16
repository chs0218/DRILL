from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# clear screen and draw grass
def clearNdraw():
    clear_canvas_now()
    grass.draw_now(400, 30)
    
# Circle Radius Value
r = 210

while True:
    # define Character Location
    x = 400
    y = 90

    # from left to right move
    while x < 780:
        clearNdraw()
        character.draw_now(x, y)
        x+=2
        delay(0.01)

    # from bottom to top move
    while y< 560:
        clearNdraw()
        character.draw_now(x, y)
        y+=2
        delay(0.01)

    # from right to left move
    while x > 20:
        clearNdraw() 
        character.draw_now(x, y)
        x-=2
        delay(0.01)

    # from top to bottom move
    while y > 90:
        clearNdraw()
        character.draw_now(x, y)
        y-=2
        delay(0.01)

    # from left to first place move
    while x < 400:
        clearNdraw()
        character.draw_now(x, y)
        x+=2
        delay(0.01)

    # define Circle Point and Circle Degree
    x = 400
    y = 300
    degree = -90
    
    # Circle Move
    while degree < 270:
        clearNdraw()
        character.draw_now(x + r * math.cos(degree / 360 * 2 * math.pi), y + r * math.sin(degree / 360 * 2 * math.pi))
        degree += 1
        delay(0.01)

   
close_canvas()
