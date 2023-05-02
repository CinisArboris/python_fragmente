class ImageLoader:
    def load_image(self, file_path):
        # Carga una imagen desde un archivo
        print("Cargar imagen desde el archivo:", file_path)

class ImageResizer:
    def resize_image(self, image, new_dimensions):
        # Cambiar el tamaño de la imagen
        print("Cambiar el tamaño de la imagen a:", new_dimensions)

class ImageSaver:
    def save_image(self, image, file_path):
        # Guardar la imagen en un archivo
        print("Guardar imagen en el archivo:", file_path)
