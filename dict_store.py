# Write your code here!

def temp_and_color(data):
    """
    Recibe un diccionario con información de temperatura y color y retorna una tupla con:
    - El valor bajo la clave 'temp' si existe, de lo contrario retorna None.
    -El valor bajo la clave 'color' si existe, de lo contrario retorna none.
    """

    temp_value = data.get("temp", None)
    color_value = data.get("color", None)
    return (temp_value, color_value)

if __name__ == "__main__":
    data1 = {"temp": 25, "color": "blue", "status": "ok"}
    print(temp_and_color(data1))

    data2 = {"status": "ok"}
    print(temp_and_color(data2))
