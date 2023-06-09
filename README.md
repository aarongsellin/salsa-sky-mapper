# Salsa Sky Mapper

SalsaSkyMapper is a Python project for calculating the structure of the Milky Way using data from the Salsa radio telescope which is at Onsala Space Observatory.

## Introduction

This project provides a Python script for automatically calculating the positions of hydrogen clouds in our galaxy. 
It does this by utilizing 3 equations, two for calculating the distance between the gas cloud and the galactic center,
and another for converting that distance to Cartesian coordinates.

### Equations for Calculating Distance between gas cloud and galactic center

The following equation is always applied to calculate the distance no matter what the value of $l$ is:

$R = \frac{{R_0 V_0 \sin(l)}}{{V_0 \sin(l) + V_r}}$

And If $0&deg < l < 90&deg$ or $270&deg < l < 360&deg$ then the following calculation has to be done to get the correct distance:

$r = {\sqrt{R^2 - R_0^2 \sin^2 l }+ R_0 \cos l}$

### Equations for converting to Cartesian coordinates

${x, y} = {r cos(l - 90°), r sin(l - 90°)}$

##
