from ursina import *
from ursina import collider
from ursina.color import rgba
from ursina.prefabs.first_person_controller \
    import FirstPersonController
import random
from ursina.shaders import basic_lighting_shader
from ursina.shaders import colored_lights_shader


from ursina.scripts.colorize import colorize
defaultpath = "assets/blocks/"


class Block(Button):
    def __init__(self, pos):
        super().__init__()
        self.parent = scene
        self.model = 'cube'
        self.collider = 'box'
        self.color = color.color(0, 0, 1)

        self.texture = load_texture(defaultpath+'default')
        self.origin_y = 0.5
        self.parent = scene
        self.position = pos
        self.hardness = 5
        self.highlight_color = color.white
        shader = colored_lights_shader

    def destroy(self):
        self.hardness -= 1


class bedrock(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "bedrock"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 10000

    def destroy(self):
        self.highlight_color = color.red


class grass(Block):
    def __init__(self, pos, var):
        super().__init__(pos)
        self.name = "grass"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1


class dirt(Block):
    def __init__(self, pos, var):
        super().__init__(pos)
        self.name = "dirt"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1


class mud(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "mud"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class mudBrick(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "mud-brick"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class sand(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "sand"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1

class clay(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "clay"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1
class stone(Block):
    def __init__(self, pos,var):
        super().__init__(pos)
        self.name = "stone"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1


class stoneBrick(Block):
    def __init__(self, pos,var):
        super().__init__(pos)
        self.name = "stone-brick"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1


class stoneTiles(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "stone-tiles"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class terracotta(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "terracotta"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class brick(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "brick"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class terracottaTiles(Block):
    def __init__(self, pos,var):
        super().__init__(pos)
        self.name = "terracotta-tiles"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1


class concrete(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "concrete"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class concreteBrick(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "concrete-brick"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class concretePillar(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "concrete-pillar"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class log(Block):
    def __init__(self, pos,var):
        super().__init__(pos)
        self.name = "log"
        self.texture = load_texture(defaultpath + self.name + '-' + str(var))
        self.hardness = 1

class leaves(Block):
    def __init__(self, pos):
        super().__init__(pos)
        # self.Branches = Block(texture=load_texture(defaultpath + "branches"), scale=(0.6,0.6,0.6))

        self.name = "leaves"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class wood(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "wood"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class ash(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "ash"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class glass(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "glass"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1


class iron(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.name = "iron"
        self.texture = load_texture(defaultpath + self.name)
        self.hardness = 1
