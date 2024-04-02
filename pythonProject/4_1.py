from collections import defaultdict

# 创建一个defaultdict实例，指定默认值为int类型的0
my_dict = defaultdict(int)

# 在defaultdict中使用键"apple"并增加其值
my_dict['apple'] += 1

# 打印结果
print(my_dict)  # 输出：defaultdict(<class 'int'>, {'apple': 1})

a = my_dict['banana']
print(a) #输出： 0


# 创建一个defaultdict实例，指定默认值为list类型的空列表
my_dict2 = defaultdict(list)

# 向defaultdict中添加值
my_dict2['fruits'].append('apple')
my_dict2['fruits'].append('banana')
my_dict2['fruits'].append('cherry')

my_dict2['colors'].append('red')
my_dict2['colors'].append('blue')

# 打印结果
print(my_dict2)  # 输出：defaultdict(<class 'list'>, {'fruits': ['apple', 'banana', 'cherry'], 'colors': ['red', 'blue']})

list1 = my_dict['size']
print(list) #输出： <class 'list'>
if list1:
    print('1')
else:
    print('0')
#输出  0

list2 = my_dict2['colors']
if list2:
    print('1')
else:
    print('0')
#输出  1

my_dict2.pop('fruits')
print(my_dict2)
#用pop删除了key ='fruits'的键值对，
#输出 defaultdict(<class 'list'>, {'colors': ['red', 'blue']})