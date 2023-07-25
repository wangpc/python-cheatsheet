#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# author: ZJay
# 目的: 通过执行一个单一的文件, 在 15 分钟内讲解明白 python3 的基础语法知识
# 使用方法: `python3 ./run.py`

print("python3 学习中要注意的点")

# print 方法的若干参数中, 逗号分隔的参数中间会在打印的时候增加空格
print("100 + 200 =", 100 + 200)

# input 方法输入的时候, 参数后面的提示条件不会增加空格
# name = input("Please enter your name: ")
# print("Hello", name + ".")

# 缩进的形式是四个空格
a = 100
if a >= 10:
    print(a)
else:
    print(-a)
# end

# 三个单引号表示跨行字符串, r'' 表示后面的内容中的转义符不转义
print(r'''hello,\n
world''')
      
# python 中的 null 的表现形式为 None, 注意大写
print(None)

# ord 方法获取字符的整数表示
print(ord('中'))

# chr 方法从编码获取字符
print(chr(25991))

# 直接进行 unicode 的表示
print('\u4e2d\u6587')

# encode 方法获取原始编码 >>> b'ABC' str -> byte
'ABC'.encode('ascii')
# b'\xe4\xb8\xad\xe6\x96\x87'
'中文'.encode('utf-8')

# byte -> str
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') # >>> '中文'
b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore') # >>> '中'

# len 方法获取 str 对应的字符数
print('字符串 "ABC" 的长度是:', len('ABC'))

# len 方法获取 bytes 对象的字节数
print(r'字节码 (bytes) "\xe4\xb8\xad\xe6\x96\x87" 的字节数是:', len(b'\xe4\xb8\xad\xe6\x96\x87'))

# 字符串格式化
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# 或者使用 format 方法
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

# 或者使用 f-string
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

# list
# insert 方法插入
classmates = ['Tracy', 'Cuier']
classmates.insert(1, 'Nancy')
# pop 方法出栈 (尾部元素)
classmates.pop()
# pop 方法删除指定 index 的元素
classmates.pop(1)
# 替换元素直接赋值
classmates[0] = 'Tina'
# list 允许异构, 允许嵌套
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']

# tuple 元组: 定义后不可变
classmates = ('Michael', 'Bob', 'Tracy')


# dict

d = {
    "Micheal": 85, 
    "Bob": 91,
    "Lora": 78
}

if "Karen" in d:
    print("Here is Karen.")
else:
    print("No Karen here.")

print(d.get("Micheal", -1))

