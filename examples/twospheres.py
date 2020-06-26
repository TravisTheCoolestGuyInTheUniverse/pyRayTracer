from image import Image
from pixel import Pixel
from scene import Scene
from sphere import Sphere
from vector import Vector
from camera import Camera
from point import Point
from material import Material, ChequeredMaterial
from light import Light

COLS = 1920
ROWS = 1080
RENDEREDIMG = "twospheres.ppm"
CAMERA = Camera(Vector(0, -0.35, -1))
OBJECTS = [
#Ground
Sphere(Point(0, 10000.5, 1), 10000.0, ChequeredMaterial(color1 = Pixel.fromHex("#420500"),
color2 = Pixel.fromHex("#E6B87D"),
ambient = 0.2,
reflection = 0.2)),
#Blue ball
Sphere(Point(0.75, -.1, 1), 0.6, Material(Pixel.fromHex("#0000FF"))),
#Pink ball
Sphere(Point(-0.75, -0.1, 2.25), 0.6, Material(Pixel.fromHex("#803980")))
]
LIGHTS = [
Light(Point(1.5, -.5, -10), Pixel.fromHex("#FFFFFF")),
Light(Point(-.5, -10, -10), Pixel.fromHex("#E6E6E6"))]
