# Student Grade Management System
# This program calculates the average score and assigns a grade

def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3


def determine_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def main():
    print("Student Grade Management System")

    student_name = input("Enter student name: ")

    score1 = float(input("Enter score for Subject 1: "))
    score2 = float(input("Enter score for Subject 2: "))
    score3 = float(input("Enter score for Subject 3: "))

    average = calculate_average(score1, score2, score3)
    grade = determine_grade(average)

    print("\n--- Result ---")
    print("Student Name:", student_name)
    print("Average Score:", average)
    print("Grade:", grade)


main()
