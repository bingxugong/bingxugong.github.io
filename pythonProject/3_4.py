a: int = 3

if isinstance(a, int):
    print("a确实是int类型")
else:
    print("a不是int类型")

b: int = 3.0
if isinstance(b, int):
    print("b确实是int类型")
else:
    print("b不是int类型")
# 在Python中，类型注释（type annotations）仅仅是一种标记，
# 它并不会在运行时进行类型检查或强制类型转换。
# 因此，当您使用a: int = 3.0时，虽然使用了类型注释来声明a为int类型，
# 但实际上a的值仍然是3.0，即浮点数类型，而不会被强制转换为整数类型。
#
# 要进行强制类型转换，您需要显式地使用类型转换函数，例如int()函数来将浮点数转换为整数，如下所示：

c: int = int(3.0)
if isinstance(c, int):
    print("c确实是int类型")
else:
    print("c不是int类型")
