#!/usr/bin/python

def T(n):
    return ( n * (n + 1) ) / 2
def P(n):
    return ( n * ((3 *n) - 1) ) / 2
def H(n):
    return ( n * ((2 * n) - 1) )

count = 0

T_ind = 285
P_ind = 165
H_ind = 144
T_val = T(T_ind)
P_val = P(P_ind)
H_val = H(H_ind)
line = H_val
count = 0

while True:
    while T_val < line:
        T_ind += 1
        T_val = T(T_ind)
    if T_val > line: #overshot it
        line = T_val
        count = 1
    else: # landed on it
        count += 1
    while P_val < line:
        P_ind += 1
        P_val = P(P_ind)
    if P_val > line: #overshot it
        line = P_val
        count = 1
    else: # landed on it
        count += 1
    while H_val < line:
        H_ind += 1
        H_val = H(H_ind)
    if H_val > line: #overshot it
        line = H_val
        count = 1
    else: # landed on it
        count += 1
    if count >= 3:
        print T_val, P_val, H_val
        print T_ind, P_ind, H_ind
        print 'ANSWER = ', T_val
        break




        
    


    


