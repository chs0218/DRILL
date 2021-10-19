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
        self.speed = random.randint(5, 10)
        self.key = random.randint(0, 1)
        if self.key == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

    def falling(self):
        if self.key == 0:
            if self.y > 70:
                self.y -= self.speed
            else:
                self.y = 70
        else:
            if self.y > 80:
                self.y -= self.speed
            else:
                self.y = 80

    def draw(self):
        self.image.draw(self.x, self.y - 10)


running = True
open_canvas(600, 600)
grass = load_image('grass.png')

Balls = [Ball() for i in range(20)]
while running:
    clear_canvas()
    grass.draw(300, 30)
    for i in range(10):
        Balls[i].falling()
        Balls[i].draw()
    update_canvas()
    handle_events()

