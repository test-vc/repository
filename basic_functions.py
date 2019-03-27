# module to create a unit step input signal

def u(n): # unit step function
    if n>=0:
        return 1
    else:
        return 0

def dirac(n): # dirac impulse function
    if n==0:
        return 1
    else:
        return 0

def v(n):   # velocity step function
    if n>=0:
        return n
    else:
        return 0
