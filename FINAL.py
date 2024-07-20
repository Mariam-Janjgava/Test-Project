#Design of program displacement
def display_menu():
    print("\nStudent Grade Book Menu")
    print("1. Add Student Grade")
    print("2. Display All Grades")
    print("3. Calculate Average Grade")
    print("4. Determine Highest Grade")
    print("5. Determine Lowest Grade")
    print("6. Exit")

#addition of grades
def add_grade(grades):
    try:
        grade = float(input("Enter the student's grade: "))
        if 0 <= grade <= 100:
            grades.append(grade)
            print("Grade added successfully!")
        else:
            print("Invalid grade! Please enter a grade between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a numerical grade.")

#Showcasing the grades
def display_grades(grades):
    if grades:
        print("\nAll Student Grades:")
        for i, grade in enumerate(grades, start=1):
            print(f"Student {i}: {grade}")
    else:
        print("No grades available.")

#Average of the grades
def calculate_average(grades):
    if grades:
        average = sum(grades) / len(grades)
        print(f"\nAverage Grade: {average:.2f}")
    else:
        print("No grades available to calculate average.")

#The highest grade command
def determine_highest_grade(grades):
    if grades:
        highest = max(grades)
        print(f"\nHighest Grade: {highest}")
    else:
        print("No grades available to determine highest grade.")

#The lowest grade command
def determine_lowest_grade(grades):
    if grades:
        lowest = min(grades)
        print(f"\nLowest Grade: {lowest}")
    else:
        print("No grades available to determine lowest grade.")

#User command respond
def main():
    grades = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_grade(grades)
        elif choice == '2':
            display_grades(grades)
        elif choice == '3':
            calculate_average(grades)
        elif choice == '4':
            determine_highest_grade(grades)
        elif choice == '5':
            determine_lowest_grade(grades)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
