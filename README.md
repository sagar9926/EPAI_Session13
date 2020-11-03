# Created By : Sagar Agrawal

# EPAI Session 13 : Sequences

## A regular strictly convex polygon is a polygon that has the following characteristics:

* All interior angles are less than 180
* All sides have equal length

![](https://cdn-skill.splashmath.com/panel-uploads/GlossaryTerm/a6639fe615d14e21939cdbd33d4d51fe/1564673544_polygon.png)

![](https://1.bp.blogspot.com/-V2BlJdpTLgg/W59zYdx1L3I/AAAAAAAAFec/0QRvbJ1lEBwd6D1W64s_RexCVf5mTTEdgCLcBGAs/s1600/jpeg2.jpg)

Objective 1 [pts:400]:
Create a Polygon Class:
where initializer takes in:
number of edges/vertices
circumradius
that can provide these properties:
# edges
# vertices
interior angle
edge length
apothem
area
perimeter
that has these functionalities:
a proper __repr__ function
implements equality (==) based on # vertices and circumradius (__eq__)
implements > based on number of vertices only (__gt__)
Objective 2 [pts:600]:
Implement a Custom Polygon sequence type:
where initializer takes in:
number of vertices for largest polygon in the sequence
common circumradius for all polygons
that can provide these properties:
max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
that has these functionalities:
functions as a sequence type (__getitem__)
supports the len() function (__len__)
has a proper representation (__repr__)
Results:
Implement these 2 classes as a separate module. Access these modules in a jupyter-notebook (or Google Colab or Deep Note)
Run Objective 1 module to show that the functionalities are implemented properly
Run Objective 2 module and show which polygon is efficient for n = 25
You are submitting link to your GitHub repo, where we can find the 2 modules and your notebook in which you have called and tested them
All your code must be publicly accessible (make sure to open all links in an incognito window before submitting)
