class Trig:
  def __init__(self):
    self.pi = 3.1415926535897932384626433
    pass
  
  def factorial(num):
    if num < 2: return 1
    else: return num * factorial(num-1)
  
  def radians(self, num): return num*self.pi
  
  def degToRad(self, num): return num*(self.pi/180)
  
  def radToDeg(self, num): return num*(180/self.pi)
  
  def radiansRev(self, num): return num/self.pi

  def sin(self, num, deg=True, prec=2):
    def factorial(num):
      if num < 2: return 1
      else: return num * factorial(num-1)
    if deg == True: x = self.degToRad(num%360)
    else: x = num
    return round(x - float((x**3)/6)+float((x**5)/120)-float((x**7)/factorial(7))+((x**9)/factorial(9))-((x**11)/factorial(11))+((x**13)/factorial(13))-((x**15)/factorial(15))+((x**17)/factorial(17))-((x**19)/factorial(19))+((x**21)/factorial(21))-((x**23)/factorial(23))+((x**25)/factorial(25)), 2)

  def cos(self, num, deg=True, prec=2):
    if deg == True: return self.sin(90+num, prec=prec)
    else: return self.sin(self.pi/2+num ,deg=False, prec=prec)
    
  def tan(self, num, deg=True, prec=2):
    if num % 90 == 0 and num % 180 != 0:
      raise ZeroDivisionError("That's not quite allowed")
    if deg == True: return self.sin(num, prec)/self.cos(num, prec=prec)
    else: return self.sin(num, deg=False, prec=prec)/self.cos(num, deg=False, prec=prec)

  def csc(self, num, deg=True, prec=2):
    if deg==True: return 1/self.sin(num, prec=prec)
    else: return 1/self.sin(num, deg=False, prec=prec)

  def sec(self, num, deg=True, prec=2):
    if deg==True: return 1/self.cos(num, prec=prec)
    else: return 1/self.cos(num, deg=False, prec=prec)
  
  def cot(self, num, deg=True, prec=2):
    if deg==True: return 1/self.tan(num, prec=prec)
    else: return 1/self.tan(num, deg=False, prec=prec)

