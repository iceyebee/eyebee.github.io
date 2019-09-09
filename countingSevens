import math

def f(n):
   i = 0
   value = 0
   if n<1:
       negErrorString = 'Not a positive integer.'
       return negErrorString
   else:
       while i <= (math.log10(n)):
           if n%10**(i+1) < 7*10**i:
               value+= i*10**(i-1)*int(n%10**(i+1)/10**i)
           elif n%10**(i+1) >= 8*10**i:
               value+= i*10**(i-1)*(int(n%10**(i+1)/10**i)-1)+10**i
           else:
               value+= n%10**i+1+7*i*10**(i-1)
           i += 1
       return int(value)

print("Counting 7's--")
cont = 'y'
while cont == 'y':
   while True:
       try:
           numString = input("Please enter a number (greater than 1): ")
           num = int(numString)
           break
       except ValueError:
           print("Not an integer.")
   print(f(num))
   cont = raw_input("Would you like to continue? (Press y to continue; any other key to stop) ")
