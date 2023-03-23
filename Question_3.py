number = [1,2,31,4,15,6,7,22,9,10]
n = len(number)
number_sort = []

print(f"ก่อนเรียงเลขจากน้อยไปมาก : {number}")

for i in range(n):
    for j in range(i+1,n):
        if number[i] > number[j]:
            temp = number[i]
            number[i] = number[j]
            number[j] = temp

for i in range(n):
    number_sort.append(number[i])

print(f"หลังเรียงเลขจากน้อยไปมาก : {number_sort}")


