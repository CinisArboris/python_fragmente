from antes import ImageProcessor
from despues import ImageLoader, ImageConverter, ImageSaver


def antes_aplicar_responsabilidad_unica():
    processor = ImageProcessor()
    image = processor.load_image('ruta/imagen.jpg')
    grayscale_image = processor.convert_to_grayscale(image)
    processor.save_image(grayscale_image, 'ruta/imagen_grayscale.jpg')


def despues_aplicar_responsabilidad_unica():
    loader = ImageLoader()
    converter = ImageConverter()
    saver = ImageSaver()
    image = loader.load_image('ruta/imagen.jpg')
    grayscale_image = converter.convert_to_grayscale(image)
    saver.save_image(grayscale_image, 'ruta/imagen_grayscale.jpg')


if __name__ == '__main__':
    antes_aplicar_responsabilidad_unica()
    print('-'*30)
    despues_aplicar_responsabilidad_unica()
