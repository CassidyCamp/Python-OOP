class Student:
    def __init__(self, name: str, age: int, grade: str):
        self.name = name
        self.age = age
        self.grade = grade
        
        
student = Student("Daler", 17, "Full-stack")
student = Student("Samandar", 20, "Frontend")
student = Student("Ozod", 18, "Backend")