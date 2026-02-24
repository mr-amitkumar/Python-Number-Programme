# A harshad number is a number which is divisible by its sum of its digits:

n = int(input("Enter the number: "))
sums = 0
temp = n 
while temp > 0:
    d = temp % 10
    sums += d
    temp //= 10

if n % sums == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")