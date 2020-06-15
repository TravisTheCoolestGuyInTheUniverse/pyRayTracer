from image import Image
from pixel import Pixel


def main():
    ROWS = 2
    COLS = 3
    i = Image(ROWS, COLS, "P3")

    RED = Pixel(1, 0, 0)
    GREEN = Pixel(0, 1, 0)
    BLUE = Pixel(0, 0, 1)


    i.setPixel(0, 0, RED)
    i.setPixel(0, 1, GREEN)
    i.setPixel(0, 2, BLUE)
    i.setPixel(1, 0, RED + GREEN)
    i.setPixel(1, 1, RED+GREEN+BLUE)
    i.setPixel(1, 2, 0.001*RED)

    with open("out.ppm", "w") as f:
        i.imageToPPM(f)

if __name__ == "__main__":
    main()
