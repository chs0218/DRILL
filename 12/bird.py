import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel은 30cm
BIRD_SIZE = 50 # 새는 50 픽셀의 크기이며 새의 크기는 약 150cm
FLY_SPEED_KMPH = 30.0  # 새가 나는 속도 30km/h
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5 # 한번 날개짓을 하는데 0.5초가 걸림
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14 # 한번의 날갯짓은 14 프레임

class Bird:
    image = None
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x = random.randint(100, 1400)
        self.y = 450
        self.dir = random.randint(0, 1)

        if self.dir == 0:
            self.dir -= 1

        self.frame = 0
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y, BIRD_SIZE, BIRD_SIZE)
        else:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100,
                                           0, 'h', self.x, self.y, BIRD_SIZE, BIRD_SIZE)
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        if self.x < 25:
            self.dir = 1
        elif self.x > 1600 - 25:
            self.dir = -1
        pass