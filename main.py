from image import Image
from pixel import Pixel
from scene import Scene
from sphere import Sphere
from vector import Vector
from camera import Camera
from point import Point
from renderEngine import RenderEngine

def main():
    ROWS = 200
    COLS = 320
    i = Image(ROWS, COLS, "P3")

    RED = Pixel(1, 0, 0)
    GREEN = Pixel(0, 1, 0)
    BLUE = Pixel(0, 0, 1)

    ball = Sphere(Point(0, 0, 0), 0.5, Pixel.fromHex("#FF0000"))
    cam = Camera(Point(0, 0, -1))
    sne = Scene([ball], cam, ROWS, COLS)
    engine = RenderEngine()
    i = engine.render(sne)


    """i.setPixel(0, 0, RED)
    i.setPixel(0, 1, GREEN)
    i.setPixel(0, 2, BLUE)
    i.setPixel(1, 0, RED + GREEN)
    i.setPixel(1, 1, RED+GREEN+BLUE)
    i.setPixel(1, 2, 0.001*RED)
    """
    with open("out.ppm", "w") as f:
        i.imageToPPM(f)

if __name__ == "__main__":
    main()
