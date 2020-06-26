from pixel import Pixel

"""contains properties that describe how an object interacts with light"""
class Material:
    def __init__(self, color=Pixel.fromHex("#FFFFFF"), ambient=0.05, diffuse=1.0, specular=1.0):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular

    def colorAt(self, position):
        return self.color
