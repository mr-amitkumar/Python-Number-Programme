# The Fibonacci series is a sequence of numbers where each number is the sum of the two previous numbers.

n = int(input("Enter the no of terms: "))
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a, b = b, c