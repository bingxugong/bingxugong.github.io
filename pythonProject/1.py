from dataclasses import dataclass, field

@dataclass
class BaseData:
    """
    Any data object needs a gateway_name as source
    and should inherit base data.
    """

    gateway_name: str

    extra: dict = field(default=None, init=False)


# 创建BaseData对象
data_obj = BaseData(gateway_name="example_gateway")

# 访问字段
print(data_obj.gateway_name)  # 输出: example_gateway
print(data_obj.extra)  # 输出: None
