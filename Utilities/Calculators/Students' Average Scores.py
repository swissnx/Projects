
# a program to evaluate the students' average scores;
# the program should ask for the student's name, followed by her/his single score;

class SchoolClass:
    def __init__(self):
        self.__school_class = {}

    def __add_student(self, name, score):
        if name in self.__school_class:
            self.__school_class[name] += (score,)
        else:
            self.__school_class[name] = (score,)

    def __calculate_averages(self):
        for name in sorted(self.__school_class.keys()):
            adding = 0
            counter = 0
            for score in self.__school_class[name]:
                adding += score
                counter += 1
            print(f"{name}: {adding / counter:.2f}")

    def __run(self):
        try:
            print("\nFind Students' average scores")
            while True:
                name = input("\nName: ")
                if name == '':
                    break

                while True:
                    try:
                        score = int(input("Score (0-10): "))
                        if score not in range(0, 11):
                            raise ValueError("Score must be between 0-10")
                        
                    except ValueError as ve:
                        return f"\n\033[3m!✶ Error: \033[38;5;200m{ve}\033[0m"
                    
                    else:
                        break
                    
                self.__add_student(name, score)
            self.__calculate_averages()
            
        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.run()
