class ImageProcessorDespues:
    def __init__(self, color_converter):
        self.color_converter = color_converter

    def process_image(self, image_data):
        print("Procesando imagen...")
        return self.color_converter.convert(image_data)


class RGBToGrayscaleConverterDespues:
    def convert(self, image_data):
        print("Convirtiendo imagen RGB a escala de grises...")
        return image_data
