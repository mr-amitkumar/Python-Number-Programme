# A number which is equal to the sum of it divisor is called perfect number

n = int(input("Enter the number: "))
sums = 0
for i in range(1,n):
    if n % i == 0:
        sums += i
    
if sums == n:
    print(n,"is perfect")
else:
    print(n,"is perfect")