import numpy
import sys
import math
from numpy import matrix as MA
import sys

def TETRA(ar):
    for i in range(len(ar)):
        Dist = ar[i].split()
        AB,AC = int(Dist[0]), int(Dist [1])
        AD,BC = int(Dist[2]), int(Dist[3])
        BD,CD = int(Dist[4]), int(Dist[5])
        M1 = [0, 1, 1, 1, 1];
        M2 = [1,0, AB**2,AC**2,AD**2]
        M3 = [1,AB**2,0,BC**2,BD**2]
        M4 = [1,AC**2,BC**2,0,CD**2]
        M5 = [1,AD**2,BD**2,CD**2,0]
        Mat = [M1,M2,M3,M4,M5]
        Volume = math.sqrt((numpy.linalg.det(Mat))/288)
        S1,S2,S3,S4 = SurfaceArea(AB,BC,AC), SurfaceArea(AD,BD,AB),SurfaceArea(AC,CD,AD),SurfaceArea(BD,CD,BC)
        radius = (3*Volume)/(S1+S2+S3+S4)
        print "%.4f"%(radius)

def SurfaceArea(A,B,C):
    S = (A + B + C)/float(2);
    No = S* (S-A)*(S-B)*(S-C)
    SArea = math.sqrt(No);
    return SArea

m = input()
ar = [];
i =0;
for i in range(m):
    ar.append(raw_input())
TETRA(ar)

