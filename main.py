# School Management System
# OOP + File Handling + Encapsulation

# ---------------- Course Class ----------------
class Course:
    def __init__(self, course_name):
        self.course_name = course_name


# ---------------- Student Class ----------------
class Student:
    def __init__(self, name, roll, password):
        self.name = name
        self.roll = roll
        self.enrolled_courses = []
        self.__password = password   # private variable (Encapsulation)

    def enroll_course(self, course):
        self.enrolled_courses.append(course.course_name)

    # Getter method (password access)
    def get_password(self):
        return self.__password


# ---------------- File Handling Functions ----------------
FILE_NAME = "students.txt"

def save_student(student):
    with open(FILE_NAME, "a") as file:   # append mode
        courses = ", ".join(student.enrolled_courses)
        file.write(
            f"Name: {student.name}, Roll: {student.roll}, Courses: {courses}\n"
        )

def show_all_students():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n----- All Students -----")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No student data found!")
# ---------------- Main Program ----------------
def main():
    while True:
        print("\n1. Enroll Student")
        print("2. Show All Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            roll = input("Enter roll number: ")
            password = input("Set password: ")

            student = Student(name, roll, password)

            n = int(input("How many courses? "))
            for i in range(n):
                cname = input(f"Enter course {i+1} name: ")
                course = Course(cname)
                student.enroll_course(course)

            save_student(student)
            print("Student enrolled & saved successfully!")

        elif choice == "2":
            show_all_students()

        elif choice == "3":
            print("Program closed.")
            break

        else:
            print("Invalid choice!")


# ---------------- Program Start ----------------
main()
