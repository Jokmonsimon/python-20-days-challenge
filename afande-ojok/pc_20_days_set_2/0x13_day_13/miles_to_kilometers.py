# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	return miles * 1.6  # approximately 1.6 km in 1 mile

my_trip_miles = convert_distance(55)

# 2) Convert my_trip_miles to kilometers by calling the function above
convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_miles))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_miles * 2))

def sum(x, y):
	return (x+y)
print(sum(sum(1, 2), sum(3, 4)))

print((10>=5*2) and (10 <= 5*2))