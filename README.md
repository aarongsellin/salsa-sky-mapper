# Salsa Sky Mapper

SalsaSkyMapper is a Python project for calculating the structure of the Milky Way using data from the Salsa radio telescope which is at Onsala Space Observatory.

## Introduction

This project provides a Python script for automatically calculating the positions of hydrogen clouds in our galaxy. 
It does this by utilizing 3 equations, two for calculating the distance between the gas cloud and the galactic center,
and another for converting that distance to Cartesian coordinates.

This entire project is based on information from a SALSA project documentation titled, Mapping the Milkyway and you
can find it on the [SALSA website](https://liv.oso.chalmers.se/salsa/support).

## Interactive Play (In Development)

A feature that is currently being developed for this repository is the ability to play around with how the calculations
are made in an interactive sandbox esc enviornment. A user should be able to modulate variables like
the relative velocity $V$, the longitude $l$ and then see live how it affects the readings and where the gas cloud
ends up on a Cartesean map of the Galaxy. Another feature will be a small library of examples of how many observations, 
in a time interval will affect the readings. Meaning it would be able to generate sample observational data to illustrate
what someone doing them could expect it to look like when they are all done with thei observations. 
The image below is figure 2.1 from the afformentioned SALSA project, Mapping the Milkyway, and is an example of how to
graphical user interface might look.

![interactive](https://github.com/mrikea4real/salsa-sky-mapper/assets/79717170/90d8ae12-fe9f-4c9e-acac-e17c4b17d8ca)

$C$ is the location of the galactic center, $S$ is that of the sun and $M$ is a gas cloud. 

### Constants

$V_0$ Sun's velocity around the Galactic center, i.e., 220 km/s

$R_0$ Distance from the Sun to Galactic center, i.e., 8.5 kpc

$l$ Galactic longitude of observation

$V$ Velocity of a cloud of gas

$R$ Cloud's distance to the Galactic center

### Equations for Calculating Distance between gas cloud and galactic center

The following equation is always applied to calculate the distance no matter what the value of $l$ is:

$R = \frac{{R_0 V_0 \sin(l)}}{{V_0 \sin(l) + V_r}}$

And If $0&deg < l < 90&deg$ or $270&deg < l < 360&deg$ then the following calculation has to be done to get the correct distance:

$r = {\sqrt{R^2 - R_0^2 \sin^2 l }+ R_0 \cos l}$

Distance calculation implemented in code:
![distance](https://github.com/mrikea4real/salsa-sky-mapper/assets/79717170/1ea517a8-14a3-4ed5-989d-56ad93d04463)

### Equations for converting distance to Cartesian coordinates

${x} = {r cos(l - 90°)}$

${y} = {r sin(l - 90°) + R_0}$

Conversion calculation implemented in code:

![conversion](https://github.com/mrikea4real/salsa-sky-mapper/assets/79717170/63c48d4f-fd3d-4419-a782-747a418870fc)
