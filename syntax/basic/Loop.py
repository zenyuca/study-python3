# 循环

# for in 循环
sum = 0
for item in [1, 2, 3, 4, 5]:
  sum += item
print(sum)

count = 0
for i in range(100):
  count += (i + 1)
print(count)

# class range(stop)
# class range(start, stop[, step])
sum = 0
for x in range(10):
  sum += x
print(sum)

r = range(10, 20)   # 定义一个范围
print(1 in r)       # in 判断 1 是否在r中
print(r.index(11))  # 获取范围中11的下标

ls = list(range(10, 20, 2))   # 将范围转换成list（数组）
print(ls)       # [10, 12, 14, 16, 18]

# while 循环
count = 0
i = 0
while i < 100:
	count += i
	i += 1
print(count)
