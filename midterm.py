# Function to calculate the letter grade based on the grade score
def calculate_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

# Main program
students = 5

for i in range(students):
    # Get input for each student's grades
    print(f"Enter the grades for student {i+1}:")
    student_name = input("Name: ")
    enabling_assessment1 = float(input("Enabling Assessment 1: "))
    enabling_assessment2 = float(input("Enabling Assessment 2: "))
    enabling_assessment3 = float(input("Enabling Assessment 3: "))
    enabling_assessment4 = float(input("Enabling Assessment 4: "))
    enabling_assessment5 = float(input("Enabling Assessment 5: "))
    summative_grade1 = float(input("Summative Assessment 1: "))
    summative_grade2 = float(input("Summative Assessment 2: "))
    summative_grade3 = float(input("Summative Assessment 3: "))
    final_exam = float(input("Final Examination: "))

    # Calculate averages
    enabling_assessment_average = (enabling_assessment1 + enabling_assessment2 + enabling_assessment3 + enabling_assessment4 + enabling_assessment5) / 5
    summative_average = (summative_grade1 + summative_grade2 + summative_grade3) / 3

    # Calculate grade using the formula
    grade = (enabling_assessment_average * 0.3) + (summative_average * 0.3) + (final_exam * 0.4)

    # Calculate letter grade
    letter_grade = calculate_letter_grade(grade)

    # Display the results
    print(f"\nStudent {i+1} Grades:")
    print(f"Name: {student_name}")
    print(f"Class Participation: {enabling_assessment_average:.2f}")
    print(f"Summative Grade: {summative_average:.2f}")
    print(f"Grade: {grade:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print("---------------------------------")
