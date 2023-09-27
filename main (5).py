class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the student list based on CGPA in descending order
    student_list.sort(key=lambda student: student.cgpa, reverse=True)

# Test the function with different input lists of students
if __name__ == "__main__":
    # Create a list of student objects
    students = [
        Student("Alice", "A101", 3.8),
        Student("Bob", "B102", 3.5),
        Student("Charlie", "C103", 4.0),
        Student("David", "D104", 3.9),
    ]

    # Print the original list of students
    print("Original list of students:")
    for student in students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")

    # Sort the list of students
    sort_students(students)

    # Print the sorted list of students
    print("\nSorted list of students (based on CGPA in descending order):")
    for student in students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")