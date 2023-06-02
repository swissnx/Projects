
# Program to find student with highest GPA

import string

class Student:
    def __init__(self, name=None, hours=None, qpoints=None):
        self.__name = name
        self.__hours = float(hours) if hours else None
        self.__qpoints = float(qpoints) if qpoints else None

    def __getName(self):
        return self.__name

    def __getHours(self):
        return self.__hours

    def __getQPoints(self):
        return self.__qpoints

    def __gpa(self):
        return self.__qpoints/self.__hours

    def __print_info(self):
        print("The best student is:", self.__getName())
        print("hours:", self.__getHours())
        print("GPA:", self.gpa())

    def run(self):
        return self.__run()

    def __run(self):
        filename = input("Enter name the grade file: ")
        try:
            infile = open(filename, 'r')
            best = self.makeStudent(infile.readline())
            for line in infile:
                s = self.makeStudent(line)
                if s.gpa() > best.gpa():
                    best = s
            infile.close()
            best.print_info()
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    @staticmethod
    def makeStudent(infoStr):
        name, hours, qpoints = string.split(infoStr,"\t")
        return Student(name, hours, qpoints)


if __name__ == "__main__":
    student = Student()
    student.run()
