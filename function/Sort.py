# 排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？
# 直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

ls = [-1, 0, -2, 3, 1]
print(sorted(ls))         # => [-2, -1, 0, 1, 3]

ls = ['abc', '04444', '-21', '0s']
print(sorted(ls))         # => ['-2', '0', '0', 'abc']
print(sorted(ls, key = len))                    # => ['0s', 'abc', '-21', '04444']
print(sorted(ls, reverse = True, key = len))    # => ['04444', 'abc', '-21', '0s']


# key 指定排序算法
ls = [-1, 0, -2, 3, 1]
print(sorted(ls, key = abs))         # => [0, -1, 1, -2, 3]
