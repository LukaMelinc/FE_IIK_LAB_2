import math

# Convert phase angle from degrees to radians
phi_degrees = 120
phi_radians = math.radians(phi_degrees)

# Using the provided formula
resultant_voltage = (1 / math.sqrt(3)) * (600 - 150 * (math.cos(phi_radians) + 1j * math.sin(phi_radians)))

# Calculate the magnitude of the resultant voltage
resultant_voltage_magnitude = abs(resultant_voltage)

print(resultant_voltage_magnitude)