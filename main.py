from tkinter.font import names

from grades_manager import add_student, avg_by_student

def main():
    print("Welcome to the Student Grades Manager!/n")
    my_grades = {}

    while True:
        print("Select an option:")
        print("1 add a student")
        print("2. Print student grade averages")
        print("3. Exit/n")
        
        option = input().strip()
        if option == "1":
            my_grades = add_student(my_grades)

        elif option == "2":
            print("Select an option:")
            print("a. Display all students")
            print("b. Display selected students/n")

            sub_option = input().strip().lower()
            if sub_option == "a":
                avg_by_student(my_grades, names)
            else:
                print("Invalid option selected!/n")

        elif option == "3":
            print("Goodbye!")

        else:
            print("Invalid option selected!/n")

    if __name__ == "__main__":
        main()
