"""
1 hour of bro code
string
type casting
integers
varibles
user input
if elif else statements
loops
"""

# array of characters
my_string = "d35523434"

# can only use strings with strings
# example of syntax error: print(my_string[0] + 3)


# type casting
# int() - converts to integer
# float() - converts to float
# str() - converts to string
# bool() - converts to boolean  True 1 False 0

my_charater = "3"
my_integer = 6
#print(int(my_charater) + my_integer)

# integers
divide = 5 / 2
divide_int = 5 // 2

print(divide)
print(divide_int)
print("kill your self terminal")

#cost of apples and oranges
apples = 5
oranges = 10


if apples < oranges:
    print("im going to buy the apples beacuse they are cheaper")
elif apples == oranges:
    print("im going to buy both")
else:
    print("im going to buy the oranges beacuse they are cheaper")

#CONSTANTS - variables that are never meant to change
YOMAMA = 10
yo_moma = range(4,12,2)
the_list = list(yo_moma)
print(the_list)

for i in the_list:
    print(i)