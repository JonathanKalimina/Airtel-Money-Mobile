# MULUNGUSHI UNIVERSITY
# ICT111 - Student Grading System
# Lab 2: Student Grading System

students = []

while True:
    print("\n========== STUDENT GRADING SYSTEM ==========")
    print("1. Add student")
    print("2. Display all")
    print("3. Class summary")
    print("4. Exit")

    option = input("Choose an option (1-4): ").strip()

    if option == "1":
        # Get and validate student number
        while True:
            student_number = input("Enter student number: ").strip()
            if student_number == "":
                print("Student number cannot be blank. Please try again.")
            else:
                break

        # Get and validate student name
        while True:
            name = input("Enter student name: ").strip()
            if name == "":
                print("Student name cannot be blank. Please try again.")
            else:
                break

        # Get and validate the mark
        while True:
            mark_input = input("Enter student mark (0-100): ").strip()

            try:
                mark = float(mark_input)

                if mark < 0 or mark > 100:
                    print("Invalid mark. The mark must be between 0 and 100.")
                else:
                    break

            except ValueError:
                print("Invalid input. Please enter a numeric mark.")

        # Assign grade and decision
        if mark >= 80:
            grade = "A"
            decision = "Excellent"
        elif mark >= 70:
            grade = "B"
            decision = "Very good"
        elif mark >= 60:
            grade = "C"
            decision = "Good"
        elif mark >= 50:
            grade = "D"
            decision = "Pass"
        else:
            grade = "F"
            decision = "Fail"

        # Store the student's details in a dictionary
        student = {
            "student_number": student_number,
            "name": name,
            "mark": mark,
            "grade": grade,
            "decision": decision
        }

        # Add the dictionary to the students list
        students.append(student)

        print("\nStudent record added successfully!")
        print("Grade:", grade)
        print("Decision:", decision)

    elif option == "2":
        # Display all student records
        if len(students) == 0:
            print("\nNo student records are available yet.")
        else:
            print("\n================ STUDENT REPORT ================")

            for student in students:
                print("-----------------------------------------------")
                print("Student number:", student["student_number"])
                print("Name:", student["name"])
                print("Mark:", student["mark"])
                print("Grade:", student["grade"])
                print("Decision:", student["decision"])

            print("================================================")

    elif option == "3":
        # Calculate and display class statistics
        if len(students) == 0:
            print("\nNo students have been added. Class statistics cannot be calculated yet.")
        else:
            total_students = len(students)
            total_marks = 0
            highest_mark = students[0]["mark"]
            lowest_mark = students[0]["mark"]
            passes = 0
            fails = 0

            for student in students:
                mark = student["mark"]
                total_marks = total_marks + mark

                if mark > highest_mark:
                    highest_mark = mark

                if mark < lowest_mark:
                    lowest_mark = mark

                if mark >= 50:
                    passes = passes + 1
                else:
                    fails = fails + 1

            average = total_marks / total_students

            print("\n============= CLASS SUMMARY =============")
            print("Total students:", total_students)
            print("Class average: {:.2f}".format(average))
            print("Highest mark:", highest_mark)
            print("Lowest mark:", lowest_mark)
            print("Number of passes:", passes)
            print("Number of fails:", fails)
            print("==========================================")

    elif option == "4":
        print("\nThank you for using the Student Grading System.")
        print("Program has exited successfully.")
        break

    else:
        print("\nInvalid menu option. Please choose 1, 2, 3 or 4.")
