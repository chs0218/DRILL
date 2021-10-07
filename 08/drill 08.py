from pico2d import *
from random import randint


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
    pass

def move_character():
    global x, y, Arrow_X, Arrow_Y, frameline
    t = 0.01
    x = (1 - t) * x + t * Arrow_X
    y = (1 - t) * y + t * Arrow_Y

    dist = (x - Arrow_X) ** 2 + (y - Arrow_Y) ** 2

    if dist < 10 ** 2:
        Arrow_X = randint(0, KPU_WIDTH)
        Arrow_Y = randint(0, KPU_HEIGHT)
        if Arrow_X > x:
            frameline = 1
        elif Arrow_X < x:
            frameline = 0
        else:
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

while running:
    move_character()
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.draw(Arrow_X, Arrow_Y)
    character.clip_draw(frame * 100, 100 * frameline, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

close_canvas()
