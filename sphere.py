from vector import Vector
from pixel import Pixel

class Sphere:
    """
    Sphere class. defined by center, radius, and color.
    """
    def __init__(self, centerPoint, radius, color):
        self.centerPoint = centerPoint
        self.radius = radius
        self.color = color

    """
    interesting that the intersect function is here in the tutorial.

    checks if ray intersects this sphere. returns distance to intersection or None
    if there is no intersection.
    """
    def intersects(self, ray):
        sphereToRay = ray.origin - self.centerPoint
        #a = 1
        b = 2 * ray.direction.dot(sphereToRay)
        c = sphereToRay.dot(sphereToRay) - self.radius * self.radius
        discriminant = b * b - 4 * c

        if discriminant >=0:
            dist = (-b - discriminant ** .5) / 2
            if dist > 0:
                return dist
        return None
