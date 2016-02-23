# Implementation of a Vector class

class Vector:
    def __init__(self, list_):
        self.list_ = list_
        
    def get_list(self):
        return self.list_
    
    def check_lengths(self,v1,v2):
        if len(v1) != len(v2):
            raise Exception('Vectors are different lengths!')
    
    def add(self, v):
        self.check_lengths(self.get_list(), v.get_list())
        return Vector([e[0]+e[1] for e in zip(self.get_list(), v.get_list())])
    
    def subtract(self, v):
        self.check_lengths(self.get_list(), v.get_list())
        return Vector([e[0]-e[1] for e in zip(self.get_list(), v.get_list())])
      
    def dot(self, v):
        self.check_lengths(self.get_list(), v.get_list())
        return sum(e[0]*e[1] for e in zip(self.get_list(), v.get_list()))
        
    def norm(self):
        return pow(sum(pow(e,2) for e in self.get_list()), 0.5)
        
    def __str__(self):
        return str(self.get_list()).replace('[','(').replace(']',')').replace(' ','')
    
    def equals(self, v):
        if len(self.get_list()) != len(v.get_list()):
            return False
        else:
            return all([e[0] == e[1] for e in zip(self.get_list(), v.get_list())])