def weather_condition(temperature):
    if temperature >= 7:
        return "Warm"
    else:
        return "Cold"

inputTemp = float(input("Enter temperature:"))

print(weather_condition(inputTemp))