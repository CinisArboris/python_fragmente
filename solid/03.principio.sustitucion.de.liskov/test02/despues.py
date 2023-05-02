class ImageDespues:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_dimensions(self):
        return (self.width, self.height)


class SquareImageDespues(ImageDespues):
    def __init__(self, side):
        super().__init__(side, side)

    def get_dimensions(self):
        return (self.width, self.height)
