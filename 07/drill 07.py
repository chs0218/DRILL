from pico2d import *
from random import randint

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
    pass

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
hand_arrow = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')

running = True

frame = 0
frameline = 0
x = 300
y = 300
Arrow_X = randint(0, KPU_WIDTH)
Arrow_Y = randint(0, KPU_HEIGHT)

hand_arrow.draw(Arrow_X, Arrow_Y)


while running:
    sec = 0
    Arrow_X = randint(0, 600)
    Arrow_Y = randint(0, 600)
    if Arrow_X > x:
        frameline = 1
    else:
        frameline = 0
    distanceX = (x - Arrow_X) / 15
    distanceY = (y - Arrow_Y) / 15
    while(sec < 15):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        hand_arrow.draw(Arrow_X, Arrow_Y)
        character.clip_draw(frame * 100, 100 * frameline, 100, 100, x, y)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
    
        x -= distanceX
        y -= distanceY

        sec += 1
        delay(0.05)
    handle_events()

close_canvas()
