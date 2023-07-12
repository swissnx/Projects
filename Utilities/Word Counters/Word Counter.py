
from os import strerror


class FileCounterTool:
    def __init__(self, file_name, chunk_size=65536):
        self.__file_name = file_name
        self.__chunk_size = chunk_size
    
    def __count_characters(self):
        cnt = 0
        chunk_size = 65536
        with open(self.__file_name, "rt") as s:
            while True:
                chunk = s.read(self.__chunk_size)
                if not chunk:
                    break
                cnt += len(chunk)
        return cnt

    def __count_lines(self):
        cnt = 0
        with open(self.__file_name, "rt") as s:
            for line in s:
                cnt += 1
        return cnt
    
    def __count_words(self):
        cnt = 0
        with open(self.__file_name, "rt") as s:
            for line in s:
                words = line.split()
                cnt += len(words)
        return cnt
    
    def run(self):
        while True:
            try:
                print("\nWhat information would you like to see?")
                print("\n1. Character count\n2. Line count\n3. Word count")
                print("4. All of the above\n0. Exit")
                choice = input("\nYour choice: ")

                if choice.isalpha():
                    print("Invalid input. Please enter integer.")
                
                else:
                    choice = int(choice)
                
                    if choice == 1 or choice == 4:
                        char_count = self.__count_characters()
                        print(f"\n\nCharacters in file: {char_count}")
                    
                    if choice == 2 or choice == 4:
                        line_count = self.__count_lines()
                        print(f"Lines in file: {line_count}")
                    
                    if choice == 3 or choice == 4:
                        word_count = self.__count_words()
                        print(f"Words in file: {word_count}")
                    
                    if choice == 0 or choice == "":
                        break
            
            except FileNotFoundError as e:
                print(f"\nFile not found: {e.filename}")

            except PermissionError as e:
                print(f"\nPermission denied: {e.filename}")

            except IOError as e:
                print(f"\nI/O error occurred: {strerror(e.errno)}")

            except ValueError as e:
                print(f"\nInvalid input: {e}")

            except Exception as e:
                print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")


if __name__ == "__main__":
    file_name = input("File Path: ")
    counter_tool = FileCounterTool(file_name)
    counter_tool.run()