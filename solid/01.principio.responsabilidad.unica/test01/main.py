from antes import ImageProcessor
from despues import ImageLoader, ImageResizer, ImageSaver


def antes_aplicar_responsabilidad_unica():
    processor = ImageProcessor()

    image = processor.load_image('ruta/imagen.jpg')
    resized_image = processor.resize_image(image, (800, 600))
    processor.save_image(resized_image, 'ruta/imagen_redimensionada.jpg')


def despues_aplicar_responsabilidad_unica():
    loader = ImageLoader()
    resizer = ImageResizer()
    saver = ImageSaver()

    image = loader.load_image('ruta/imagen.jpg')
    resized_image = resizer.resize_image(image, (800, 600))
    saver.save_image(resized_image, 'ruta/imagen_redimensionada.jpg')


if __name__ == '__main__':
    antes_aplicar_responsabilidad_unica()
    print('-'*30)
    despues_aplicar_responsabilidad_unica()
