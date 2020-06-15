from pixel import Pixel
class Image:
    def __init__(self, rows, cols, imgFormat):
        self.rows = rows
        self.cols = cols
        self.imgFormat = imgFormat
        self.pixels = [[None for _ in range(cols)] for _ in range(rows)]

    def setPixel(self, row, col, pixel):
        self.pixels[row][col] = pixel


    def imageToPPM(self, f):
        def toByte(p):
            return round(max(min(p * 255, 255), 0))

        f.write(f"{self.imgFormat} {self.cols} {self.rows}\n 255")
        for row in self.pixels:
            f.write("\n")
            for col in row:
                f.write(f"{toByte(col.r)} {toByte(col.g)} {toByte(col.b)} ")
