class Person:
    def __init__(self, firstname='Milaan', lastname='Parmar', age=96, country='England', city='London', gender = 'male'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.gender = gender
        self.skills = []
    
    def person_info(self):
        gender = "He" if self.gender == "male" else "she"
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)

class Student(Person):
    def __init__(self, firstname, lastname, age, country, city, gender):
        super().__init__(firstname, lastname, age, country, city, gender)

s1 = Student("Arthur", "Curry", 33, "England", "London", "male" )
s2 = Student('Emily', 'Carter', 28, 'England', 'Manchester', "female")
print(s1.person_info())
print(s2.person_info())
s1.add_skill('Python')
s1.add_skill('R')
s1.add_skill('Nextflow')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Software Development')
s2.add_skill('Data Analysis')
s2.add_skill('Pipeline development')
print(s2.skills)