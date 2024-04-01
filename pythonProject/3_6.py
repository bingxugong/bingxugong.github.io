from collections import defaultdict

# 创建一个默认值为空列表的defaultdict
d = defaultdict(list)

# 归类单词到以相同首字母为键的列表中
words = ['apple', 'banana', 'bear', 'cat', 'dog']
for word in words:
    d[word[0]].append(word)

print(d)  # 输出：defaultdict(<class 'list'>, {'a': ['apple'], 'b': ['banana', 'bear'], 'c': ['cat'], 'd': ['dog']})
