from pico2d import *
import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.3)
BIRD_KM_PER_HOUR = 40.0
BIRD_M_PER_SEC = BIRD_KM_PER_HOUR * 1000.0 / 3600.0
BIRD_SPEED_PPS = (BIRD_M_PER_SEC * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

Bird_image_width = 918 // 5
Bird_image_height = 506 // 3

class Bird:
    image = None
    def __init__(self, x = 400, y = 400, velocity = 1):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frameX = 0
        self.frameY = 2

    def draw(self):
        self.image.clip_draw(int(self.frameX) * Bird_image_width, int(self.frameY) * Bird_image_height,
                             Bird_image_width, Bird_image_height, self.x, self.y)

    def update(self):
        self.x += BIRD_SPEED_PPS * game_framework.frame_time * self.velocity
        self.frameX = (self.frameX + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)

        if self.frameX > 5:
            self.frameY = (self.frameY - 1) % 3
            self.frameX = self.frameX % 5

        if self.x < 25 or self.x > 1600 - 25:
            self.x = 25
