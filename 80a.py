def decimalSum(x):
   xstr = str(x)
   total = 0
   for c in str(xstr)[0 : 101]:
      if c != ".":
         total += int(c)
   return total

from decimal import *
import math
getcontext().prec = 105
total = 0
for i in range(2,100):
   if pow(int(math.sqrt(i)), 2) != i:
      total += decimalSum(Decimal(i).sqrt())
   
print(total)
