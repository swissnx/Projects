
def even_num(num):
  print(num)
  if num % 2 != 0:
    print("\nPlease enter an even number\n")
  elif num == 2:
    return num
  else:
    return even_num(num - 2)


print("\nList of All Even Numbers until our given number\n")
even_num(int(input("Enter here: ")))
print("\nExecuted successfully!")

# Output: 10, 8, 6, 4, 2.
