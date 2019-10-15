class SchoolMember:

    # 代表任何学校里的成员。'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        # 告诉我有关我的细节。'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):

    # definition Teacher
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Initialized Teacher...... {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Salary is :{}".format(self.salary))


class Student(SchoolMember):
    # definition student
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("Initialized Student......{}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks is : {}'.format(self.marks))


t = Teacher("James", 20, 20000)
s = Student('Dior', 6, 100)

print()

members = [t, s]
for i in members:
    i.tell()
