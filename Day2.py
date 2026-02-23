import csv
import os

# -------------------- STUDENT CLASS --------------------

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks  # dictionary: subject -> marks

    def calculate_percentage(self):
        total_marks = sum(self.marks.values())
        max_marks = len(self.marks) * 100
        percentage = (total_marks / max_marks) * 100
        return round(percentage, 2)

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        else:
            return "D"

    def update_mark(self, subject, new_mark):
        if subject in self.marks:
            self.marks[subject] = new_mark
            print("Marks updated successfully.")
        else:
            print("Subject not found.")

# -------------------- CSV FILE HANDLING --------------------

CSV_FILE = "results.csv"

def export_to_csv(student):
    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Roll No", "Name", "Percentage", "Grade"])

        writer.writerow([
            student.roll_no,
            student.name,
            student.calculate_percentage(),
            student.calculate_grade()
        ])

    print("Result exported to CSV successfully.")

# -------------------- MAIN PROGRAM --------------------

def main():
    students = []

    while True:
        print("\n===== Student Result Management System =====")
        print("1. Add Student")
        print("2. Update Student Marks")
        print("3. Export Results to CSV")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll_no = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")

            marks = {}
            subjects_count = int(input("Enter number of subjects: "))

            for i in range(subjects_count):
                subject = input(f"Enter subject {i+1} name: ")
                mark = int(input(f"Enter marks for {subject}: "))
                marks[subject] = mark

            student = Student(roll_no, name, marks)
            students.append(student)

            print("Student added successfully.")
            print(f"Percentage: {student.calculate_percentage()}%")
            print(f"Grade: {student.calculate_grade()}")

        elif choice == "2":
            roll_no = input("Enter roll number to update: ")
            found = False

            for student in students:
                if student.roll_no == roll_no:
                    subject = input("Enter subject to update: ")
                    new_mark = int(input("Enter new marks: "))
                    student.update_mark(subject, new_mark)
                    print(f"Updated Percentage: {student.calculate_percentage()}%")
                    print(f"Updated Grade: {student.calculate_grade()}")
                    found = True
                    break

            if not found:
                print("Student not found.")

        elif choice == "3":
            for student in students:
                export_to_csv(student)

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

# -------------------- PROGRAM START --------------------

if __name__ == "__main__":
    main()
