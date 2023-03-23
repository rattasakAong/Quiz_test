prime = []
for number in range(501):
    flag = True
    if number == 0 or number == 1:
        flag = False

    if flag:
        for i in prime:
            if number % i == 0:
                flag = False
                break
    if flag:
        prime.append(number)

print(f"result is {prime}")