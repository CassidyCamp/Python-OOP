class Student :
    def __init__(self, name: str, age: int, grade: str):
        self.name = name
        self.age = age
        self.grade = grade
    
    
    def info(self):
        print(f"{self.name}, {self.age} yoshda, {self.grade}-sinf o‘quvchisi.") 
        
        
student1 = Student("Ali", 15, 9)
student1.info()