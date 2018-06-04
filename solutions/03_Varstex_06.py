'''
If a runner runs 12 kilometers in 30 minutes and 30 seconds.
What is his/her average speed in miles per hour. (Tip: 1 mile = 1.6 km)

'''

# set up variables
distance_in_km = 12
runtime_in_sec = 30 * 60 + 30

# convert km to miles
def km_to_miles(km):
    miles = km * 0.6
    return miles

distance_in_miles = km_to_miles(distance_in_km)
#print(distance_in_miles)

# get part of hour
seconds_per_hour = 60 * 60  # 60 secs in 1 minute, 60 mins in 1 hour
runtimes_per_hour = seconds_per_hour / runtime_in_sec
#print(runtimes_per_hour)

# calculate miles/hr
miles_per_hour = distance_in_miles * runtimes_per_hour
print(miles_per_hour)
