# 递归操作
def recur (n):
  if n == 1:
    return 1
  return n * recur(n - 1)

result = recur(5)
print(result)

result = recur(100)
print(result)
