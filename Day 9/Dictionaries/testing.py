student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

print(student_scores)

for student in student_scores:
    print(student)
    print(f"student score: {student_scores[student]}")
    if student_scores[student] >= 91:
        student_grades[student] = 'Outstanding'
    elif student_scores[student] >= 81 and student_scores[student] < 90:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] >= 71 and student_scores[student] < 80:
        student_grades[student] = "Acceptable"
    elif student_scores[student] < 70:
        student_grades[student] = "Acceptable"

print(student_grades)