# Scene2

import scene, sound

class Scene2(scene.Scene):
    def __init__(self, main_scene=None):
        self.main_scene = main_scene

    def draw(self):
        scene.background(0, 0, 1)

    def touch_began(self, touch):
        sound.play_effect('Clank')
        if self.main_scene:
            self.main_scene.switch_scenes()

if __name__ == '__main__':
    scene.run(Scene2())
