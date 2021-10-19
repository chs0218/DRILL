from pico2d import *
import random


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


class Ball:
    def __init__(self):
        self.x = random.randint(0, 599)
        self.y = 599
        self.image = load_image('ball21x21.png')

    def draw(self):
        self.image.draw(self.x, self.y - 10)


running = True
open_canvas(600, 600)

Balls = [Ball() for i in range(10)]
while running:
    for i in range(10):
        Balls[i].draw()
    update_canvas()
    handle_events()

