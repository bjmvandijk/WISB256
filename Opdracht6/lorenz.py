#!/usr/bin/python3

import numpy
from scipy import integrate
import matplotlib.pyplot as plt

class Lorenz(object):
    def __init__(self, xyz, sigma=10, rho=28, beta=(8/3)): 
        self.test = True
        self.xyz = xyz
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
        if type(xyz) == list:
            self.elems = [float(xyz) for xyz in xyz]

        else:
            self.test = False
 
    def __str__(self):
        if self.test == True:
            print(xzy)
            return '\n'.join(["{:.6f}".format(i) for i in self.elems])
        else:
            return "Use [x,y,z] instead of x,y,z" + '\n'

    def func(self, xyz, t):
        q = [0, 0, 0]
        q[0] = self.sigma*(xyz[1] - xyz[0]) 
        q[1] = xyz[0]*(self.rho - xyz[2]) - xyz[1]
        q[2] = xyz[0]*xyz[1] - self.beta*xyz[2]
        return q


    def solve(self, T, dt):
        self.t = numpy.arange(0, T, dt)
        sol = integrate.odeint(self.func, self.xyz, self.t)
        return sol
