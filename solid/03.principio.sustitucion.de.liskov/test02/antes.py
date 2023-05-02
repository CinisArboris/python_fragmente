class ImageAntes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_dimensions(self):
        return (self.width, self.height)


class SquareImageAntes(ImageAntes):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def get_dimensions(self):
        return (self.side, self.side)
