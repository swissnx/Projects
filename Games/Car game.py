
class CarGame:
    def __init__(self):
        self.__command = ""
        self.__started = False

    def __start(self):
        if self.__started:
            return "Car is already started!"
        else:
            self.__started = True
            return "Car started...Ready to go!"
    
    def __stop(self):
        if not self.__started:
            return "Car is already stopped!"
        else:
            self.__started = False
            return "Car stopped"
    
    def __help(self):
        return "start - to start the car\nstop - to stop the car\nquit - to exit the game"
    
    def __run(self):
        while True:
            self.__command = input("\nCommand: ").lower()
            try:
                if self.__command == "start":
                    print(self.__start())
                elif self.__command == "stop":
                    print(self.__stop())
                elif self.__command == "help":
                    print(self.__help())
                elif self.__command == "quit":
                    break
                else:
                    print("Sorry, I don't understand that...")
            except Exception as e:
                print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    game = CarGame()
    game.run()
