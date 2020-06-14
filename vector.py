import math
#class best representation because of operator overloading
"""
a list of three numbers used in many ways as it pertains to ray tracing.
"""
class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** .5

    def normalize(self):
        x = self.x/self.magnitude()
        y = self.y/self.magnitude()
        z = self.z/self.magnitude()
        return Vector(x, y, z)

    def dot(self, v2):
        return self.x*v2.x + self.y*v2.y + self.z*v2.z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector(x, y, z)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        z = self.z * other
        return Vector(x, y, z)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        z = self.z / other
        return Vector(x, y, z)

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"




if __name__ == "__main__":
    v = Vector(1, -2, -2)
    v2 = Vector(3, 6, 9)
    print(v.magnitude())
    nv = v.normalize()
    print(nv)
    print(v.dot(v2))
    av = v + v2
    print(av)
    sv = v - v2
    print(sv)
    mv = 2 * v
    print(mv)
    dv = v2 / 3
    print(dv)
