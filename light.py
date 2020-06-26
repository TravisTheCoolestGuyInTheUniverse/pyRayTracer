from pixel import Pixel

"""Light represents a point in space that emits light"""
class Light:
    def __init__(self, position, color):
        self.position = position
        self.color = color
