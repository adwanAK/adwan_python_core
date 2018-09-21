'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''


nums = range(1, 1000000)

gen = (n for n in nums)

for item in gen:
    print_string = f"{item}/1111"
    print(f"{print_string} = {item//1111}")

# I see that we get the same number in a
