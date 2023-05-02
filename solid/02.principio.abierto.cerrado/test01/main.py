from antes import ImageFilter
from despues import GrayscaleFilter, SepiaFilter, BlurFilter


def antes_principio_abierto_cerrado():
    filter_processor = ImageFilter()
    image = "imagen.jpg"
    filter_processor.apply_filter(image, 'grayscale')
    filter_processor.apply_filter(image, 'sepia')
    filter_processor.apply_filter(image, 'blur')


def dsepues_principio_abierto_cerrado():
    grayscale_filter = GrayscaleFilter()
    sepia_filter = SepiaFilter()
    blur_filter = BlurFilter()
    image = "imagen.jpg"
    grayscale_filter.apply(image)
    sepia_filter.apply(image)
    blur_filter.apply(image)


if __name__ == '__main__':
    antes_principio_abierto_cerrado()
    print('-'*30)
    dsepues_principio_abierto_cerrado()
