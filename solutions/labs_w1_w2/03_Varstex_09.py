'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''

# welcome message
print("""
-------------------------------------------------
               TRIP COST CALCULATOR
-------------------------------------------------
""")

# get user input
miles_to_drive = float(input("How many miles do you need to drive? "))
mpg_of_car = float(input("How many MPG can your car reach? "))
price_per_gallon = float(input("How much does 1 gallon of fuel cost? "))

# calculate cost of trip
cost_for_trip = miles_to_drive / mpg_of_car * price_per_gallon
print(f"\nYour trip will cost you ${round(cost_for_trip, 2)}")

# TIP: check out the "String Formatting" section in Python Intermediate
#      for more about using f-strings :)
