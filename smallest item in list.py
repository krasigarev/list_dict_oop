# Smallest Item in List

num = list(map(int, input().split(" ")))

print(min(num))

min_number = num[0]

for element in num:
    if element < min_number:
        min_number = element

print(min_number)

data_min = sorted(num)

print(data_min)

num.sort()

print(num)

sorted_num = sorted(num)

print(sorted_num)
print(num)