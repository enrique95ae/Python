def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

print(weather_condition(5))