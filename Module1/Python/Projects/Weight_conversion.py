weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (kg/lbs): ")

if unit == "kg":
  weight *= 2.205
  unit = "Lbs"
  print(f"Your weight after conversion is: {round(weight, 1)} {unit}")
elif unit == "lbs":
  weight /= 2.205
  unit = "Kg"
  print(f"Your weight after conversion is: {round(weight, 1)} {unit}")
else:
  print(f"Unit {unit} is invalid!")

