
from time import time


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
