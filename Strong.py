# A number in which the sum of its factorial of its digits is equal to the original number.

n = int(input("Enter the number: "))
sums = 0
temp = n
while temp > 0:
    d = temp % 10
    fact = 1
    for i in range(1,d+1):
        fact *= i
    sums += fact
    temp //= 10

if sums == n:
    print("strong")
else:
    print("not strong")