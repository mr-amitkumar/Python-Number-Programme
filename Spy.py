#  A number whose sum is equal to it product is known as spy num

n = int(input("Enter the number:"))
temp = n
s = 0
p = 1
while temp > 0:
    d = temp % 10
    s += d
    p *= d
    temp //= 10

if s == p:
    print("Spy")
else:
    print("Not Spy")