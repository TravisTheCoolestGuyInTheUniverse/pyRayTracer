from image import Image
from pixel import Pixel
from scene import Scene
from sphere import Sphere
from vector import Vector
from camera import Camera
from point import Point
from renderEngine import RenderEngine
from material import Material
from light import Light
import argparse
import importlib
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene", help="Path to scene file (without .py extension)")
    args = parser.parse_args()
    mod = importlib.import_module(args.scene)
    scene = Scene(mod.OBJECTS, mod.LIGHTS, mod.CAMERA, mod.ROWS, mod.COLS)
    engine = RenderEngine()
    image = engine.render(scene)

    os.chdir(os.path.dirname(os.path.abspath(mod.__file__)))
    with open(mod.RENDEREDIMG, "w") as f:
        image.imageToPPM(f)

if __name__ == "__main__":
    main()
