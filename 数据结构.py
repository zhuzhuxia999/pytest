

student = {"作者zhzuhuxia","长得还行","就是个子不高"}

print(student)

if '长得还行' in student :
    print('艾玛，老帅了')
if '并不好看' in student :
    print('怎么可能呢')

#set 可以进行集合运算
a = set('123456')
b = set('23456')

print(a)
print('差集',a - b)
print('并集',a | b)
print('交集',a & b)
print('两个集合中不同时存在的元素',a ^ b)


c = {"name":"猪猪侠","id":"1"}
print(c)
name = '这是我的name'
print(f'hello {name}')
print(f'1+2')
print(f'{1+2}')

print('斐波那契数列**************')
a , b = 0 , 1
while b < 10:
    print(b)
    a , b = b , a+b