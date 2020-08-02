def add(*argl):
  x = 0
  for arg in argl:
    try:
      for z in arg: #helps with lists
        x+=z
    except:
      x+=arg
  return x
def subtract(*args):
  x = 0
  for arg in args:
    x-=arg
  return x
def multiply(*args):
  x = 0
  for arg in args:
    x*=arg
  return x
def divide(*args):
  x = 0
  for arg in args:
    x/=arg
  return x

##These are mainly useless, but a demonstration of infinite argument taking
##functions.