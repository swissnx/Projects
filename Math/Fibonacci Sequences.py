
class Fibonacci:
    def __init__(self):
        self.__start = None
        self.__end = None
    
    def __fibonacci(self, num):
        if num < 1:
            return None
        if num < 3:
            return 1

        elem1 = elem2 = 1
        total = 0
        for i in range(3, num + 1):
            total = elem1 + elem2
            elem1, elem2 = elem2, total
        return total

    def __run(self):
        try:
            self.__start = int(input("Start-point: "))
            self.__end = int(input("End-point: "))

            print()
            for num in range(self.__start, self.__end):
                print(f"{num} - {self.__fibonacci(num)}")
            print()

        except Exception as e:
            print(f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m")

    def run(self):
        return self.__run()


if __name__ == "__main__":
    fib = Fibonacci()
    fib.run()



# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● FUNCTION ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● #

import sys

sys.set_int_max_str_digits(0)

def fibonacci(num):
  if num < 1:
    return None
  if num < 3:
    return 1

  elem1 = elem2 = 1
  total = 0
  for i in range(3, num + 1):
    total = elem1 + elem2
    elem1, elem2 = elem2, total
  return total

start = int(input("Starting point: "))
end = int(input("Ending point:   "))
print()

for num in range(start, end):
  print(f"{num} - {fibonacci(num)}")
print()



# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● Iteration vs Recursion: Speedtest ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● #

import time

# Iteration
def fibonacci(idx):
	seq = [0,1]
	for i in range(idx):
		seq.append(seq[-1] + seq[-2])
	return seq[-2]

print("***** Iteration *****")
it = time.time()
num = fibonacci(int(input("\nEnter number: ")))
print(f"\nNumber is: {num}")
print(f"Speed: {str(time.time()-it)}\n\n")


# Recursion
def Fibonacci(idx):
	if idx <= 1:
		return idx
	else:
		return Fibonacci(idx-1) + Fibonacci(idx-2)

print("***** Recursion *****")
rec = time.time()
num = fibonacci(int(input("\nEnter number: ")))
print(f"\nNumber is: {num}")
print(f"Speed: {str(time.time()-rec)}\n\n")



# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● FUNCTION ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● #

# Comparing with: Recursion
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)   # this fib(n-1) is a sequence, means, sequence 8-1 = 7 which is 13, 8-2 = 6 which is 8, 8+13 = 21



# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● FUNCTION ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● #

class Fibonacci:
  def __init__(self, num):
    self.__n = num
    self.__i = 0
    self.__elem1 = self.__elem2 = 1

  def __iter__(self):
    return self

  def __next__(self):
    self.__i += 1
    if self.__i > self.__n:
      raise StopIteration
    if self.__i in [1, 2]:
      return 1
    result = self.__elem1 + self.__elem2
    self.__elem1, self.__elem2 = self.__elem2, result
    return result


class Class:
  def __init__(self, n):
    self.__iter = Fibonacci(n)

  def __iter__(self):
    return self.__iter

inpt = int(input("Enter number: "))
user = Class(inpt)
print()
for i in user:
  print(i)



# Class iteration explained: run the code on terminal
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)



# ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● GENERATOR ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●● #

def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)
