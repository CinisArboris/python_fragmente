class ImageProcessorDespues:
    def __init__(self):
        print("Inicializando ImageProcessorDespues")

    def process_image(self, image):
        print("Procesando imagen en ImageProcessorDespues")


class ImageEditorDespues:
    def __init__(self, image):
        self.image = image
        print("Inicializando ImageEditorDespues")

    def process(self, processor):
        print("Ejecutando proceso en ImageEditorDespues")
        processor.process_image(self.image)
