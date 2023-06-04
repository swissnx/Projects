
# sorting the numbers: what happens inside the max() function

my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)



# initial code for better understanding:
my_list = [8, 10, 6, 2, 4]  # list to sort

for i in range(len(my_list) - 1):  # we need (5 - 1) comparisons
    if my_list[i] > my_list[i + 1]:  # compare adjacent elements
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # If we end up here, we have to swap the elements.




# this: read the next program comment to understand this
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

# perfect functional program > suggested to insert in def > class: this is in core of what happens above ^^
def list_nums_sorter():
  my_list = []
  swapped = True
  num = int(input("Number of elements to sort: "))
  
  for i in range(num):
      val = float(input("Enter an element: "))
      my_list.append(val)
  
  while swapped:
      swapped = False
      for i in range(len(my_list) - 1):
          if my_list[i] > my_list[i + 1]:
              swapped = True
              my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
  
  print("\nSorted:")
  print(my_list)

list_nums_sorter()

