"""I need a function that takes the name of the movie to look up and
the width of the letter grid, and computes the key presses that
will enter that string on the DVR grid. The output should be a
string, with "u", "d", "l", "r", and "!" corresponding to up,
down, left, right, and select.

For example, with a grid of width 5,
a b c d e
f g h i j
k l m n o
p q r s t
u v w x y
z
the movie "up" would be "dddd!u!".
"""
from copy import deepcopy
def Remote(ar):
    Start  = 1
    for i in range(len(ar)):
        Char = ord(ar[i]) - ord('a') + 1
        QS, RS = Start/5, Start%5
        QN, RN = Char/5, Char%5
        K, L = 0,0 
        if (QN - QS) > 0: 
            K = 0 
            while K < QN - QS:
                print 'd',
                K += 1
        elif (QN - QS) < 0:
            K = 0 
            while K < abs(QN - QS):
                print 'u',
                K += 1
        else: 
            pass
        if (RN - RS) > 0:
            L = 0
            while L < RN - RS:
                print 'r',
                L += 1
        elif (RN - RS) < 0:
            L = 0
            while L < abs(RN - RS):
                print 'l',
                L +=1
        else:
            pass
        print '!',
        Start = deepcopy(Char)

Remote(list(raw_input('Enter the Movie name:  ')))
           
