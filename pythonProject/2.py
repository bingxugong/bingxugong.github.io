from dataclasses import dataclass, field

@dataclass
class BaseData:
    """
    Any data object needs a gateway_name as source
    and should inherit base data.
    """

    gateway_name: str

    extra: dict = field(default=None, init=False)

@dataclass
class ContractData(BaseData):
    """
    Data object representing contract information.
    """

    symbol: str
    exchange_name: str


# 创建ContractData对象
contract_obj = ContractData(gateway_name="example_gateway", symbol="BTCUSD", exchange_name="Exchange1")

# 访问继承自BaseData的字段
print(contract_obj.gateway_name)  # 输出: example_gateway

# 访问子类特有的字段
print(contract_obj.symbol)  # 输出: BTCUSD
print(contract_obj.exchange_name)  # 输出: Exchange1
