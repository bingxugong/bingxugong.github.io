from collections import defaultdict

# 创建一个默认值为0的defaultdict
d = defaultdict(int)

# 统计列表中元素出现的次数
my_list = ['a', 'b', 'c', 'a', 'b', 'a']
for item in my_list:
    d[item] += 1

print(d)  # 输出：defaultdict(<class 'int'>, {'a': 3, 'b': 2, 'c': 1})
