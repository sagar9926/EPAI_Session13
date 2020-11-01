import math

class Polygon :
    
    """
    Creates a polygon with specified number of vertices and circum radius.
        
            Parameters : 
                number_edges : Number of edges/vertices of polygon
                circum_radius : Circum radius of polygon
            Returns : 
                interiorAngle=(n−2)*180/n 
                edgeLength,s=2*R*sin(π/n)
                apothem,a=R*cos(π/n)
                area=1/2*n*s*a
                perimeter=n*s
    """
    
    def __init__(self,number_edges,circum_radius):
        self.edges = number_edges
        self.circum_rad = circum_radius
        
    @property
    def edges(self):
        print("Getting Edges...")
        return self._number_edges
    
    @edges.setter
    def edges(self,number_edges):
        print("Setting edges value...")
        if number_edges < 3:
            raise ValueError("Minimum number of edges required to form a polygon is 3")
        self._number_edges = number_edges
        
    @property
    def circum_rad(self):
        print("Getting Cirum radius ...")
        return self._circum_rad
    
    @circum_rad.setter
    def circum_rad(self,circum_radius):
        print("Setting circum radius value...")
        if circum_radius < 0:
            raise ValueError("Cirum radius cannot be negative")
        self._circum_rad = circum_radius
   
    @property 
    def interiorAngle(self):
        return((self.edges - 2)*180 / self.edges)

    @property 
    def edgeLength(self):
        return(2*self.circum_rad * math.sin(math.pi/self.edges))
    
    @property
    def apothem(self):
        return(self.circum_rad*math.cos(math.pi/self.edges))
        
    @property
    def area(self):
        return(0.5 * self.edges* self.edgeLength * self.apothem)
    
    @property
    def perimeter(self):
        return(self.edges* self.edgeLength)
    
    def __repr__(self):
        return f'Polygon(Edges = {self.edges}, Circum Radius = {self.circum_rad})'
    
    def __eq__(self,other):
        if isinstance(self,type(other)):
            return ((self.edges == other.edges) and self.circum_rad == other.circum_rad)
        else:
            raise TypeError(f"Cannot compare values of type {self.__class__} and {other.__class__}")
            
    def __gt__(self,other):
        if isinstance(self,type(other)):
            return (self.circum_rad > other.circum_rad)
        else:
            raise TypeError(f"Cannot compare values of type {self.__class__} and {other.__class__}")
