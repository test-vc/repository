# test program for GitHub and Travis.CI

def fibonacci():
    # test program for generating a fibonacci series
    a,b=0,1
    while a<100:
        print(a, end="_")
        a,b=b, a+b

     # notes to print:
     # r before the string (e.g. print(r"Szia!\n") ignores the meaning of special characters
     # with """ in the string, it can go over multiple lines. With """\ the start and end return are ignored
     # the argument end="adsf" can change the end sign of the print (instead of \n)

def unit_step():
    # module to create a unit step input signal

    def u(n):
        if n >= 0:
            return 1
        else:
            return 0


def rad_to_deg():
    # Wir brauchen die Zahl pi von der Library "math"
    from math import pi

    rad = float(input("Winkel in Bogenmass eingeben: "))
    deg = rad*180.0/pi
    grad = int(deg)
    bogenmin = int((deg - grad)*60)
    bogenmin = ((deg - grad)*60 - bogenmin)*60
    print(rad, " rad = ", grad, "°", bogenmin, "'", bogenmin, "\"", sep = "")
