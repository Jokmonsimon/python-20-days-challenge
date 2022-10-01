# Working with if statement

points = int(input("Plese enter your Points: "))
prize = ["Wooden rabbit", "no prize", "Wafer-thin mint", "Penguin"]

if points <= 0:
    print("Points can only take on positive integer values up to 200.")
elif points <= 50:
    print("Congratulations! You have won {} for {} points earned!".format(prize[0], points))
elif points <= 150:
    print("Sorry! {} for {} points earned!. Please try again!".format(prize[1], points))
elif points <= 180:
    print("Congratulations! You have won {} for {} points earned!".format(prize[2], points))
elif points <= 200:
    print("Congratulations! You have won {} for {} points earned!".format(prize[3], points))
else:
    print("Sorry! Prizes available for positive integer values up to 200!")
