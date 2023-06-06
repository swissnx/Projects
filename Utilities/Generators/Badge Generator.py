
class BadgeGenerator:
    def __init__(self):
        self.__label = input("Label: ")
        self.__message = input("Message: ")
        self.__color = input("Badge color (def. green): ") or "green"
        self.__style = input("Badge style (def. flat): ") or "flat"
        self.__logo_color = input("Logo color (def. white): ")
        self.__label_color = input("ELabel color (def. black): ")
        self.__logo_width = input("Logo width (def. 40): ")
        self.__link_left = input("Left link URL: ")
        self.__link_right = input("Right link URL: ")
        self.__colorA = input("ColorA value (def. None): ")
        self.__colorB = input("ColorB value (def. None): ")
        self.__encoded_image_string = input("Encoded Image string: ")
    
    def __generate_badge_url(self):
        if self.__encoded_image_string:
            data_uri = f"data:image/svg+xml;base64,{self.__encoded_image_string}"
            badge_url = f"https://img.shields.io/badge/{self.__label}-{self.__message}-{self.__color}?style={self.__style}&logo={data_uri}&logoColor={self.__logo_color}&labelColor={self.__label_color}&logoWidth={self.__logo_width}&link={self.__link_left}&link={self.__link_right}"
        else:
            badge_url = f"https://img.shields.io/badge/{self.__label}-{self.__message}-{self.__color}?style={self.__style}&logoColor={self.__logo_color}&labelColor={self.__label_color}&logoWidth={self.__logo_width}&link={self.__link_left}&link={self.__link_right}"
        
        if self.__colorA:
            badge_url += f"&colorA={self.__colorA}"
        
        if self.__colorB:
            badge_url += f"&colorB={self.__colorB}"
        
        return badge_url
    
    def __run(self):
        badge_url = self.__generate_badge_url()
        print(f"\nBadge URL: {badge_url}")
    
    def run(self):
        self.__run()


if __name__ == "__main__":
    badge_generator = BadgeGenerator()
    badge_generator.run()
