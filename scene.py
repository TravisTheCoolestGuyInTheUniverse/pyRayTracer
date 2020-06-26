class Scene:
    """
    contains all information necessary for ray tracing engine to render an image
    """
    def __init__(self, objects, lights, camera, rows, cols):
        self.objects = objects
        self.lights = lights
        self.camera = camera
        self.rows = rows
        self.cols = cols

    def addObject(self, object):
        self.objects.append(object)
