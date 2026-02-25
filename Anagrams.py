# Two numbers are anagrams if they contain the same digits but arranged in a different order.

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter second number: "))

if sorted(str(n1)) == sorted(str(n2)):
    print("anagrams")
else:
    print('not anagrams')