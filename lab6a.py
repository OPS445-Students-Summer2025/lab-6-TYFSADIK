#!/usr/bin/env python3

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.grades = {}

    def addGrade(self, course, grade):
        self.grades[course] = grade

    def displayStudent(self):
        return f"Student Name: {self.name}\nStudent Number: {self.number}"

    def displayGPA(self):
        try:
            gpa = sum(self.grades.values()) / len(self.grades)
        except ZeroDivisionError:
            gpa = 0.0
        return f"GPA of student {self.name} is {gpa:.1f}"

    def displayCourses(self):
        return [course for course, grade in self.grades.items() if grade > 0.0]

if __name__ == "__main__":
    # Example usage
    s = Student("John", "12345")
    s.addGrade("ops445", 4.0)
    s.addGrade("ipc144", 3.5)
    print(s.displayStudent())
    print(s.displayCourses())
    print(s.displayGPA())
