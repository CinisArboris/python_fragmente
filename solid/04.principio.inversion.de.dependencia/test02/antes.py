class ImageAntes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_dimensions(self):
        return (self.width, self.height)


class ImageProcessorAntes:
    def __init__(self, image):
        self.image = image

    def change_color(self, color):
        print(f"Cambiando el color de la imagen a {color}")
