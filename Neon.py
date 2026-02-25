# A number whose square is equal to it number is known as neon number

n = int(input("Enter the number: "))
sq = n ** n
temp = n
s = 0
while n > 0 :
    d = n % 10
    s += d
    n //= 10

if s == temp:
    print("Neon") 
else:
    print("Not neon")