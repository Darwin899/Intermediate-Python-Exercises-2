import time
def fib(n):
   # starting time
   startt = time.time() 
   fi = [0] * (n+1) 
   fi[1] = 1
   for i in range (2,n+1): 
      fi[i] = fi[i-1] + fi[i-2] 
   # ending time
   endt = time.time() 
   executiontime = endt - startt
   return fi[n], executiontime
   
fibvalue,executiontime=fib(34)
# prints the fibvalue & executiontime
print("fib value: ",fibvalue, end='\n')
print("execution time: ",executiontime)
