
from time import time


class ExecutionTime:
    def __init__(self):
        self.__start = 0
        self.__end = 0
        self.__execution_time = 0
        self.__minutes = 0
        self.__milliseconds = 0

    def __measure_exec_time(self, function, *args):
        self.__start = time()
        function(*args)
        self.__end = time()
        self.__execution_time = self.__end - self.__start
        self.__minutes = self.__execution_time / 60
        self.__milliseconds = self.__execution_time * 1000
        self.__print_exec_time()

    def __print_exec_time(self):
        if self.__milliseconds >= 1000:
            print(f"\nExecution Time:\n{self.__minutes:.2f} min\n{self.__execution_time:.2f} s\n")
        else:
            print(f"\nExecution Time:\n{self.__minutes:.2f} min\n{self.__execution_time:.2f} s\n{self.__milliseconds:.2f} ms\n")

    def __run(self):
        try:
            file_path = input("Enter the file path: ")
            with open(file_path, 'r') as file:
                script = file.read()
            self.__measure_exec_time(exec, script)
        except Exception as e:
            print(f"\n\u001b[3m** An error occurred: \u001b[38;5;200m{e}\u001b[0m")

    def measure_exec_time(self, function, *args):
        self.__measure_exec_time(function, *args)
        self.__print_exec_time()

    def run(self):
        return self.__run()


if __name__ == "__main__":
    exec_time = ExecutionTime()
    exec_time.run()
