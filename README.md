# Mathematical-functions
These few python files contain some interesting mathematical functions. Many of these functions aren't availible in normal python. 
The main.py file is to test the usability of importing the functions. Some of these functions can be used for data calculations, such as
the standard deviation calculator. Other functions are quite arbitary but do have some uses; These functions, like the add function, are very similar
to builtin functions. The difference between the add function and the sum function is that the sum function takes in 2 arguments while add takes in as many as you like:

```python
def add(*argl):
  x = 0
  for arg in argl:
    try:
      for z in arg: #Can add all the values in a list
        x+=z
    except: #Normal adding all arguments
      x+=arg
  return x
```

Another useful function can be found in the TextEditing section. While the TextEditing section is quite small, the "strtonumlst" is quite useful in that it takes in a 
string list and converts it into a normal list of integers or floats:
```python
def strtonumlst(arg1, prec=True):
  if isinstance(arg1, list):
    return arg1
  if ',' in arg1:
    arg1 = arg1.split(',') 
  else:
    arg1 = arg1.split(' ')
  if prec == True: listnums = [float(num) for num in arg1]
  else: listnums = [int(num) for num in arg1] 
  return listnums
  ```
  
  While many of these functions are interesting, they are all availible in the builtin math module. I created this as a side project for fun, as a psuedo-replacement for the
  math module. This entire "module" will not now, nor ever, import any other modules. It will exhibit simple, or sometimes partially complex, calculation functions for use 
  within a program. The point is, with this, you don't need to import the math module or any other modules. Copy-paste the code, calculate some standard deviations, and
  good luck to future programming!
  
  
Graphing section has been added, it has been implemented through Matplotlib. To set it up, follow:
```python
from Graph import graph

line = graph("x**2") #Everything is in terms of x, so this is actually: y=x**2
line.display() #Displays the actual graph
```

Trigonometric functions section has been added. The Sine function has been implemented through a Taylor's series to the 23rd degree. The remaining functions were built off of the
Sine function. Here are the uses:
```python
from Trig import *

print(sin(90)) #prints 1.0

print(cos(90)) #prints 0.0

print(tan(45)) #prints 1.0

print(piradians(1)) #prints 3.1415... (1 pi radians)

print(radiansRev(3.1415)) #prints ~1

print(degToRad(180)) #prints pi (180 degrees is pi radians)
#etc...
#Note, the Taylor's series is calculated with each run, so it may be a bit slow for now
```