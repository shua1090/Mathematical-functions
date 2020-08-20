def factorial(num):
  if num < 2:
    return 1
  else:
    return num * factorial(num-1)

def sqrt(num):
  return num**(1/2)

def nroot(num, n=2):
  return num**(1/n)

def sin(num, deg=True):
  if deg == True:
    x = 3.1415926535897932384626433
    x = num*(x/180)
    return round(x - float((x**3)/6)+float((x**5)/120)-float((x**7)/factorial(7))+((x**9)/factorial(9))-((x**11)/factorial(11))+((x**13)/factorial(13))-((x**15)/factorial(15))+((x**17)/factorial(17))-((x**19)/factorial(19))+((x**21)/factorial(21))-((x**23)/factorial(23))+((x**25)/factorial(25)), 7)

def cos(num, deg=True):
  if deg == True:
    return sin(90-num)

def tan(num, deg=True):
  if num % 90 == 0 and num % 180 != 0:
    return "1/0 (undefined)"
  if deg == True: return sin(num)/cos(num)

##Dataset Calculations##
def SD(dataset):
  if isinstance(dataset, list):
    import Operations
  else:
    x = type(dataset)
    print("You have placed a ", x, " as the argument instead of a list. Please convert the argument into a list or use the String to list function.")
    raise TypeError
  y=mean(dataset)
  return (Operations.add([(k-y)**2 for k in dataset])/len(dataset))**(1/2)

def median(nums):
  nums = nums.strtolst()
  nums.sort()
  if (len(nums)/2)%2==0 or (len(nums)/2)%2==1:
    return (nums[(len(nums)//2)-1]+nums[(len(nums)//2)])/2
  else:
    return nums[int(len(nums)/2)]

def mean(arg):
  from TextEditing import strtolst
  arg = strtolst(arg)
  import Operations
  return Operations.add(arg) / len(arg)

def ranged(arg):
  from TextEditing import strtolst
  arg = strtolst(arg)
  print(arg)
  arg.sort()
  return arg[-1]-arg[0]