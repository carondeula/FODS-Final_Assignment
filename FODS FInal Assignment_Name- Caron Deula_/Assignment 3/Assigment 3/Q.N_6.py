class Student:
    def __init__(self, student_id, name, address, admission_year, level, section):
        self.student_id = student_id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section

    def display(self):
        print("\nStudent Information:")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

# Example usage
s = Student("S1", "Caron", "Lalitput", 2024, "Level 4", "C")
s.display()
