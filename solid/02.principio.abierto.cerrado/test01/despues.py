from abc import ABC as BaseFilter, abstractmethod

class ImageFilter(BaseFilter):
    @abstractmethod
    def apply(self, image):
        pass

class GrayscaleFilter(ImageFilter):
    def apply(self, image):
        print("Aplicar filtro de escala de grises a la imagen")

class SepiaFilter(ImageFilter):
    def apply(self, image):
        print("Aplicar filtro sepia a la imagen")

class BlurFilter(ImageFilter):
    def apply(self, image):
        print("Aplicar filtro de desenfoque a la imagen")
