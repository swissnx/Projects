
# The Collatz Conjecture is an unsolved mathematical problem. It states that for any positive integer n, if you take the following process:
#  • if n is even, divide it by 2
#  • if n is odd, multiply it by 3 and add 1
# then you will always reach 1. This script is a simulation of the conjecture for a given value of c0.

def collatz_conjecture():
    c0 = int(input("Enter c0: "))
    if c0 > 1:
        steps = 0
        while c0 != 1:
            if c0 % 2 != 0:
                cnew = c0 * 3 + 1
            else:
                cnew = c0 // 2
            print(f"-> {c0}")
            c0 = cnew
            steps += 1
        print(f"\nSteps = {steps}\n")
    else:
        print("Bad c0 value")


collatz_conjecture()
