from pixel import Pixel
from image import Image
from vector import Vector
from ray import Ray
from point import Point

"""
renders 3d objects into 2d objects using ray tracing.
"""
class RenderEngine:

    def render(self, scene):
        rows = scene.rows
        cols = scene.cols
        aspectRatio = float(cols) / rows
        x0 = -1.0
        x1 = +1.0
        xstep = (x1 - x0) / (cols - 1)
        y0 = -1.0 / aspectRatio
        y1 = +1.0 / aspectRatio
        ystep = (y1 - y0) / (rows - 1)

        camera = scene.camera
        pixels = Image(rows, cols, "P3")

        """
        using the aspect ratio above, send out a ray from each pixel as it relates
        to where it would be located in the virtual world towards positve z values.
        
        """
        for j in range(rows):
            y = y0 + j * ystep
            for i in range(cols):
                x = x0 + i * xstep
                ray = Ray(camera.centerPoint, Point(x, y) - camera.centerPoint)
                pixels.setPixel(j, i, self.rayTrace(ray, scene))

        return pixels

    def rayTrace(self, ray, scene):
        color = Pixel(0, 0, 0)
        # Find nearest object hit by the ray in the scene
        distHit, objHit = self.findNearest(ray, scene)
        if objHit is None:
            return color
        hitPos = ray.origin + ray.direction * distHit
        color += self.colorAt(objHit, hitPos, scene)
        return color

    def findNearest(self, ray, scene):
        distMin = None
        objHit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (objHit is None or dist < distMin):
                distMin = dist
                objHit = obj
        return (distMin, objHit)

    def colorAt(self, objHit, hitPos, scene):
        return objHit.color
