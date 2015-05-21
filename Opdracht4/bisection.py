#!/usr/bin/python3

def findRoot(f,a,b,epsilon):
    m = (a+b)/2
    while abs(b-a) > epsilon:
        if f(m) == 0:
            return m
        elif f(b)*f(m) < 0:
            a = m
        else:
            b = m
        m = (a+b)/2
    return m

def findAllRoots(f,a,b,epsilon):
    lijst = []
    m = (a+b)/2
    #while abs(b-a) > epsilon:
    while m < 0:
        if f(m) == 0:
            lijst.append(m)
        elif f(m)*m > 0:
            b = m
        elif f(a)*f(m) < 0:
            b = m
        else: break
        m = (a+b)/2
    lijst.append(m)
    while m > 0:
        if f(m) == 0:
            lijst.append(m) 
        elif f(m)*m < 0:
            a = m
        elif f(b)*f(m) <0:
            a = m
        else: break
        m = (a+b)/2
    lijst.append(m)
    
    return lijst