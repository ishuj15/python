class College:
    def __init__(self, college_name,new_name, new_grades):
        self.college_name=college_name


class Student(College):
    def __init__(self, new_name, new_grades):
        super().__init__(self,college_name)
        self.name= new_name
        self.grades=new_grades

    def average_grade(self):
        return sum(self.grades)/len(self.grades)

    # static method
    @staticmethod
    def assigned_by():
       return "Assigned By me"


student_one=Student('Ishu', [100,100,100])
print(student_one.name)
print(student_one.average_grade())
print(Student.assigned_by())