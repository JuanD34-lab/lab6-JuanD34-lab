# Write your code here!

def employee_print(employee_info):
    """
    Recibe un diccionario con información de un empleado. 
    Imprime siempre Name, salary y Role (o 'N/A' si no existen).
    Luego imprime cualquier otra clave-valor restante.
    Si no hay información adicional, imprime 'No additional info!'.
    """

    name = employee_info .get("Name", "N/A")
    salary = employee_info.get("salary", "N/A")
    role = employee_info.get("role", "N/A")

    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")

    remaining_info = dict(employee_info)
    remaining_info.pop("Name", None)
    remaining_info.pop("Salary", None)
    remaining_info.pop("Role", None)

    if remaining_info:
        for key, value in remaining_info.items():
            print(f"{key}: {value}")
        else:
            print("No additional info!")

if __name__ == "__main__":
    data1 = {}
    employee_print(data1)
    # Salida:
    # Name: N/A
    # Salary: N/A
    # Role: N/A
    # No other info!

    data2 = {
        "Name": "Diego",
        "Salary": 5000000,
        "Role": "Janitor",
        "Years at company": 9001,
        "Hours per week": 2
    }
    employee_print(data2)
    # Salida:
    # Name: Diego
    # Salary: 5000000
    # Role: Janitor
    # Years at company: 9001
    # Hours per week: 2
