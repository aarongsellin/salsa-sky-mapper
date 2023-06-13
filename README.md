# Salsa Sky Mapper Library

This is a library for calculating and making sense of data from the SALSA radio telescope at Onsala Space Observatory.

## Calculator
This project provides a Python script for automatically calculating the positions of hydrogen clouds in our galaxy. 
It does this by utilizing 3 equations, two for calculating the distance between the gas cloud and the galactic center,
and another for converting that distance to Cartesian coordinates.

### Command Line Options:

- `-plot`: Enable plotting the sky map (default: True).
- `-plot=False`: Disable plotting the sky map.
- `-output=<filename>` or `-out=<filename>`: Specify the output file name for the plotted data, without file extension.
- `-data=<filename>`: Specify the data file name for calculations. If not provided, the script will use the default data file.

In the example below, we don't want to plot the graph only calculate x & y values and output it to a file called calculated.txt: 

`py sky-map-calculator.py -plot=False out=calculated`

To understand how the calculations are done, read [this](further-reading/Understanding-The-Calculator.md).

This feature is based on information from a SALSA project documentation titled, Mapping the Milkyway and you
can find it on the [SALSA website](https://liv.oso.chalmers.se/salsa/support).

## Interactive Play (In Development)

The goal of Interactive Play is to provide tools for calculations and visualization, making it easier for intrigued astronomers to take a deep dive into the structure of the Milky Way's hydrogen clouds. This facilitates a better understanding of their positions and characteristics. To do this Interactive Play offers two key features:

 - **Theoretical Gas Cloud Placement**: This feature enables users to click on any position on the map and instantly see the calculated variables as if an observed gas cloud existed at that specific location. It provides a hypothetical scenario to explore the potential effects of different gas cloud placements.

 - **Observation Impact Simulation**: This feature demonstrates the impact of different observation quantities and time intervals on the readings obtained with the SALSA telescope. It allows users to simulate various observational scenarios and observe how different quantities and time intervals affect the resulting data and visualizations.

The image below is figure 2.1 from the afformentioned SALSA project, Mapping the Milkyway, and is an example of how to
graphical user interface might look for the variable explorer.

![interactive](https://github.com/mrikea4real/salsa-sky-mapper/assets/79717170/90d8ae12-fe9f-4c9e-acac-e17c4b17d8ca)

$C$ is the location of the galactic center, $S$ is that of the sun and $M$ is a gas cloud. 


