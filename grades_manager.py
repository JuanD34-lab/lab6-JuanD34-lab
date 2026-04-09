def initialize_dict(student_name, subject_grades):
    """
    Retorna un diccionario con un estudiante y sus materias.
    """
    return {student_name: subject_grades}

def add_student(student_grades = None):
    """
    Permite agregar a un estudiante y sus calificaciones a un diccionario
    """
    if student_grades is None:
        student_grades = {}

    name = input("Enter student name: ").strip().title()
    subjects = {}

    while True:
        entry = input("Enter subject and grade (or 'exit' to finish): ").strip()
        if entry.lower() == "exit":
            break

        if "," not in entry:
            print("Invalid format. Use <subject>,<grade>.")
            continue
        
        subject, grade = entry.split(",", 1)
        subject = subject.strip().title()
        grade_str = grade.strip()

        if grade_str.replace(".", 1).isdigit():
            subjects[subject] = float(grade_str)
        else:
            print("Invalid grade. Must be a number.")

        student_grades[name] = subjects
        print(f"Student {name} succesfully added to the grades management system./n")
        return student_grades