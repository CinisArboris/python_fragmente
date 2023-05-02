from antes import ImageProcessorAntes
from despues import ImageProcessorDespues, RGBToGrayscaleConverterDespues


def antesInversionDependencia():
    image_processor = ImageProcessorAntes()
    image_data = "datos de la imagen"
    result = image_processor.process_image(image_data)
    print(f"Resultado del procesamiento de la imagen: {result}")


def despuesInversionDependencia():
    color_converter = RGBToGrayscaleConverterDespues()
    image_processor = ImageProcessorDespues(color_converter)
    image_data = "datos de la imagen"
    result = image_processor.process_image(image_data)
    print(f"Resultado del procesamiento de la imagen: {result}")


if __name__ == '__main__':
    antesInversionDependencia()
    print('-'*30)
    despuesInversionDependencia()
