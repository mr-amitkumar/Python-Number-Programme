# A Desarium number is a number where the sum of its digits raised to the power of their respective positions is equal to that number


n = int(input("Enter the number: "))
sums = 0
s = str(n)
for i in range(len(s)):
        d = int(s[i])
        p = i + 1
        sums += d ** p
        
if sums == n:
    print("Desarium")
else:
    print("Not Desarium")