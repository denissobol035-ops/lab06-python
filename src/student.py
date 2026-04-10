from typing import List

class Student:
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name: str = name
        self.group: str = group
        self.average_grade: float = average_grade

    def __str__(self) -> str:
        return (
            f"Student {self.name} from group {self.group} "
            f"with average grade {self.average_grade}"
        )

    def __repr__(self) -> str:
        return (
            f"Student(name='{self.name}', "
            f"group='{self.group}', "
            f"average_grade={self.average_grade})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return False
        return (
            self.name == other.name
            and self.group == other.group
            and self.average_grade == other.average_grade
        )

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            raise TypeError("Cannot compare Student with non-Student")
        return self.average_grade < other.average_grade


# =========================
# Demonstration
# =========================

print("--- Task A ---")
student1: Student = Student("Denis", "CS-124", 89.5)
print("Student name:", student1.name)
print("Student group:", student1.group)
print("Student average grade:", student1.average_grade)

print()
print("--- Task B ---")
print("Internal dictionary:", student1.__dict__)
print("Changing grade using __dict__")
student1.__dict__["average_grade"] = 95.0
print("Updated grade:", student1.average_grade)

print()
print("--- Task C ---")
print("Human-readable output:")
print(student1)

print()
print("--- Task D ---")
print("Developer representation:")
print(repr(student1))

print()
print("--- Task E ---")
student2: Student = Student("Denis", "CS-124", 95.0)
print("Are students equal?")
print(student1 == student2)

print()
print("--- Task F ---")
student3: Student = Student("Anna", "CS-124", 75.0)
print("Compare students by grade:")
print("student3 < student1:", student3 < student1)

print()
print("--- Task G ---")
students: List[Student] = [
    student1,
    student2,
    student3,
    Student("Ivan", "CS-124", 60.0),
]

print("Before sorting:")
for s in students:
    print(s)

students.sort()

print("After sorting (by average_grade):")
for s in students:
    print(s)
