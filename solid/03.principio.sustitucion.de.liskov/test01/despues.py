class ImageDespues:
    def load(self, file_path):
        print(f"Cargar imagen desde el archivo: {file_path}")

    def save(self, file_path):
        print(f"Guardar imagen en el archivo: {file_path}")

    def animate(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")

class AnimatedImageDespues(ImageDespues):
    def load(self, file_path):
        print(f"Cargar imagen animada desde el archivo: {file_path}")

    def save(self, file_path):
        print(f"Guardar imagen animada en el archivo: {file_path}")

    def animate(self):
        print("Animar imagen")
