#!/usr/bin/python3

import math

class Vector(object):
    def __init__(self,n,x=0):
        self.round = True
        if type(x) == list:
            self.elems = [float(x) for x in x]
        else:
            self.elems = n*[float(x)]
            if x != 0:
                self.round = False

    def __str__(self):
        if self.round == True:
            return '\n'.join(["{:.6f}".format(i) for i in self.elems])
        else:
            return '\n'.join([str(i) for i in self.elems])

    def lincomb(self,other,alpha,beta):
        answers = list(map(lambda x,y: x*alpha + y*beta, self.elems,other.elems))
        return Vector(len(answers), answers)

    def scalar(self,alpha):
        #answers = [x*alpha for x in self.elems] 
        answers = list(map(lambda x: x*alpha, self.elems))       
        return Vector(len(answers), answers)
        
    def inner(self,other):
        answers = list(map(lambda x,y: x*y, self.elems,other.elems))
        return sum(answers)

    def norm(self):
        #answers = [x**2 for x in self.elems]
        answers = list(map(lambda x: x**2, self.elems))
        return math.sqrt(sum(answers))