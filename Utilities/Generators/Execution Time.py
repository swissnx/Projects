
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

    def measure_exec_time(self, function, *args):
        self.__measure_exec_time(function, *args)
        self.__print_exec_time()

    def __run(self):
        try:
            file_path = input("File path: ")
            with open(file_path, 'r') as file:
                script = file.read()
            self.__measure_exec_time(exec, script)

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self.__run()


if __name__ == "__main__":
    exec_time = ExecutionTime()
    exec_time.run()



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #
# from time import time

# ✶✶✶✶✶✶✶✶✶ CONCURRENT MEASUREMENT ✶✶✶✶✶✶✶✶✶
start = time()
#
# function here to measure the execution timing
#
end = time()

execution_time = end - start
minutes = execution_time / 60
milliseconds = execution_time * 1000

if milliseconds >= 1000:
    print(f"\nExecution Time:\n{minutes:.2f} min\n{execution_time:.2f} s\n")
else:
    print(f"\nExecution Time:\n{minutes:.2f} min\n{execution_time:.2f} s\n{milliseconds:.2f} ms\n")



# ✶✶✶✶✶✶✶✶✶ IMMEDIATE MEASUREMENT ✶✶✶✶✶✶✶✶✶
def measure_exec_time(function, *args):
    start = time()

    function(*args)

    end = time()

    execution_time = end - start
    minutes = execution_time / 60
    milliseconds = execution_time * 1000

    if milliseconds >= 1000:
        print(f"\nExecution Time:\n{minutes:.2f} min\n{execution_time:.2f} s\n")
    else:
        print(f"\nExecution Time:\n{minutes:.2f} min\n{execution_time:.2f} s\n{milliseconds:.2f} ms\n")


# 
# function here
# 

# 
# argument here
# 

measure_exec_time(function, argument)


#●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●

# Test_1
# apply to "concurrent" measurement
def create_acronym(text: str) -> str:
    words = text.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym


try:
    text = input("Enter here: ")
    acronym = create_acronym(text)
    print(f"\n'{text}' acronym: {acronym}")

except Exception as e:
    print(f"Problem is: {e}")


#××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××

# Test_2
# insert above "immediate" function here
text = "Hello, welcome to Python world!"

measure_exec_time(print, text)  # works this way. takes print as argument, and send it print() function


#××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××

# Test_3
# insert above "immediate" function here
def create_acronym(text: str) -> str:
    words = text.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym


try:
    text = input("Enter here: ")
    acronym = create_acronym(text)
    print(f"\n'{text}' acronym: {acronym}")

except Exception as e:
    print(f"Problem is: {e}")


measure_exec_time(create_acronym, text)
