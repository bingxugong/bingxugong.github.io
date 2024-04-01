from typing import Callable
from random import randint

class Event:
    def __init__(self, name: str):
        self.name = name

def event_handler(*events: Event) -> int:
    total = 0
    for event in events:
        a = randint(1, 100)
        print(a)
        total += a
    return total

# 使用 Callable 类型提示来声明一个可调用对象的类型
HandlerType: Callable[..., int] = event_handler

# 调用 HandlerType，即调用 event_handler 函数
event1 = Event("event1")
event2 = Event("event2")
result = HandlerType(event1, event2)
print(f"Handler returned: {result}")
