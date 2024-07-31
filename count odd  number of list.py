# count number odd of list

nums = list(map(int, input().split(" ")))

counter = 0

for num in nums:
    if not num % 2 == 0:
        counter += 1

print(counter)

odd_nums_list = len([element for element in nums if element % 2 == 1])
print(odd_nums_list)

print([element for element in nums if element % 2 == 1])

print(len([element for element in list(map(int, input().split(" "))) if element % 2 == 1]))

