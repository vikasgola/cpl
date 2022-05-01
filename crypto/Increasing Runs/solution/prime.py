# Python program to display all the prime numbers within an interval
lower = 1
upper = 500

# print("Prime numbers between", lower, "and", upper, "are:")

count = 0
primes= []
for num in range(1,500):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
        #    print(num,end="")
           primes.append(num)
           count+=1
           if count == 50 : break
print(primes)
print(len(primes))