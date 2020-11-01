import math
from functools import lru_cache


class CustomPolygon :
    """
    Creates custom polygon sequence starting from number of vertices = 3 till the maximum specified number of vertices and common circum radius.
            Parameters : 
                max_edges : Maximum number of edges/vertices of polygon in sequence
                common_circum_radius : Circum radius of polygon
            Returns : 
                efficiency : List comprising efficiency values (area/perimeter) for all the polygons in sequence
                max_efficiency : Returns the Polygon with the highest area : perimeter ratio
    """
    
    def __init__(self,max_edges,common_circum_radius):
        self.max_edges = max_edges
        self.common_circum_radius = common_circum_radius
    
    def __len__(self):
        return self.max_edges - 2
        
    def __getitem__(self,s):
        if isinstance(s,int):
            if s < 0:
                s = s + self.__len__()
            if s < 0 or s >= self.__len__():
                raise IndexError
            else:
                return CustomPolygon._efficiency(s+3,self.common_circum_radius)
        if isinstance(s,slice):
            start,stop,step = s.indices(self.__len__())
            rng = range(start,stop,step)
            return [CustomPolygon._efficiency(i+3,self.common_circum_radius) for i in rng]

    @lru_cache(2**10)     
    def _edgeLength(common_circum_radius,edges):
        return(2*common_circum_radius * math.sin(math.pi/edges))
    
    @lru_cache(2**10)     
    def _apothem(common_circum_radius,edges):
        return(common_circum_radius*math.cos(math.pi/edges))
    
    @lru_cache(2**10)
    def _efficiency(edges,common_circum_radius):
        area = 0.5 * edges * CustomPolygon._edgeLength(common_circum_radius,edges) * CustomPolygon._apothem(common_circum_radius,edges)
        perimeter = edges * CustomPolygon._edgeLength(common_circum_radius,edges)
        #print(f"Edges {edges}, Area {area} , Perimeter {perimeter}")
        return (area/perimeter)
    
    @property
    def max_efficiency(self):
        slices = slice(0,self.__len__())
        efficiency = self.__getitem__(slices)
        max_efficiency = max(efficiency)
        print(f'Maximum efficiency polygon has Vertices : {efficiency.index(max_efficiency) + 3} and Circum Radius : {self.common_circum_radius} ')
        return efficiency.index(max_efficiency) + 3
    
    def __repr__(self):
        return f'CustomPolygon(MaximumEdge = {self.max_edges}, Circum Radius = {self.common_circum_radius})'
