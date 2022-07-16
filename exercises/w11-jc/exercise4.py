"""
Create classes to represent the objects needed for the final project. Create init methods for all
of them, checking that the provided values are correct.

"""

class Mario:
    def __init__(self, life:int):
        self.life = life


class Special_object:
    pass
class Mushroom(Special_object):
    pass
class Fire_flower(Special_object):
    pass
class Star(Special_object):
    pass

class Enemies:
    def __init__(self, change_direction: bool, dangerous: bool):
            self.change_direction = change_direction
            self.dangerous = dangerous

class Goomba(Enemies):
    def __init__(self, change_direction, dangerous):
        super().__init__(change_direction, dangerous)

class Koopa_Troopa(Enemies):
    def __init__(self, change_direction, dangerous):
        super().__init__(change_direction, dangerous)

class Block:
    def __init__(self, breakable: bool, special_object: Special_object):
        breakable = self.breakable
        special_object = self.special_object

class Enemy:
    def __init__(self):


class Special_object:
    def __init__(self):
