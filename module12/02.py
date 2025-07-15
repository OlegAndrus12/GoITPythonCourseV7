# composition has relation

class Department:
    def __init__(self, name):
        self.name = name
        self.teachers = []  # Composition happens here

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    
    def get_department_details(self):
        details = f"Department: {self.name}\n"
        details += "Teachers:\n"
        for teacher in self.teachers:
            details += f"- {teacher.get_details()}\n"
        return details


# inheritance is relation

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    

class Teacher(Person):
    def __init__(self, field, age, name):
        self.field = field
        super().__init__(age, name)
