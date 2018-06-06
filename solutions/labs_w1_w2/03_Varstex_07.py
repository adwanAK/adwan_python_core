'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''

# initialize our variables from the instructions
current_pop = 380123456
birth_rate_in_sec = 1/6
death_rate_in_sec = 1/12
immigration_rate_in_sec = 1/40

# how many seconds in one year?
# CHALLENGE: import your solution from a previous exercise to use it here!
sec_per_year = 3600 * 24 * 365  # secs/hr * hrs/day * days/year

# calculate the population rates per year
births_per_year = birth_rate_in_sec * sec_per_year
deaths_per_year = death_rate_in_sec * sec_per_year
immigrations_per_year = immigration_rate_in_sec * sec_per_year

# calculate population development for the next three years
years = 3
while years > 0:
    # using the in-built function round() because there's only whole humans!
    current_pop += round(births_per_year + immigrations_per_year - deaths_per_year)
    print(current_pop)
    years -= 1

# NOTE: these results don't account for changing population rates.
