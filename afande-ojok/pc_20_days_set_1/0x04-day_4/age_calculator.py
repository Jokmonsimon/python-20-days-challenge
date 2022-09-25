# Age Calculator

# Defined a Python function for three user inputs: 
# y: year of birth 
# m: month of birth 
# d: date of birth
def age_calculator(y, m, d):
    # Import the datetime module in Python inside the function
    import datetime
    # Take today’s date by using the datetime.now() method of the datetime module
    today = datetime.datetime.now().date()
    # Create dob variable store date of birth input
    dob = datetime.date(y, m, d)
    # Subtract dob from today's date and divide by 365.25
    age = int((today - dob).days / 365.25)
    print("Wow! You are {} years old".format(age))
age_calculator(1993, 6, 3)