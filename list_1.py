# temperature = [20, 21, 20, 25, "Hi"]
#
# for temp in temperature:
#     print(temp)
#
# for index in range(len(temperature)):
#     print(temperature[index])


# Multiply a List of Integers version 1

# data_list = input().split(" ")
# p = int(input())
#
# numbers_list = []
#
# for el in data_list:
#     numbers_list.append(int(el) * p)
#
# print(data_list)
# print(numbers_list)


# Multiply a List of Integers version 2

data_list_1 = list(map(int, input().split(" ")))
p = int(input())

a = 4 * data_list_1
print(a)
