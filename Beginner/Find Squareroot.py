
import math
import time


def squareroot():

  while True:
    num = input("Sqrt Number: ")
    if num == "":
      print("\nFinished. Byeee\n")
      break
      
    num = float(num)
    sqroot = math.sqrt(num)
    time.sleep(0.5)
    print(f"\n-> {sqroot}\n")


squareroot()
