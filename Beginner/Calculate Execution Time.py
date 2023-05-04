
from time import time

start = time()

# 
# function here to measure the execution timing
# 

end = time()

execution_time = end - start
print(f"\nExecution Time:\n{execution_time / 60:.2f} min\n{execution_time:.2f} s\n{execution_time * 1000:.2f} ms\n")



# try this function:
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
