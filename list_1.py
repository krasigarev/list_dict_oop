# temperature = [20, 21, 20, 25, "Hi"]
#
# for temp in temperature:
#     print(temp)
#
# for index in range(len(temperature)):
#     print(temperature[index])


# Multiply a List of Integers

data_list = input().split(" ")
p = int(input())

numbers_list = []

for el in data_list:
    numbers_list.append(int(el) * p)

print(data_list)
print(numbers_list)