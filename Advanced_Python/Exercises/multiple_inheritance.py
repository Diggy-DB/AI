
class Teacher:
    def __init__(self):
        self.major = "teacher"
    def skills(self):
        return "teaching, education"
class Youtuber:
    def __init__(self):
        self.major = "youtuber"
    def skills(self):
        return "video editing, narrative"
class Student(Teacher):
    def skills(self):
        print("He is a student learning in " + Teacher.major() + ", and my skills are " + Teacher.skills(self))

s = Student()
s.skills()