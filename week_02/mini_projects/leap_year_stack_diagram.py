'''
--------------------------------------------------------
                LEAP YEAR + STACK DIAGRAM
--------------------------------------------------------

Construct a function according to the following description,
then draw a stack diagram of an execution with ‘2000’ as input.

-- DESCRIPTION --
We add a Leap Day on February 29, almost every four years.
The leap day is an extra, or intercalary day and we add it to the
shortest month of the year, February. In the Gregorian calendar
three criteria must be taken into account to identify leap years:

- The year can be evenly divided by 4, is a leap year, unless:
  - The year can be evenly divided by 100, it is NOT a leap year, unless:
    - The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are
leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

-- TASK --
You are given the year, and you have to write a function to check
if the year is leap or not.

Input Format:
Read y, the year that needs to be checked.

Constraints:
1900 <= y <= 10**5

Output Format:
Your function must return a boolean value (True/False)

-- STACK DIAGRAM --
You can use the viz mode here:
http://www.pythontutor.com/visualize.html#mode=edit
for better visual understanding and support in creating the stack diagram.

'''

# Function only starts after the while loop calls it
def check_leap_year(input_year):
    leap_year = False
    if(input_year % 4 == 0):
        leap_year = True
        if(input_year % 100 == 0):
            if(input_year % 400 == 0):
                leap_year = True
            else:
                leap_year = False
    return(leap_year)


input_year = input("Please input year y and 1900 <= y <= 10**5 :")

# Program starts at this loop
# This while really is not necessary, but I wanted an interactive input prompt with user:
while(str(input_year) != "END"):
    input_year = int(input_year)

    if(input_year < 1900 or input_year > 10**5):
        print("To terminate program type END 'Upper case'")
        input_year = int(input("Wrong Input!!! Please input year y and 1900 <= y <= 10**5 :"))

    else:
        print("Is the year", input_year, "leap year?===>", check_leap_year(input_year), "<======")
        print("\nTo terminate program type END 'Upper case")
        input_year = input("Please input year y and 1900 <= y <= 10**5 :")


print("Thank you! Program terminated")
