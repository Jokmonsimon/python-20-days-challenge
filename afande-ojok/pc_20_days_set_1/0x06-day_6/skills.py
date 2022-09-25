class Developer(object):
    def __init__(self, skills):
        self.skills = skills

    def __add__(self, other):
        skills = self.skills + other.skills
        return Developer(skills)

    def __str__(self):
        return "Skills"
    # __str__(), __add__() - Function call

A = Developer('NodeJS')
B = Developer('Python')

print(A + B)

