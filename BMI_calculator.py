def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

print("Welcome to the BMI Calculator!")

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")
