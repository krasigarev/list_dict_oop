# rotate List of strings

data_str = input().split(" ")

print(data_str[-1], end=" ")
print(*data_str[:-1])

last_element = data_str.pop()
data_str.insert(0, last_element)

print(*data_str)
