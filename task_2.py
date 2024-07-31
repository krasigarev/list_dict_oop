nums = list(map(int, input().split(" ")))

positive_nums = list(filter(lambda x: x >= 0, nums))

print(positive_nums)

