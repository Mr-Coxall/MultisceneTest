# In this example, the program switches between 3 different scenes.

import importlib, inspect, scene, MultiScene

# assumes module name == scene name as in Scene0.Scene0
def find_scenes():  # Scene0.Scene0, Scene1.Scene1, Scene2.Scene2...
    for i in xrange(999):
        scene_name = 'Scene{}'.format(i)
        try:
            module = importlib.import_module(scene_name)
        except ImportError:
            return
        class_members = inspect.getmembers(module, inspect.isclass)
        yield [sc[1] for sc in class_members if sc[0] == scene_name][0]

class SceneSwitcher(MultiScene.MultiScene):
    def __init__(self):
        self.scenes = [scn for scn in find_scenes()]
        assert self.scenes, 'No Scene files found!'
        print('{} scenes imported: {}'.format(len(self.scenes), self.scenes))
        self.scene_index = -1
        self.switch_scenes()
        scene.run(self, orientation=scene.LANDSCAPE)

    @property
    def next_scene(self):
        self.scene_index += 1
        return self.scenes[self.scene_index % len(self.scenes)]

    def switch_scenes(self):
        self.switch_scene(self.next_scene(self))

SceneSwitcher()
