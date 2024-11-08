from math import *
import numpy

frames = 1000

class Link:	

        def __init__(self, T):
                self.T = T
                self.len = None
                self.root = None
                self.Ts = numpy.linspace(0, 2 * pi, num=frames)
                self.x = numpy.linspace(0, 2 * pi, num=frames)
                self.y = numpy.linspace(0, 2 * pi, num=frames)
                self.motion = None # crank, rock, slide, fixed

        def __eq__(self, other):
                return self.T == other.T


        



l1 = Link(1)
l2 = Link(2)
l3 = Link(3)
l4 = Link(4)

links = [l1, l2, l3, l4]




def tog(a, b, c, d, Tc):
    if Tc == 2:
        Tta = acos((a**2 + d**2 - b**2 - c**2) / (2 * a * d) + (b * c) / (a * d))
        Ttb = acos((a**2 + d**2 - b**2 - c**2) / (2 * a * d) - (b * c) / (a * d))
    elif Tc == 4:
        # replace a with c
        Tta = acos((c**2 + d**2 - b**2 - a**2) / (2 * c * d) + (b * a) / (c * d))
        Ttb = acos((c**2 + d**2 - b**2 - a**2) / (2 * c * d) - (b * a) / (c * d))

    assert(Tc != 3)

    return Tta, Ttb


def grashof(a, b, c, d, Tcf=None):

        #a = l2.len
        #b = l3.len
        #c = l4.len
        #d = l1.len

        s = min(a, b, c, d)
        l = max(a, b, c, d)

        # determine p
        p = None
        if s != a and l != a:
                p = a
        elif s != b and l != b:
                p = b
        elif s != c and l != c:
                p = c
        elif s != d and l != d:
                p = d

        # determine q
        q = None
        if s != a and l != a and p != a:
                q = a
        if s != b and l != b and p != b:
                q = b
        if s != c and l != c and p != c:
                q = c
        if s != d and l != d and p != d:
                q = d

        if (s + l) < (p + q):
                typ = 'Grashof'
                #print('Grashof')
        elif (s + l) > (p + q):
                typ = 'non-Grashof'
                #print('non-Grashof')
        else:
                typ = 'Special'
                #print('Special')
        
        # determine code
        if s == d: # s = ground
                code = 'GCCC'
                Tc = 2
                l1.motion = 'fixed'
                l2.motion = 'crank'
                l3.motion = 'crank'
                l4.motion = 'crank'
                #print('GCCC')
        elif s == a: # s = input
                code = 'GCRR'
                Tc = 2
                l1.motion = 'fixed'
                l2.motion = 'crank'
                l3.motion = 'rock'
                l4.motion = 'rock'
                #print('GCRR')
        elif s == b: # s = coupler
                code = 'GRCR'
                Tc = 3
                l1.motion = 'fixed'
                l2.motion = 'rock'
                l3.motion = 'crank'
                l4.motion = 'rock'
                #print('GRCR')
        elif s == c: # s = output
                code = 'GRRC'
                Tc = 4
                l1.motion = 'fixed'
                l2.motion = 'rock'
                l3.motion = 'rock'
                l4.motion = 'crank'
                #print('GRRC')

        if Tcf != None:
                Tc = Tcf


        if code == 'GRCR':
                if Tc != 3:
                        Tta, Ttb = tog(l2.len, l3.len, l4.len, l1.len, Tc)
                        Ta = numpy.linspace(Tta+0.0001, Ttb-0.0001, num=int(frames/2))
                        Tb = numpy.linspace(Ttb-0.0001, Tta+0.0001, num=int(frames/2))
                        if Tc == 2:
                                l2.Ts = numpy.concatenate([Ta, Tb])
                        if Tc == 4:
                                l4.Ts = numpy.concatenate([Ta, Tb])
        elif code == 'GCRR':
                if Tc != 2:
                        Tta, Ttb = tog(l2.len, l3.len, l4.len, l1.len, Tc)
                        Ta = numpy.linspace(Tta+0.0001, Ttb-0.0001, num=int(frames/2))
                        Tb = numpy.linspace(Ttb-0.0001, Tta+0.0001, num=int(frames/2))
                        if Tc == 3:
                                l3.Ts = numpy.concatenate([Ta, Tb])
                        if Tc == 4:
                                l4.Ts = numpy.concatenate([Ta, Tb])
        elif code == 'GRRC':
                if Tc != 4:
                        Tta, Ttb = tog(l2.len, l3.len, l4.len, l1.len, Tc)
                        Ta = numpy.linspace(Tta+0.0001, Ttb-0.0001, num=int(frames/2))
                        Tb = numpy.linspace(Ttb-0.0001, Tta+0.0001, num=int(frames/2))
                        if Tc == 2:
                                l2.Ts = numpy.concatenate([Ta, Tb])
                        if Tc == 3:
                                l3.Ts = numpy.concatenate([Ta, Tb])
                
                

         


        return Tc, typ, code
