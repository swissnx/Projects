
class NumberPrinter:
    def __init__(self):
        self.__digits = ['1111110',
                         '0110000',
                         '1101101',
                         '1111001',
                         '0110011',
                         '1011011',
                         '1011111',
                         '1110000',
                         '1111111',
                         '1111011']
        self.__num = input("Display Number: ")
        self.__width = int(input("Width (def-7): ") or 7)
        self.__height = int(input("Height (default-5): ") or 5)
        self.__space = int(input("Space between numbers (default-1): ") or 1)
        self.__symbol = input("Enter the symbol to use for display (default is #): ") or '#'
        self.__color = input("Color (red, green, yellow, blue, magenta, cyan, white): ")

    def __print_number(self):
        num = self.__num
        digs = str(num)
        lines = ["" for _ in range(self.__height)]

        for d in digs:
            segs = [[" " for _ in range(self.__width)] for _ in range(self.__height)]
            ptrn = self.__digits[ord(d) - ord('0')]

            if ptrn[0] == '1':
                for i in range(self.__width):
                    segs[0][i] = self.__symbol

            if ptrn[1] == '1':
                for i in range(self.__height // 2):
                    segs[i][self.__width - 1] = self.__symbol

            if ptrn[2] == '1':
                for i in range(self.__height // 2, self.__height):
                    segs[i][self.__width - 1] = self.__symbol

            if ptrn[3] == '1':
                for i in range(self.__width):
                    segs[self.__height - 1][i] = self.__symbol

            if ptrn[4] == '1':
                for i in range(self.__height // 2, self.__height):
                    segs[i][0] = self.__symbol

            if ptrn[5] == '1':
                for i in range(self.__height // 2):
                    segs[i][0] = self.__symbol

            if ptrn[6] == '1':
                for i in range(self.__width):
                    segs[self.__height // 2][i] = self.__symbol

            for lin in range(self.__height):
                lines[lin] += ''.join(segs[lin]) + " " * self.__space

        return lines

    def __run(self):
        try:
            num = int(self.__num)
            lines = self. __print_number()
            colors = {"red": "\033[31m",
                      "green": "\033[32m",
                      "yellow": "\033[33m",
                      "blue": "\033[34m",
                      "magenta": "\033[35m",
                      "cyan": "\033[36m",
                      "white": "\033[37m"
                      }
            color_code = colors.get(self.__color.lower(), "\033[37m")
            reset_code = "\033[0m"

            for line in lines:
                print(color_code + line + reset_code)

        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

        except Exception as e:
            return f"\n\033[3m!✶ Error: \033[38;5;200m{e}\033[0m"

    def run(self):
        return self. __run()


if __name__ == "__main__":
    printer = NumberPrinter()
    printer.run()




# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ DOCUMENTATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #

digits = ['1111110',
		  '0110000',
		  '1101101',
		  '1111001',
		  '0110011',
		  '1011011',
		  '1011111',
		  '1110000',
		  '1111111',
		  '1111011',]


def print_number(num):
	global digits
	digs = str(num)
	lines = [ "" for lin in range(5) ]
	for d in digs:
		segs = [ [" "," "," "," "] for lin in range(5) ]
		ptrn = digits[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)


print_number(int(input("Enter the number you wish to display: ")))



# ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ EXPLANATION ✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶✶ #

"""   Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.
Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:

  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

Note: the number 8 shows all the LED lights on.
Your code has to display any non-negative integer number entered by the user.
Tip: using a list containing patterns of all ten digits may be very helpful.    """




digits = [ '1111110',  	# 0            # decimals converted to binary
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3       # The digits list contains the patterns for each digit, represented as a string of seven '1's and '0's.
	   '0110011',	# 4       # Each '1' indicates that a segment of the seven-segment display should be lit up, and each '0' indicates that the segment should be turned off.
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]


def print_number(num):                  # This line starts the definition of the function print_number which takes a single argument num and is used to print the given number in a 7-segment display format.
	global digits                       # This line makes the global digits list available within the print_number function.
	digs = str(num)                     # This line converts the number num to a string and stores it in a variable digs.
	lines = [ "" for lin in range(5) ]       # ['', '', '', '', '']    /   This line creates a list of 5 empty strings which are used to store the 5 lines of the 7-segment display for each digit.
	for d in digs:                           # This line starts a for loop that will loop through each character in the string digs.
		segs = [ [" "," "," "," "] for lin in range(5) ]       # [' ',' ',' '], [' ',' ',' '], [' ',' ',' '], [' ',' ',' '], [' ',' ',' ']   /   This line creates a 2D list segs of 5 rows and 3 columns. Each row represents a line of the 7-segment display and each column represents a segment. The elements of segs are initially set to spaces ' '.
		ptrn = digits[ord(d) - ord('0')]                  # This line sets the variable 'ptrn' to the binary representation of the current digit by finding the index of the digit in the digits list. The index is calculated by subtracting the ASCII value of '0' from the ASCII value of the current digit.
		if ptrn[0] == '1':    # pattern                   # This line checks if the first segment of the current digit is lit. If it is, the corresponding segments in segs are set to '#' to represent the lit segment.
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):                             # This line starts a for loop that will loop through the 5 lines of the 7-segment display.
			lines[lin] += ''.join(segs[lin]) + ' '       # This line concatenates the segments of the current line in segs into a single string and appends it to the corresponding line in lines. A space is also appended after each line.
	for lin in lines:                                  # This line starts a for loop that will loop through the 5 lines in lines and print each line.
		print(lin)     # In this context, lin is a variable that holds the value of each line from the list lines in each iteration of the for loop. The for loop is looping through each line of lines and printing each line.


print_number(int(input("Enter the number you wish to display: ")))


#-----------------------------------------------------------------------------------------------------------------------------
# When you assign digs = str(5), you are converting the integer 5 to a string "5", and storing it in the variable digs.
#    Since digs is now a string, you can iterate through its characters using a for loop, as shown here:

digs = str(5)
for d in digs:
    print(d)     # 5



#-----------------------------------------------------------------------------------------------------------------------------
# Here's an example of how the code ptrn = digits[ord(d) - ord('0')] works:

digits = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001']   # 0000 = 0, 0001 = 1, etc.
d = '7'
ptrn = digits[ord(d) - ord('0')]
print(ptrn)                         # 0111  (which is 7)

# In this example, digits is a list of binary representations of the digits 0 to 9. d is a string that contains the digit '7'.
#    The line ptrn = digits[ord(d) - ord('0')] sets the value of ptrn to the binary representation of the digit in d.

# The calculation ord(d) - ord('0') determines the index of the digit in the digits list. ord is a built-in function in Python
#    that returns the ASCII value of a character. In this case, ord(d) returns the ASCII value of the digit in d and ord('0')
#    returns the ASCII value of the character '0'. By subtracting ord('0') from ord(d), we get the difference between the ASCII values,
#    which corresponds to the index of the digit in the digits list. For example, the ASCII value of '7' is 55, and the ASCII value of '0' is 48,
#    so 55 - 48 = 7, which is the index of the digit '7' in the digits list.

# Finally, ptrn is set to the value of the binary representation of the digit, which is the item in the digits list at the calculated index.
#     In this example, ptrn is set to '0111', which is the binary representation of the digit '7'.



#-----------------------------------------------------------------------------------------------------------------------------
# example:
if ptrn[0] == '1':
    segs[0][0] = segs[0][1] = segs[0][2] = '#'
# This line checks if the first character (index 0) of the binary string ptrn is equal to '1'.
# If it is, then the first three columns (index 0, 1, and 2) of the first row (index 0) of the segs list are set to '#'.

ptrn = '1000110'
segs = [ [' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' '] ]

# after execution:
ptrn = '1000110'
segs = [ ['#', '#', '#'],
         [' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' '] ]
# So the first row of segs has been updated to contain '#' in the first three columns.
# The following if statements work similarly, checking a different index of ptrn and updating different rows and columns of segs based on the value of ptrn.



#-----------------------------------------------------------------------------------------------------------------------------
# how ptrn gets 8 for example, how does it print it. Let's say the input number is 8
digs = str(8)

# The digits list contains the binary representation of each digit in a 7-segment display
# For digit 8, the binary representation is '1111111'
ptrn = digits[ord(d) - ord('0')]
print(ptrn) # Output: '1111111'

# The if statements check each bit in the binary representation of the digit
# If a particular bit is 1, then the corresponding segments in the 7-segment display are lit up
# For the digit 8, all 7 bits are 1, so all 7 segments are lit up
if ptrn[0] == '1':
    segs[0][0] = segs[0][1] = segs[0][2] = '#'
if ptrn[1] == '1':
    segs[0][2] = segs[1][2] = segs[2][2] = '#'
if ptrn[2] == '1':
    segs[2][2] = segs[3][2] = segs[4][2] = '#'
if ptrn[3] == '1':
    segs[4][0] = segs[4][1] = segs[4][2] = '#'
if ptrn[4] == '1':
    segs[2][0] = segs[3][0] = segs[4][0] = '#'
if ptrn[5] == '1':
    segs[0][0] = segs[1][0] = segs[2][0] = '#'
if ptrn[6] == '1':
    segs[2][0] = segs[2][1] = segs[2][2] = '#'

# The lit up segments are represented by the character '#'
# The final output is a 5x3 matrix representation of the 7-segment display for the digit 8
# Each row in the matrix represents a different segment in the display



#-----------------------------------------------------------------------------------------------------------------------------
# so what does this line do then:
for lin in range(5):                            
	lines[lin] += ''.join(segs[lin]) + ' '
# The line for lin in range(5): is a for loop that runs 5 times, once for each line of the seven segment display.
# The variable lin is used as an index to access the elements in the list lines.

# The line lines[lin] += ''.join(segs[lin]) + ' ' is concatenating (adding) the current line of the seven segment display
# to the corresponding line in the lines list. segs[lin] is a list of 3 characters representing a single line of the seven segment display,
# which is joined together into a string using ''.join(segs[lin]). Finally, a space character is added to the end of the string using + ' ',
# and the result is concatenated to the end of the corresponding line in the lines list using +=.
