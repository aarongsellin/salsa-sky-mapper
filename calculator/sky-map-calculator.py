import math, sys, os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class sky_map_calculator:
    def __init__(self, data_path=None, output_file=None):
        # Constants
        self.Ro = 8.5
        self.Vo = 220

        # Lists
        self.xcords = []
        self.ycords = []

        if data_path:
            self.read_data(data_path)
        else:
            self.read_default_data()

        # Perform calculations
        self.calculate_coordinates()

    def read_data(self, path):
        # Check if file exists
        if os.path.isfile(path):
            # File exists
            self.data = pd.read_csv(path)
        else:
            # File does not exist, raise an error
            raise FileNotFoundError(f"Could not find file at {path}")
        
    def read_default_data(self):
        # Read default data
        self.data = pd.read_csv("./datasets/example-data.csv")

    def calculate_coordinates(self):

        # Extract velocity and longitude columns
        velocities = self.data['velocity']
        longitudes = self.data['longitude']

        # Calculations
        for v, longitude in zip(velocities, longitudes):
            # Get velocity and longitude
            longitudeRad = math.radians(longitude)

            # Calc R
            r = (self.Ro*self.Vo*math.sin(longitudeRad))/(self.Vo*math.sin(longitudeRad)+v)
            
            # If longitude is between 0 < l < 90 or 270 < l < 360, then this next step is neccessary.
            if (0 < longitude < 90 or 270 < longitude < 360):
                r = math.sqrt(math.pow(r,2)-(math.pow(self.Ro,2)*math.pow(math.sin(longitudeRad),2))) + self.Ro * math.cos(longitudeRad)

            # Calc x
            x = r * math.cos(longitudeRad-(math.pi/2))
            
            # Calc 
            y = r * math.sin(longitudeRad-(math.pi/2)) + self.Ro

            # Add coordinates to global list
            self.xcords.append(x)
            self.ycords.append(y)

        # Output calculations to a file
        self.output_to_file()

    def output_to_file(self):
        # Output to file
        if output_file:
            with open(output_file + ".txt", 'w') as f:
               f.write("x,y\n")
               for x, y in zip(self.xcords, self.ycords):
                    f.write(f"{x},{y}\n")

    def plot(self):
        # Create a new figure
        fig, ax = plt.subplots()

        # Plot the x and y coordinates
        ax.plot(self.xcords, self.ycords, 'D', color="purple", markersize=5)

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

if __name__ == "__main__":
    data_path = None
    output_file = None
    plot = True

    # Parse command-line arguments
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "-plot":
            pass
        elif sys.argv[i] in ["-plot=False","-plot=false"]:
            plot = False
        elif sys.argv[i].startswith("-output") or sys.argv[i].startswith("-out"):
             _, output_file = sys.argv[i].split("=")
        elif sys.argv[i].startswith("-data"):
            if i + 1 < len(sys.argv):
                _, data_path = sys.argv[i].split("=")
            else:
                raise ValueError("Invalid command addition: -data")
        else:
            raise ValueError(f"Unknown command {sys.argv[i]}")

    calc = sky_map_calculator(data_path=data_path, output_file=output_file)

    if plot:
        calc.plot()
