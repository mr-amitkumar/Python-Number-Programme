# When a prime number is reversed and then reverse number is a also prime it is called emrip number which is reverse of prime.


def prime(n):
    if n > 1:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True
    return  False

def Emrip(n):
    rev = int(str(n)[::-1])
    
    if prime(n) and rev != n and prime(rev):
        return True
    return False

n = int(input("Enter the number: "))
if Emrip(n):
    print("Emrip")
else:
    print("Not Emrip")