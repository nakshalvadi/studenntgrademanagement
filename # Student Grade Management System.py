# Student Grade Management System

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        grades_str = ", ".join([f"{subject}: {grade}" for subject, grade in self.grades.items()])
        return f"ID: {self.student_id}, Name: {self.name}, Grades: {grades_str}, Average: {self.calculate_average():.2f}"

class GradeManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} added successfully!")
        else:
            print("Student with this ID already exists.")

    def add_grade(self, student_id, subject, grade):
        if student_id in self.students:
            student = self.students[student_id]
            student.add_grade(subject, grade)
            print(f"Grade for {subject} added to {student.name}.")
        else:
            print("Student not found.")

    def display_student_info(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(student)
        else:
            print("Student not found.")

    def display_all_students(self):
        if self.students:
            for student in self.students.values():
                print(student)
        else:
            print("No students in the system.")

# Main Program
def main():
    system = GradeManagementSystem()

    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Info")
        print("4. View All Students")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            system.add_student(student_id, name)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            subject = input("Enter subject name: ")
            grade = float(input("Enter grade: "))
            system.add_grade(student_id, subject, grade)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            system.display_student_info(student_id)
        elif choice == "4":
            system.display_all_students()
        elif choice == "5":
            print("Exiting system...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
