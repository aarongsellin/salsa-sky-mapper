import math
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Constants
Ro = 8.5
Vo = 220

# Lists
xcords = []
ycords = []

# Data
data = pd.read_csv("example-data.csv")

# Extract velocity and longitude columns
velocities = data['velocity']
longitudes = data['longitude']

# Calculations
for v, longitude in zip(velocities, longitudes):
    # Get velocity and longitude
    longitudeRad = math.radians(longitude)

    # Calc R
    r = (Ro*Vo*math.sin(longitudeRad))/(Vo*math.sin(longitudeRad)+v)
    
    # If longitude is between 0 < l < 90 or 270 < l < 360, then this next step is neccessary.
    if (0 < longitude < 90 or 270 < longitude < 360):
        r = math.sqrt(math.pow(r,2)-(math.pow(Ro,2)*math.pow(math.sin(longitudeRad),2))) + Ro * math.cos(longitudeRad)

    # Calc x
    x = r * math.cos(longitudeRad-(math.pi/2))
    
    # Calc 
    y = r * math.sin(longitudeRad-(math.pi/2)) + Ro

    # Add coordinates to global list
    xcords.append(x)
    ycords.append(y)

# Create a new figure
fig, ax = plt.subplots()

# Plot the x and y coordinates
ax.plot(xcords, ycords, 'D', color="purple", markersize=5)

plt.xlabel(("X kpc"))
plt.ylabel(("Y kpc"))
plt.title("The Milkyway")

plt.grid(True)

# Draw a turquoise circle in the middle of the screen
circle = Circle((0, 0), 25, color='turquoise',alpha=0.3)  # Radius is half the diameter
ax.add_patch(circle)

# Set the aspect ratio to equal
ax.set_aspect('equal', adjustable='box')

# Set the x and y axis limits
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)

# Display the plot
plt.show()
