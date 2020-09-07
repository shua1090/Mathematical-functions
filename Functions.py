def factorial(num):
  if num < 2:
    return 1
  else:
    return num * factorial(num-1)

def sqrt(num):
  return num**(1/2)

def nroot(num, n=2):
  return num**(1/n)

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