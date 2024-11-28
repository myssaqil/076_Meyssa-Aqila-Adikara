
class RectangleController:
    width = 0
    height =0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculateLuas(self):
        return self.width * self.height

