def factorial(num):
    if num < 2: return 1
    else: return num * factorial(num-1)

def piradians(num): return 3.1415926535897932384626433*num

def degToRad(num): return num*(3.1415926535897932384626433/180)

def radToDeg(num): return num*(180/3.1415926535897932384626433)
  
def radiansRev(num): return num/3.1415926535897932384626433

def sin( num, deg=True, prec=2):
    if deg == True: x = degToRad(num%360)
    else: x = num
    return round(x - float((x**3)/6)+float((x**5)/120)-float((x**7)/factorial(7))+((x**9)/factorial(9))-((x**11)/factorial(11))+((x**13)/factorial(13))-((x**15)/factorial(15))+((x**17)/factorial(17))-((x**19)/factorial(19))+((x**21)/factorial(21))-((x**23)/factorial(23))+((x**25)/factorial(25)), 2)

def cos( num, deg=True, prec=2):
    if deg == True: return sin(90+num, prec=prec)
    else: return sin(3.1415926535897932384626433/2+num ,deg=False, prec=prec)
    
def tan( num, deg=True, prec=2):
    if num % 90 == 0 and num % 180 != 0:
      raise ZeroDivisionError("That's not quite allowed")
    if deg == True: return sin(num, True, prec)/cos(num, True, prec)
    else: return sin(num, prec, deg=False, )/cos(num, prec, deg=False)

def csc( num, deg=True, prec=2):
    if deg==True: return 1/sin(num, True, prec)
    else: return 1/sin(num, False, prec)

def sec( num, deg=True, prec=2):
    if deg==True: return 1/cos(num, True, prec)
    else: return 1/cos(num, False, prec)
  
def cot( num, deg=True, prec=2):
    if deg==True: return 1/tan(num, True, prec)
    else: return 1/tan(num, False, prec)
