# BMI (Body Mass Index) Calculator

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters (e.g. 1.75): "))

    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)

    print(f"\nYour BMI is: {bmi}")
    print(f"Category: {category}")

except ValueError:
    print("Please enter valid numbers for weight and height.")
