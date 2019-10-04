import math
from pylab import *
from scipy import signal

'''
Filter Builder Classes

MultiStage_Low & MultiStage_High classes are final and complete

Each classes take cut-off frequency, H, A, c5 as input, 
the remaining variables will be solved for via self.solveFor()

Bode plots across a pre-defined variable 't' can be constructed through the plot command. 
Phase plots available, but not currently implemented 

Licence: CC0 - Oct 4th, 2019 because why not
Questions?
Email: malm4036@stthomas.edu
'''
def printDetials(self):

        print("Wo = " + repr(self.wo)+ ", f = " + repr(self.f) + ", a = " + repr(self.a) + ", q = " + repr(self.q))


class MultiStage_Low:
    r1, r3, r4, c2, c5 = 0, 0, 0, 0, 0
    wo = 0.0
    f = 0.0
    k = 0.0
    h = 0.0
    q = 0.0
    a = 0.0
    def solveFor(self, f, h, a, c5):

        k = 2 * math.pi * f * c5
        c2 = (4/ (a ** 2)) * (h + 1) * c5
        r1 = (a / 2) * h * k
        r3 = a / (2 * (h + 1) * k)
        r4 =  r1 # a / (2 * k)

        return  k, r1, r3, r4, c2

    def __init__(self, f, h, a, c5):
        self.f = f
        self.h = h
        self.a = a
        self.c5 = c5

        self.k, self.r1, self.r3, self.r4, self.c2 = self.solveFor(f, h, a, c5)
        
        return
        
    def plot(self, f, cascaded = 1):
        topC = (-1 * self.h * (1 / (self.r1 * self.r3 * self.c2 * self.c5)))
        bottomC1 = (1 / self.c2) * ((1/self.r1) + (1/self.r3) + (1/self.r4))
        bottomC2 = 1 / (self.r3 * self.r4 * self.c2 * self.c5)
        system = signal.lti([topC], [1, bottomC1, bottomC2])
        #system = signal.lti([1], [1/(4000*math.pi),1])
        w = 2 * math.pi * f
        w, mag, phase = signal.bode(system, w)
        semilogx(f, mag)

        return mag
    


class MultiStage_High:
    r5, r2, c1, c4, c3 = 0, 0, 0, 0, 0
    wo = 0.0
    f = 0.0
    k = 0.0
    h = 0.0
    q = 0.0
    a = 0.0
    def solveFor(self, f, h, a, c1):

        k = 2 * math.pi * f * c1
        c3 = c1
        c4 = c1/h
        r2 = a / (k * (2 + (1/h)))
        r5 = (h * (2 + (1/h))) / ( a * k)

        return  k, r2, r5, c3, c4

    def __init__(self, f, h, a, c1):
        self.f = f
        self.h = h
        self.a = a
        self.c1 = c1

        self.k, self.r2, self.r5, self.c3, self.c4 = self.solveFor(f, h, a, c1)
        
        return
        
    def plot(self, f, cascaded = 1):
        topC = (-1 * (self.c1 / self.c4))
        bottomC1 = (self.c1 + self.c4 + self.c3) / (self.c3 * self.c4 * self.r5)
        bottomC2 = 1 / (self.r2 * self.r5 * self.c3 * self.c4)
        system = signal.lti([topC, 0, 0], [1, bottomC1, bottomC2])
        #system = signal.lti([1], [1/(4000*math.pi),1])
        w = 2 * math.pi * f
        w, mag, phase = signal.bode(system, w)
        semilogx(f, mag)

        return mag
    

'''
class High_Pass_Filter:
    r1, r2, c1, c2 = 0, 0, 0, 0
    wo = 0.0
    f = 0.0
    q = 0.0
    a = 0.0
    def solveFor(self, R1, R2, C1, C2):

        wo = 1 / (math.sqrt(R1 * R2 * C1 * C2))
        f = wo / (2 * math.pi)
        d = (self.r1 * self.r2 * self.c1 * 2)
        a = (self.r1 + self.r2) / d
        q = wo / a 

        return  wo, f, a, q

    def __init__(self, R1 = 0, R2 = 0, C1 = 0, C2 = 0):
        self.r1 = R1
        self.r2 = R2
        self.c1 = C1
        self.c2 = C2

        self.wo, self.f, self.a, self.q = self.solveFor(R1, R2, C1, C2)
        
        return
        
    def plot(self, f, cascaded = 1):
        system = signal.lti([1, 0, 0], [1, 2 * self.a, (self.wo ** 2)])
        #system = signal.lti([1], [1/(4000*math.pi),1])
        w = 2 * math.pi * f
        w, mag, phase = signal.bode(system, w)
        semilogx(f, mag)

        return mag
    


class Low_Pass_Filter:
    r1, r2, c1, c2 = 0, 0, 0, 0
    wo = 0.0
    f = 0.0
    q = 0.0
    a = 0.0
    def solveFor(self, R1, R2, C1, C2):

        wo = 1 / (math.sqrt(R1 * R2 * C1 * C2))
        f = wo / (2 * math.pi)
        d = (self.r1 * self.c1 * self.c2 * 2)
        a = (self.c1 + self.c2) / d
        q = wo / a 

        return  wo, f, a, q

    def __init__(self, R1 = 0, R2 = 0, C1 = 0, C2 = 0):
        self.r1 = R1
        self.r2 = R2
        self.c1 = C1
        self.c2 = C2

        self.wo, self.f, self.a, self.q = self.solveFor(R1, R2, C1, C2)
        
        return
        
    def plot(self, f, cascaded = 1):
        system = signal.lti([(1 * self.wo ** 2)], [1, 2 * self.a, (self.wo ** 2)])
        #system = signal.lti([1], [1/(4000*math.pi),1])
        w = 2 * math.pi * f
        w, mag, phase = signal.bode(system, w)
        semilogx(f, mag)

        return mag
    def printDetials(self):
        print("Wo = " + repr(self.wo))
        print("f = " + repr(self.f))
        print("a = " + repr(self.a))
        print("q = " + repr(self.q))



class band_pass_filter:

    R1, R2, C1, C2, Ra, Rf = 0, 0, 0, 0, 1, 1
    _function = None
    wo = 0
    a = 0
    def __init__(self, filter, hz1 = 20, hz2 = 20, Q = 1, R1 = 0, R2 = 0, C1 = 0, C2 = 0, Ra = 0, Rf = 0):
       
       if(R1 + R2 + C1 + C2 == 0):
           R = 1
           C = 100 ** -6
           w1 = hz1 * 2 * math.pi
           w2 = hz2 * 2 * math.pi
           

       else:
            self.R1 = R1
            self.R2 = R2
            self.C1 = C1
            self.C2 = C2
            self.Ra = Ra
            self.Rf = Rf
'''