
import base64


class ImageEncoder:
    def __init__(self):
        self.__image = None
        self.__encoded_image = None

    def __load_image(self, image_path):
        try:
            if image_path.endswith('.svg'):
                with open(image_path, 'r') as f:
                    self.__image = f.read()
            else:
                with open(image_path, 'rb') as f:
                    self.__image = f.read()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def __encode_image(self):
        if self.__image is not None:
            if isinstance(self.__image, str):
                self.__encoded_image = base64.b64encode(self.__image.encode('utf-8')).decode('utf-8')
            else:
                self.__encoded_image = base64.b64encode(self.__image).decode('utf-8')

    def __run(self):
        image_path = input('Image path: ')
        self.__load_image(image_path)
        self.__encode_image()
        if self.__encoded_image is not None:
            print(f'\nEncoded image: {self.__encoded_image}')

    def run(self):
        self.__run()


if __name__ == "__main__":
    encoder = ImageEncoder()
    encoder.run()
