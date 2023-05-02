from antes import ImageRotator
from despues import Rotate90, Rotate180, Rotate270


def antes_principio_abierto_cerrado():
    rotator = ImageRotator()
    image = "imagen.jpg"
    rotator.rotate(image, 90)
    rotator.rotate(image, 180)
    rotator.rotate(image, 270)


def dsepues_principio_abierto_cerrado():
    rotate90 = Rotate90()
    rotate180 = Rotate180()
    rotate270 = Rotate270()
    image = "imagen.jpg"
    rotate90.rotate(image)
    rotate180.rotate(image)
    rotate270.rotate(image)


if __name__ == '__main__':
    antes_principio_abierto_cerrado()
    print('-'*30)
    dsepues_principio_abierto_cerrado()
