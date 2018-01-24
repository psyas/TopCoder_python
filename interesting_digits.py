n = int(input())

def convertbase(n, current_val):
    result = list()
    remain = 100
    while current_val != 0:
        remain = current_val%n
        current_val = current_val//n
        result.append(remain)
    return result



result = list()

for left in range(int(n)):
    if left < 2:
        continue
    flag = True
    loop_count = 999//(left)
    for right in range(loop_count):
        current_val = (left)*(right+1)
        if (sum(convertbase(n,current_val))%left) != 0:
            flag = False
    if flag == True:
        result.append(left)

print(result)
        
