number = [1,2,31,4,15,6,7,22,9,10]
n = len(number)
min_number = number[0]
for i in range(1,n):
    if number[i] < min_number:
        min_number = number[i]

print(f"min number is {min_number}")