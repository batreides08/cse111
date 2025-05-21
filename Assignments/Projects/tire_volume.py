import math

# Prompt the user for input
w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the tire volume using the given formula
volume = (math.pi * (w ** 2) * a * (w * a + 2540 * d)) / 10000000000

# Display the result rounded to two decimal places
print(f"The approximate volume is {volume:.2f} liters")
