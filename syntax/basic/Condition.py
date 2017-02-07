# 条件
age = 10
if age >= 18:
  print('你的年纪是：', age)
  print('你已经成年！')
elif age >= 6:
  print('还是个孩子')
else:
  print('幼儿')

str = input('生日：')
age = int(str)    # 将string转换成数字
if age < 1949:
  print('解放前')
elif age < 1990:
  print('80前')
elif age < 2000:
  print('90后')
else:
  print('00后')
