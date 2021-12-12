from ursina import *
from ursina import collider
from ursina.color import rgba
from ursina.prefabs.first_person_controller \
    import FirstPersonController
import random

from ursina.scripts.colorize import colorize


class Block(Button):
    def __init__(self, pos):
        super().__init__()
        self.parent = scene
        self.model = 'cube'
        self.collider = 'box'
        self.color = color.color(0, 0, 1)

        self.texture = load_texture('assets/default')
        self.origin_y = 0.5
        self.parent = scene
        self.position = pos
        self.hardness = 5
        self.highlight_color = color.white

    def destroy(self):
        self.hardness -= 1


class bedrock(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.texture = load_texture('assets/bedrock')
        self.hardness = 10000

    def destroy(self):
        self.highlight_color = color.red


class grass(Block):
    def __init__(self, pos, var):
        super().__init__(pos)
        self.texture = load_texture('assets/grass-' + str(var))
        self.hardness = 1


class log(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.texture = load_texture('assets/log')
        self.hardness = 1


class glass(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.texture = load_texture('assets/glass')
        self.hardness = 1


class iron(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.texture = load_texture('assets/iron')
        self.hardness = 1
