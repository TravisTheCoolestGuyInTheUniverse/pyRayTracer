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
                print("{:3.0f}%".format(float(j)/float(rows) * 100), end="\r")

        return pixels

    def rayTrace(self, ray, scene):
        color = Pixel(0, 0, 0)
        # Find nearest object hit by the ray in the scene
        distHit, objHit = self.findNearest(ray, scene)
        if objHit is None:
            return color
        hitPos = ray.origin + ray.direction * distHit
        hitNormal = objHit.normal(hitPos)
        color += self.colorAt(objHit, hitPos, hitNormal, scene)
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

    def colorAt(self, objHit, hitPos, normal, scene):
        material = objHit.material
        objColor = material.colorAt(hitPos)
        toCam = scene.camera.centerPoint - hitPos
        specularK = 50
        color = material.ambient * Pixel.fromHex("#000000")
        #light calculations
        for light in scene.lights:
            toLight = Ray(hitPos, light.position - hitPos)
            #diffuse shading
            color += (objColor * material.diffuse * max(normal.dot(toLight.direction), 0))
            #Specular shading
            halfVector = (toLight.direction + toCam).normalize()
            color += light.color * material.specular * max(normal.dot(halfVector), 0) ** specularK
        return color
