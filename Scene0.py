# Scene0

import scene, sound

class Scene0(scene.Scene):
    def __init__(self, main_scene=None):
        self.main_scene = main_scene

    def draw(self):
        scene.background(1, 0, 0)

    def touch_began(self, touch):
        sound.play_effect('Coin_1')
        self.main_scene.switch_scenes()

if __name__ == '__main__':
    scene.run(Scene0())
