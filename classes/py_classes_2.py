from datetime import datetime


class Person:
    def __init__(self, name, email, dob, gender, favorite_teams):
        self.name = name
        self.email = email
        self.dob = dob
        self.gender = gender
        self.teams = favorite_teams

    def print_details(self):
        print(self.name)
        print(self.email)
        print(self.gender)
        print("----Teams----")
        for team in self.teams:
            print(team)
        print("--------------------")
        # 07-04-2000

    def calculate_age(self):
        today = datetime.now()
        dob = datetime.strptime(self.dob, "%d-%m-%Y")
        delta = today - dob
        print(delta.days // 365, "years old.")


p1 = Person("Calton", "korir@yme.com", "07-04-2000", "Male", ["Manchester", "Ajax", "Brussels"])
p1.print_details()
p1.calculate_age()
