from antes import ImageAntes, AnimatedImageAntes
from despues import ImageDespues, AnimatedImageDespues


def antes_principio_sustitucion_liskov():
    image = ImageAntes()
    image.load('ruta/imagen.jpg')
    image.save('ruta/imagen_guardada.jpg')
    try:
        animated_image = AnimatedImageAntes()
        animated_image.load('ruta/imagen_animada.gif')
        animated_image.save('ruta/imagen_animada_guardada.gif')
        animated_image.animate()
    except NotImplementedError as e:
        print(f"Se ha producido una excepción: {str(e)}")


def despues_principio_sustitucion_liskov():
    image = ImageDespues()
    image.load('ruta/imagen.jpg')
    image.save('ruta/imagen_guardada.jpg')
    animated_image = AnimatedImageDespues()
    animated_image.load('ruta/imagen_animada.gif')
    animated_image.save('ruta/imagen_animada_guardada.gif')
    animated_image.animate()


if __name__ == '__main__':
    antes_principio_sustitucion_liskov()
    print('-'*30)
    despues_principio_sustitucion_liskov()