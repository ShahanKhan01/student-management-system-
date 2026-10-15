
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average():.2f}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)



    def create_student(self):
        name = input("Enter student name: ").strip()

        try:
            roll_no = int(input("Enter roll number: "))
        except ValueError:
            print("Invalid roll number. Please enter a whole number.")
            return

        # Check whether the roll number already exists
        for student in self.students:
            if student.roll_no == roll_no:
                print("A student with this roll number already exists.")
                return


        marks = []

        for i in range(3):
            try:
                mark = float(
                    input(f"Enter marks for subject {i + 1}: ")
                )
            except ValueError:
                print("Invalid marks. Please enter a number.")
                return

            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(mark)

        student = Student(name, roll_no, marks)
        self.add_student(student)

        print("Student added successfully!")



    def display_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.display()
            print("----------------")


    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                student.display()
                return

        print("Student not found.")



def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.create_student()

        elif choice == "2":
            manager.display_students()

        elif choice == "3":
            roll_no = int(input("Enter roll number to search: "))
            manager.search_student(roll_no)

        elif choice == "4":
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
