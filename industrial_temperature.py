def trigger_alarm(temperatures, threshhold=80):
    """
    Retorna una lista con los nombres de los sensosres cuya lectrura supera estrictamente el limite dado.
    """
    triggered = []
    for sensor, temp in temperatures.items():
        if temp > threshold:
            triggered.append(sensor)
    return triggered

temperatures = {
    "sensor_1": 85.5,
    "sensor_2": 90.2, 
    "sensor_3": 78.8,
    "sensor_4": 92.3
}
threshold = 88
print(trigger_alarm(temperatures, threshold))

temperatures = {
    "sensor_A": 79.0,
    "sensor_B": 81.2, 
    "sensor_C": 75.4,
    "sensor_D": 85.7
}
print(trigger_alarm(temperatures))