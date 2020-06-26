



    ROWS = 200
    COLS = 320
    i = Image(ROWS, COLS, "P3")

    RED = Pixel(1, 0, 0)
    GREEN = Pixel(0, 1, 0)
    BLUE = Pixel(0, 0, 1)

    ball = Sphere(Point(0.75, -0.1, 1), 0.6, Material(Pixel.fromHex("#0000FF")))
    ball2 = Sphere(Point(-0.75, -0.1, 2.25), 0.6, Material(Pixel.fromHex("#803980")))
    ground = Sphere(Point(0, 10000.5, 1), 10000, Material(Pixel.fromHex("FF0000"), 0.2, 0.2))

    cam = Camera(Point(0, -0.35, -1))
    light1 = Light(Point(1.5, -0.5, -10.0), Pixel.fromHex("#FFFFFF"))
    light2 = Light(Point(-0.5, -10.5, 0), Pixel.fromHex("#E6E6E6"))
    lights = [light1, light2]
    sne = Scene([ball, ball2, ground], lights, cam, ROWS, COLS)
    engine = RenderEngine()
    i = engine.render(sne)
