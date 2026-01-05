class Student:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

# Δημιουργία Αντικειμένου
student1 = Student("Γιώργος", "12345")
student1.add_grade(18)
student1.add_grade(20)

print(f"Ο μέσος όρος του {student1.name} είναι: {student1.get_average()}")