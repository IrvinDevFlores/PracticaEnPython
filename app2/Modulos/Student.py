from dataclasses import dataclass

@dataclass
class Student:
    name: str
    student_id: int
    score: float

student = Student("hoa", "1", "dsd")

print(f"nombre {student.name} id: {student.student_id}")