# Created By : Sagar Agrawal

# EPAI Session 13 : Sequences

## A regular strictly convex polygon is a polygon that has the following characteristics:

* All interior angles are less than 180
* All sides have equal length

![](https://cdn-skill.splashmath.com/panel-uploads/GlossaryTerm/a6639fe615d14e21939cdbd33d4d51fe/1564673544_polygon.png)

![](https://1.bp.blogspot.com/-V2BlJdpTLgg/W59zYdx1L3I/AAAAAAAAFec/0QRvbJ1lEBwd6D1W64s_RexCVf5mTTEdgCLcBGAs/s1600/jpeg2.jpg)

## Objective 1 [pts:400]:

### Create a Polygon Class where initializer takes in:

* Number of edges/vertices
* Circumradius

#### That can provide these properties:

* Edges

* Vertices

* Interior angle

* Edge length

* Apothem

* Area

*Perimeter

#### That has these functionalities:

* A proper __repr__ function

* Implements equality (==) based on # vertices and circumradius (__eq__)

* Implements > based on number of vertices only (__gt__)

## Objective 2 [pts:600]:

### Implement a Custom Polygon sequence type where initializer takes in:

* Number of vertices for largest polygon in the sequence

* Common circumradius for all polygons

###That can provide these properties:

* Max efficiency polygon: returns the Polygon with the highest area: perimeter ratio

### That has these functionalities:

* Functions as a sequence type (__getitem__)

* Supports the len() function (__len__)

* Has a proper representation (__repr__)
