
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

class Image:
    def __init__(self, rows, cols, imgFormat):
        self.rows = rows
        self.cols = cols
        self.imgFormat = imgFormat
        self.pixels = [[Pixel() for _ in range(cols)] for _ in range(rows)]


    def imageToPPM(self, outFileName):
        f = open(outFileName, "w")
        f.write(f"{self.imgFormat} {self.cols} {self.rows}\n 255")
        for row in self.pixels:
            f.write("\n")
            for col in row:
                f.write(f"{col.r*255} {col.g*255} {col.b*255} ")


RED = Pixel(1, 0, 0)
GREEN = Pixel(0, 1, 0)
BLUE = Pixel(0, 0, 1)



if __name__ == "__main__":

    i = Image(2, 3, "P3")
    i.pixels[0][0] = RED
    i.pixels[0][1] = GREEN
    i.pixels[0][2] = BLUE
    i.pixels[1][0] = RED + GREEN
    i.pixels[1][1] = RED + GREEN + BLUE
    i.pixels[1][2] = 0.001 * RED

    i.imageToPPM("out.ppm")


    """f = open("out.ppm", "w")
    f.write("P3 3 2\n255\n")
    f.write()"""
