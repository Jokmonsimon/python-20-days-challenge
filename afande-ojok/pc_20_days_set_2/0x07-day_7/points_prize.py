# Working with if statement

points = int(input("Plese enter your Points: "))
prize = ["Wooden rabbit", "no prize", "Wafer-thin mint", "Penguin"]

if points <= 0:
    result = "Points can only take on positive integer values up to 200."
elif points <= 50:
    result = "Congratulations! You have won {} for {} points earned!".format(prize[0], points)
elif points <= 150:
    result = "Sorry! {} for {} points earned!. Please try again!".format(prize[1], points)
elif points <= 180:
    result = "Congratulations! You have won {} for {} points earned!".format(prize[2], points)
elif points <= 200:
    result = "Congratulations! You have won {} for {} points earned!".format(prize[3], points)
else:
    result = "Sorry! Prizes available for positive integer values up to 200!"

print(result)