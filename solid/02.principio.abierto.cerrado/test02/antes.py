class ImageRotator:
    def rotate(self, image, angle):
        if angle == 90:
            print(f"Rotar la imagen {image} 90 grados")
        elif angle == 180:
            print(f"Rotar la imagen {image} 180 grados")
        elif angle == 270:
            print(f"Rotar la imagen {image} 270 grados")
        else:
            print("Ángulo de rotación no reconocido")
