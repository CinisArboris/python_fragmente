from antes import ImageAntes, ImageProcessorAntes
from despues import ImageEditorDespues, ImageProcessorDespues


def antesDeAplicarPrincipioInversionDeDependencia():
    print("Antes de aplicar el principio de inversión de dependencia:")
    image = ImageAntes(200, 100)
    processor = ImageProcessorAntes(image)
    processor.change_color("rojo")


def despuesDeAplicarPrincipioInversionDeDependencia():
    print("Después de aplicar el principio de inversión de dependencia:")
    image = (200, 100) # Imagen representada por una tupla de tamaño (ancho, alto)
    processor = ImageProcessorDespues()
    editor = ImageEditorDespues(image)
    editor.process(processor)


if __name__ == '__main__':
    antesDeAplicarPrincipioInversionDeDependencia()
    print("------------------------------")
    despuesDeAplicarPrincipioInversionDeDependencia()
