# 这是一个随机抽取的小程序。
import random
print('欢迎来到对抗路！')
i = 1
while i < 100:
    i += 1
    my_list1 = []
    a = int(input('请收入本次抽取的人数。'))
    b = int(input('请输入总人数。 '))
    while len(my_list1) <= a-1:
         x = random.randint(1, b)
         if x not in my_list1:
             my_list1.append(x)
    mylist_2 = sorted(my_list1)
    print('抽取到的编号为：', mylist_2)