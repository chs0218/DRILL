import game_framework
import pico2d

import main_state

# pico2d.open_canvas(400, 300)
# pico2d.open_canvas(800, 600)
pico2d.open_canvas(1024, 768)
game_framework.run(main_state)
pico2d.close_canvas()