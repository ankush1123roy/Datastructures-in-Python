import numpy
import sys
import math
def PIR(ar):
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
        Volume = math.sqrt(abs((numpy.linalg.det(Mat))/288))
        print "%.4f"%(Volume)


m = input()
ar = [];
i =0;
while i < m:
    K = raw_input()
    if K:
        ar.append(K);
        i = i + 1
    
PIR(ar)


From root Sun Sep 29 06:16:49 2013
Date: Sun, 29 Sep 2013 06:16:49 -0600
To: TESTankush1123roy@gmail.com
Subject: a
User-Agent: Heirloom mailx 12.5 6/20/10
MIME-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: quoted-printable

=

From root Sun Sep 29 06:18:12 2013
Date: Sun, 29 Sep 2013 06:18:12 -0600
To: ankush1123roy@gmail.com, Solution, the, Check
Subject: a
User-Agent: Heirloom mailx 12.5 6/20/10
MIME-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit

TEST EMAIL TO CHECK THE PYTHON CODE

