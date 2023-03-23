number = int(input("Enter your number: "))
n = number
fac = 1
for i in range(1, n+1):
    fac *= i
print(f"{number}! is {fac} ")