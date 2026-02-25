# A palindrome number is a number that remians  the same when read foreward and backward

n = int(input("Enter the number : "))
temp = n
rev = 0
while temp > 0:
    d = temp % 10
    rev = rev * 10 + d
    temp //= 10
    
if rev == n:
    print("Palindrome")
else:
    print("not palindrome")