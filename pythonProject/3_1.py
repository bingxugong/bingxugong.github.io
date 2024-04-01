from typing import Callable

class Event:
    def __init__(self, name: str):
        self.name = name

def event_handler(event: Event) -> None:
    print(f"Handling event: {event.name}")

# 使用 HandlerType 类型提示来声明一个函数类型的变量
HandlerType: Callable[[Event], None] = event_handler

# 调用变量 HandlerType，即调用 event_handler 函数
event = Event("example_event")
HandlerType(event)
