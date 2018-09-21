'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

# remember: range() also creates a generator object (try printing it!)
nums = range(1, 1000000)

gen = (n for n in nums if n%1111 == 0)


print("Below print of items that are divisible by 1111 only")
for index, item in enumerate(gen):
    print_string = f"{item}/1111"
    print(f"{print_string} = {item/1111}") #Print number and divison result

# Outputs below
'''
Below print of items that are divisible by 1111 only
1111/1111 = 1.0
2222/1111 = 2.0
3333/1111 = 3.0
4444/1111 = 4.0
5555/1111 = 5.0
6666/1111 = 6.0
7777/1111 = 7.0
8888/1111 = 8.0
9999/1111 = 9.0
11110/1111 = 10.0
12221/1111 = 11.0
13332/1111 = 12.0
14443/1111 = 13.0
15554/1111 = 14.0
16665/1111 = 15.0
.
.
.
'''
