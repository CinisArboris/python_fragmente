class ImageProcessorAntes:
    def __init__(self):
        self.color_converter = RGBToGrayscaleConverterAntes()

    def process_image(self, image_data):
        print("Procesando imagen...")
        return self.color_converter.convert(image_data)


class RGBToGrayscaleConverterAntes:
    def convert(self, image_data):
        print("Convirtiendo imagen RGB a escala de grises...")
        return image_data
