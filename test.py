import random

list = [random.randint(1,9) for i in range(10)]
print(list)

index = 0
for i in range(len(list)):
    if index >= list[i+1]:
        list[index], list[i+1] = list[i+1], list[index]
    else:
        index += 1

print(list)