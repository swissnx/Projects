
def pyramid():
    blocks = int(input("Enter the number of blocks: "))
  
    height = 0
    in_layer = 1               # represents the number of blocks in the current layer. ie. if there is one block, it means there is 1 layer.
    while in_layer <= blocks:
        height += 1
        blocks -= in_layer     # here, total blocks - blocks in the current layer
        in_layer += 1          # for example. user entered 6. 1st layer 1 block (6-1), 2nd layer 2 block (5-2), 3rd layer 3 blocks (3-3)
    return height              # here, 6 = total blocks, 6-1 = 5 left of total blocks and so it goes on.

result = pyramid()
print("The height of the Pyramid:", result)
