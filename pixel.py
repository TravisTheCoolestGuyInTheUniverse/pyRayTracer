
"""
stores color information in rgb triplets.
"""
class Pixel:
    def __init__(self, r=0.0, g=0.0, b=0.0):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, other):
        r = self.r + other.r
        g = self.g + other.g
        b = self.b + other.b
        return Pixel(r, g, b)

    def __sub__(self, other):
        r = self.r - other.r
        g = self.g - other.g
        b = self.b - other.b
        return Pixel(r, g, b)

    def __mul__(self, other):
        r = self.r * other
        g = self.g * other
        b = self.b * other
        return Pixel(r, g, b)

    def __rmul__(self, other):
        return self.__mul__(other)

    @classmethod
    def fromHex(cls, hexcolor="#000000"):
        r = int(hexcolor[1:3], 16)/255.0
        g = int(hexcolor[3:5], 16)/255.0
        b = int(hexcolor[5:7], 16)/255.0
        return cls(r, g, b)
