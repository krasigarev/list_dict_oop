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

list_2 = ["one", "two", "three", "four", "five", "six"]

for i in list_2:
    print(i)

print("; ".join(list_2))

values = input()
items = values.split(' ')
nums_1 = []
for i in items:
    nums_1 += [int(i)]   # or nums.append(int(i))

print(nums_1)

num_2 = [int(item) for item in input(" ").split()]
print(num_2)
