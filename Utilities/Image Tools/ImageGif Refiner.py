
from PIL import Image, ImageFilter, ImageSequence


class ImageGifRefiner:
    def __init__(self):
        self.__image = input("Image: ")
        self.__gif = input("Gif: ")

    def __sharpen_image(self):
        try:
            img = Image.open(self.__image)
            img = img.convert('RGB')
            sharpened_img = img.filter(ImageFilter.SHARPEN)
            return sharpened_img
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred while sharpening the image: \u001b[38;5;200m{e}\u001b[0m")
            return None

    def __sharpen_gif(self):
        try:
            img = Image.open(self.__gif)
            frames = [frame.convert('RGB').filter(ImageFilter.SHARPEN) for frame in ImageSequence.Iterator(img)]
            frames[0].save('sharpened.gif', save_all=True, append_images=frames[1:])
            return 'sharpened.gif'
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred while sharpening the gif: \u001b[38;5;200m{e}\u001b[0m")
            return None

    def set_image(self, image):
        self.__image = image

    def set_gif(self, gif):
        self.__gif = gif

    def run(self):
        while True:
            if self.__image != "":
                sharpened_image = self.__sharpen_image()
                if sharpened_image is not None:
                    print(sharpened_image)
            if self.__gif != "":
                sharpened_gif = self.__sharpen_gif()
                if sharpened_gif is not None:
                    print(sharpened_gif)
            choice = input("Do you want to continue? (y/n): ")
            if choice.lower() == 'n' or choice == "":
                break
            else:
                self.set_image(input("Image: "))
                self.set_gif(input("Gif: "))


if __name__ == "__main__":
    refiner = ImageGifRefiner()
    refiner.run()
