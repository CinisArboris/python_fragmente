from antes import ImageAntes, SquareImageAntes
from despues import ImageDespues, SquareImageDespues


def antes_principio_sustitucion_liskov():
    image = SquareImageAntes(100)
    print(f"Dimensiones de la imagen: {image.get_dimensions()}")
    image_as_image = ImageAntes(100, 100)
    print(f"Dimensiones de la imagen como Image: {image_as_image.get_dimensions()}")


def despues_principio_sustitucion_liskov():
    image = SquareImageDespues(100)
    print(f"Dimensiones de la imagen: {image.get_dimensions()}")
    image_as_image = ImageDespues(100, 100)
    print(f"Dimensiones de la imagen como Image: {image_as_image.get_dimensions()}")


if __name__ == '__main__':
    antes_principio_sustitucion_liskov()
    print('-'*30)
    despues_principio_sustitucion_liskov()
