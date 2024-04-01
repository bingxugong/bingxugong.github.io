from typing import Callable
from random import randint

class Event:
    def __init__(self, name: str):
        self.name = name

def event_handler(event: Event) -> int:
    return randint(1, 100)

# 使用 Callable 类型提示来声明一个可调用对象的类型
HandlerType: Callable[[Event], int] = event_handler

# 调用 HandlerType，即调用 event_handler 函数
event = Event("example_event")
result = HandlerType(event)
print(f"Handler returned: {result}")
