from pico2d import *
import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.3)
BALL_KM_PER_HOUR = 108.0
BALL_M_PER_SEC = BALL_KM_PER_HOUR * 1000.0 / 3600.0
BALL_SPEED_PPS = (BALL_M_PER_SEC * PIXEL_PER_METER)

class Ball:
    image = None
    def __init__(self, x = 400, y = 300, velocity = 0):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += BALL_SPEED_PPS * game_framework.frame_time * self.velocity

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
