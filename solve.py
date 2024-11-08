from math import *
from link import links, l1, l2, l3, l4
import numpy


class Solver:

        def __init__(self, Tc, slider, backslider):
                self.alpha = None
                self.beta = None
                self.gamma = None
                self.a = None
                self.b = None
                self.c = None
                self.d = None
                self.mu = []
                self.muf = []
                self.alphabeta(Tc)
                self.slider = slider
                self.backslider = backslider
                
        
        def alphabeta(self, Tc):
                self.d = l1.len

                for link in links:
                        if link != l1 and link.T == Tc:
                                self.alpha = link
                                self.a = link.len
                                break
                        
                for link in links:
                        if link != l1 and link != self.alpha:
                                self.beta = link
                                self.b = link.len
                                break

                for link in links:
                        if link != l1 and link != self.alpha and link != self.beta:
                                self.gamma = link
                                self.c = link.len
                                break

                #print (self.alpha.T, self.beta.T, self.gamma.T)


        def K(self):

                a = self.a
                b = self.b
                c = self.c
                d = self.d

                K1 = d / a
                K2 = d / b
                K3 = (c**2 - a**2 - b**2 - d**2) / (2 * a * b)
                K4 = d / c
                K5 = (b**2 - c**2 - a**2 - d**2) / (2 * a * c)

                return [K1, K2, K3, K4, K5]


        def A(self, T, K1, K2, K3, K4, K5):

                A = cos(T) - K1 + K2 * cos(T) + K3
                B = -2 * sin(T)
                C = K1 + (K2 - 1) * cos(T) + K3
                D = cos(T) - K1 + K4 * cos(T) + K5
                E = -2 * sin(T)
                F = K1 + (K4 - 1) * cos(T) + K5

                return [A, B, C, D, E, F]


        def absT(self, T):
                if T < 0:
                        T = 2 * pi + T
                return T
        

        def get_angles_2(self, i):
                a = self.a
                b = self.b
                c = self.c

                T2 = self.alpha.Ts[i]
                T4 = self.gamma.Ts[i]

                T3 = asin((-c * sin(T4) - a * sin(T2)) / b)
                #print((-c * sin(T4) - a * sin(T2)) / b)
                #print(a, b, c, sin(T4), cos(T2))
                #assert(False)
                d = a * cos(T2) + b * cos(T3) + c * cos(T4)

                return T3, d


        def get_angles_3(self, i, d):
                a = links[1].len
                b = links[2].len
                c = links[3].len

                K1 = b**2 - a**2 - c**2 - d**2
                K2 = -2 * a * c
                K3 = 2 * a * d

                A = K1 - K3
                B = 2 * K2
                C = K1 + K3

                print(a, b, c, d)

                T2 = 2 * atan2((-B - sqrt(B**2 - 4 * A * C)) , (2 * A))
                T2_closed = 2 * atan2((-B + sqrt(B**2 - 4 * A * C)) , (2 * A))
                
                T3 = asin((-c - a * sin(T2)) / b)

                return T2, T3


        def get_angles(self, A, B, C, D, E, F):

                Tbeta = 2 * atan2((-B - sqrt(B**2 - 4 * A * C)) , (2 * A))
                Tbeta_closed = 2 * atan2((-B + sqrt(B**2 - 4 * A * C)) , (2 * A))

                Tgamma = 2 * atan2((-E - sqrt(E**2 - 4 * D * F)) , (2 * D))
                Tgamma_closed = 2 * atan2((-E + sqrt(E**2 - 4 * D * F)) , (2 * D))

                Tgamma = 3 * pi / 2
                Tgamma_closed = 3 * pi / 2

                #print(Tbeta_closed, Tgamma)

                #if Tbeta < 0:
                #    Tbeta = 2 * pi + Tbeta
                #if Tbeta_closed < 0:
                #    Tbeta_closed = 2 * pi + Tbeta_closed
                #if Tgamma < 0:
                #    Tgamma = 2 * pi + Tgamma
                #if Tgamma_closed < 0:
                #    Tgamma_closed = 2 * pi + Tgamma_closed

                #Tbeta = self.absT(Tbeta)
                #Tbeta_closed = self.absT(Tbeta_closed)
                #Tgamma = self.absT(Tgamma)
                #Tgamma_closed = self.absT(Tgamma_closed)
               
                
                

                #return Tbeta, Tgamma
                #return Tbeta_closed, Tgamma
                return Tbeta, Tgamma_closed
                #return Tbeta_closed, Tgamma_closed


        def coor(self, i):

                l1.x[i] = 0
                l1.y[i] = 0

                for l in range(1, len(links)):
                        link = links[l]
                        link.x[i] = links[l-1].x[i] + link.len * cos(link.Ts[i])
                        link.y[i] = links[l-1].y[i] + link.len * sin(link.Ts[i])
                        
                #assert(abs(l4.x[i] - l1.len) < 0.1)
                assert(abs(l4.y[i] - 0) < 0.1)


        def gen(self):

                imin = None
                imax = None
                mumin = 999
                mumax = -999

                xx = numpy.linspace(80, 158, num=int(1000/2))
                yy = numpy.linspace(158, 80, num=int(1000/2))

                x = numpy.concatenate([xx, yy])

                #for i, T in enumerate(self.alpha.Ts):
                for i, T in enumerate(x):

                        if self.backslider:
                            links[3].Ts[i] = pi / 2
                            Tbeta, Tgamma = self.get_angles_3(i, T)
                            links[1].Ts[i] = Tbeta
                            links[2].Ts[i] = Tgamma

                            self.coor(i)
                        elif self.slider:
                            self.gamma.Ts[i] = pi / 2
                            Tbeta, dd = self.get_angles_2(i)
                            self.beta.Ts[i] = Tbeta
                            self.gamma.Ts[i] = Tgamma

                            self.coor(i)
                        else:
                            Ks = self.K()
                            As = self.A(T, *Ks)

                            Tbeta, Tgamma = self.get_angles(*As)
                            self.beta.Ts[i] = Tbeta
                            self.gamma.Ts[i] = Tgamma

                            self.coor(i)

                        mu = self.toggles(i)
                        #print(Tbeta, Tgamma, mu)
                        if mu < mumin:
                                mumin = mu
                                imin = i
                        if mu > mumax:
                                mumax = mu
                                imax = i

                self.mu = [mumin, mumax]
                print(mumin, mumax)
                self.muf = [imin, imax]

        def toggles(self, i):

                #Tt = abs(self.beta.Ts[i] - self.gamma.Ts[i])
                Tt = (self.beta.Ts[i] - self.gamma.Ts[i])
                mu = Tt
                mu = mu / pi
                mu = abs(abs(mu) - pi)

                #if Tt > pi/2:
                #if Tt > pi:
                        #mu = pi - Tt

                #print(self.alpha.Ts[i], self.beta.Ts[i], self.gamma.Ts[i])
                
                #v2 = [self.beta.x[i] - self.alpha.x[i], self.beta.y[i] - self.alpha.y[i]]
                #v3 = [self.gamma.x[i] - self.beta.x[i], self.gamma.y[i] - self.beta.y[i]]
                
                #v2 = [xa, ya]
		#v3 = [xb-xa, yb-ya]
		#v4 = [xb-xc, yb-yc]

                #cp = numpy.cross(v3, v2)

                #if abs(cp) < 3:
                        #print('toggle detected at frame', i)
			#self.toggle.append(frame)

                return mu



      
