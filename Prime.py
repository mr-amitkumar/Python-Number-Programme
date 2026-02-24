# A prime number is a number that is greater then 1 and it can divisble by 1 and itself.

n = int(input("Enter the number: "))

if n > 1:
     for i in range(2 , n // 2 + 1):
         if n % i == 0:
             print('Not a prime')
     else:
        print("Is a prime")
else:
    print("Not a prime")