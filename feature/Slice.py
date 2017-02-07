# 切片
# class slice(start, stop[, step]) 类似于 range(start, stop, step)
R = list(range(50))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])

t = (1, 2, 3, 4, 5)
print('t', t)
print('t[1:3]', t[1:3])
print('t[::2]', t[::2])
