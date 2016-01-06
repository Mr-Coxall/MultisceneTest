# Scene1

import scene, sound

class Scene1(scene.Scene):
    def __init__(self, main_scene=None):
        self.main_scene = main_scene

    def draw(self):
        scene.background(0, 1, 0)

    def touch_began(self, touch):
        sound.play_effect('Beep')
        if self.main_scene:
            self.main_scene.switch_scenes()

if __name__ == '__main__':
    scene.run(Scene1())
