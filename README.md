# Salsa Sky Mapper

SalsaSkyMapper is a Python project for calculating the structure of the Milky Way using data from the Salsa radio telescope which is at Onsala Space Observatory.

## Introduction

This project provides a Python script for automatically calculating the positions of hydrogen clouds in our galaxy. 
It does this by utilizing 3 equations, two for calculating the distance between the gas cloud and the galactic center,
and another for converting that distance to Cartesian coordinates.

### Equations for Calculating Distance between gas cloud and galactic center

This equation is used when longitude is $0 < l < 90$ and $270 < l < 360
$R = \frac{{R_0 V_0 \sin(l)}}{{V_0 \sin(l) + V_r}}$


##
