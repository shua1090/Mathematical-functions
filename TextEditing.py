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