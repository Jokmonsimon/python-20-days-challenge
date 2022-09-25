class Welcome:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('Welcome', self.name)

greet = Welcome(input("What is your name: "))
greet.say_hello()