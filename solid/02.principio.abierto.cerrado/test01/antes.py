class ImageFilter:
    def apply_filter(self, image, filter_type):
        if filter_type == 'grayscale':
            print("Aplicar filtro de escala de grises a la imagen")
        elif filter_type == 'sepia':
            print("Aplicar filtro sepia a la imagen")
        elif filter_type == 'blur':
            print("Aplicar filtro de desenfoque a la imagen")
        else:
            print("Tipo de filtro no reconocido")
