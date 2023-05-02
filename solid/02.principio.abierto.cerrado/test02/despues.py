from abc import ABC, abstractmethod

class Rotation(ABC):
    @abstractmethod
    def rotate(self, image):
        pass

class Rotate90(Rotation):
    def rotate(self, image):
        print(f"Rotar la imagen {image} 90 grados")

class Rotate180(Rotation):
    def rotate(self, image):
        print(f"Rotar la imagen {image} 180 grados")

class Rotate270(Rotation):
    def rotate(self, image):
        print(f"Rotar la imagen {image} 270 grados")
