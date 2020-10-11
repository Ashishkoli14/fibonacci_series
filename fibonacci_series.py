n = int(input("How many terms? "))#number of terms

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if n <= 0:#to check the number is positive or not
   print("Please enter a positive integer")
elif n == 1:#if the no. entered is 1 then the series will be only 1 number "0" which is n1=0
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:#logic to print fibonacci series
       print(n1)
       nth = n1 + n2#nth value is addition of numbers
       # updating values
       n1 = n2
       n2 = nth
       count += 1
