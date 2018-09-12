# '''
# If a runner runs 12 kilometers in 30 minutes and 30 seconds.
# What is his/her average speed in miles per hour. (Tip: 1 mile = 1.6 km)

# '''
print("average speed in km per second: ")
km_per_second=12/((30*60)+30)
print(km_per_second)

print("\naverage speed in km per hour: ")
km_per_hour=(km_per_second*60*60)
print(km_per_hour)

print("\naverage speed in mile per hour: ")
km_to_mile=km_per_hour/1.6
print(km_to_mile)
