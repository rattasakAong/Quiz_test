number = [1,2,31,4,15,6,7,22,9,10]
n = len(number)
max_number = number[0]
for i in range(1,n):
    if number[i] > max_number:
        max_number = number[i]

print(f"max number is {max_number}")