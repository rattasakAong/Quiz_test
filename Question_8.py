binary = str(input("ป้อนเลขฐานสอง : "))
index = len(binary)
demical = 0

for i in binary:
    index -= 1
    if int(i) != 0:
        demical += 2**index
    
print(f"{binary} = {demical}")