import numpy as np
import matplotlib.pyplot as plt
import math 
from filterBuilder import MultiStage_High
from filterBuilder import MultiStage_Low

import filterBuilder
'''
Filter Builder Driver

MultiStage_Low & MultiStage_High classes declared in filterBuilder.py used

Each classes take cut-off frequency, H, A, c5 as input, 
the remaining variables will be solved for via self.solveFor()

Magnitude of Transfer functions retrieved by <class>.plot(time[])

Plots Magnitude in End

Licence: CC0 - Oct 4th, 2019 because why not
Questions?
Email: malm4036@stthomas.edu
'''
max_t = 9
t_steps = 10**3
t = []
t = x1 = np.logspace(0.1, max_t, t_steps, endpoint=True)

cutOff = -6



def findCutOff(t, pts, look):
    for i in range(len(pts)):
        if(t[i] > look):
            print("(" + repr(t[i]) + ", " + repr(pts[i]) + " )")
            return



'''
Ideal Values:
High Pass: A = 0.25, H = 1, F = 20, k = 6.283185307179586e-07, q = 0
    c1 = 5 e-9
    c2 = 5 e-9
    c3 = 5 e-9
    r2 = 132629.11924324612
    r5 = 19098593.17102744
''



a_S = [0.01, 0.25, 0.5, 0.9, 1, 1.5, 2, 9, 15]
for i in range(len(a_S)):

    h =  1
a =  0.25


    
 FIN: f0, f1 = 28.25, 33 * 10**3  
'''
f0, f1 = 28.25, 33 * 10**3 # 200 * 10**3 
c1 = 5 * 10 **-9
c2 = 5 * 10 **-9

h =  1# 816.8 #1
a =  0.5# 649.98 # 0.25

high = MultiStage_High( f0, h, a, c1)

points_high = high.plot(t)
filterBuilder.printDetials(high)
findCutOff(t, points_high, 20)
plt.plot(t, points_high, label = '20 hz H: ' + repr(h)  + ", A: " + repr(a))

h =  816.8 #1
a =  649.98 # 0.25

low = MultiStage_Low(f1, h, a, c2)

points_low = low.plot(t)
filterBuilder.printDetials(low)
findCutOff(t, points_low, f1)
plt.plot(t, points_low, label = '20k hz H: ' + repr(h)  + ", A: " + repr(a))
    

###############################

plt.title("Magnitude Response " )
plt.xlabel("Hz")
plt.ylabel("Magnitude (dB)")

cutOff_ = []
cuttOff_t = []
for i in range(len(t)):
    if i % 10 == 0:
        cutOff_.append(cutOff)
        cuttOff_t.append(t[i])

plt.plot(cuttOff_t, cutOff_, 'r.', label = repr(cutOff_[0]))
plt.plot(20*10**3, max(points_high) -3, 'b.')
plt.plot(20, -3, 'b.')

plt.legend()
plt.show()
