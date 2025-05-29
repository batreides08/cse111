import math
from datetime import datetime

# Prompt the user for input
w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the tire volume
volume = (math.pi * (w ** 2) * a * (w * a + 2540 * d)) / 10000000000

# Display the result 
print(f"The approximate volume is {volume:.2f} liters")

# Get the current date
current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d")

# Open the file and append the data
with open("volumes.txt", "at") as file:
    file.write(f"{formatted_date}, {w}, {a}, {d}, {volume:.2f}\n")

