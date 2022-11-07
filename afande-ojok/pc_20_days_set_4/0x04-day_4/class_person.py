class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "Hi, my name is " FOLLOWED BY THE NAME OF THE Person
        return "Hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Afande Ojok")
# Call the greeting method
print(some_person.greeting())