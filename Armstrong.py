# Armstrong number is a number whose sum of its own digits raised to the power of the number of digits given by

n = int(input("Enter the number: "))
temp = n
s = len(str(n))
sums = 0
while temp > 0:
    d = temp % 10
    sums += d ** s
    temp //= 10
if sums == n:
    print("Armstrong")
else:
    print("Not Armstrong")

 