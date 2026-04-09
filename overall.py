def student_averages(Students):
    """
    Calcula el promedio de calificaciones para cada estudiante.
    Entrada: diccionario de diccionarios con calificaciones.
    Salida: diccionario con el promedio de cada estudiante (redondeado).
    """
    averages = {}
    for student_id, assignments in students.items():

        grades = assignments.values()

        avg = sum(grades) / len(grades) if grades else 0
        averages[student_id] = round(avg)
    return averages
def assignment_averages(Students):
    """
    Calcula el promedio de calificaciones para cada tarea.
    Entrada: diccionario de diccionarios con calificaciones.
    Salida: diccionario con el promedio de cada tarea (redondeado).
    """

    assignments_totals = {}
    assignments_counts = {}
    
    for student_id, assignments in students.items():
        for assignment, grade in assignments.items():
            assignments_totals[assignment] = assignments_totals.get(assignment, 0) + grade
            assignments_counts[assignment] = assignments_counts.get(assignment, 0) + 1

    averages = {}
    for assignment in assignments_totals:
        avg = assignments_totals[assignment] / assignments_counts[assignment]
        averages[assignment] = round(avg)

    return averages 

if __name__ == "__main__":
    students = {
        "s1": {"hw1": 80, "hw2": 90, "hw3": 100},
        "s2": {"hw1": 70, "hw2": 75, "hw3": 85},
        "s3": {"hw1": 95, "hw2": 85, "hw3": 90}
    }

    print(student_averages(students))
    # {'s1': 90, 's2v': 77, 's3': 90}

    print(assignment_averages(students))
    # {'hw1': 82, 'hw2': 83, 'hw3': 92}