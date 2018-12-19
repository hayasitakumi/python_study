from datetime import date
 
class Person:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
 
    def get_age(self):
        today = date.today()
        if (self.date_of_birth.month, self.date_of_birth.day) < (today.month, today.day):
            return today.year - self.date_of_birth.year
        else:
            return today.year - self.date_of_birth.year - 1
 
    def greet(self):
        return 'Hello, I am {} {}.'.format(self.first_name, self.last_name)
 
class Student(Person):
    def __init__(self, first_name, last_name, date_of_birth, major):
        super().__init__(first_name, last_name, date_of_birth)
        self.major = major
 
    def greet(self):
        return 'Hello, I am {} {} studying {}.'.format(self.first_name, self.last_name, self.major)

# if __name__ == "__main__":
#   tom = Person('Tom', 'Anderson', date(1980, 10, 10))
#   print(tom.get_age())