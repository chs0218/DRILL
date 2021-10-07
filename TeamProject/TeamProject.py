from pico2d import *

def handle_events():
    global playing
    global stageshow
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            playing = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                playing = False
            elif event.key == SDLK_UP:
                stageshow -= 1
                if stageshow < 0:
                    stageshow = 0
            elif event.key == SDLK_DOWN:
                stageshow = (stageshow + 1) % 3
    pass

DungeonWidth, DungeonHeight = 1160, 728
open_canvas(DungeonWidth, DungeonHeight)

village = load_image("map/village.png")
dungeon = load_image("map/background.png")

stageSelect = []
stageSelect.append(load_image("map/Stage_Normal.png"))
stageSelect.append(load_image("map/Stage_Hard.png"))
stageSelect.append(load_image("map/Stage_VeryHard.png"))

CharacterX = DungeonWidth // 2
CharacterY = DungeonHeight // 2
# village.draw(CharacterX, CharacterY)
# dungeon.draw(DungeonWidth // 2, DungeonHeight // 2)

playing = True
stageshow = 0

while playing:
    clear_canvas()
    stageSelect[stageshow].draw(DungeonWidth // 2, DungeonHeight // 2)
    update_canvas()
    handle_events()

close_canvas()
