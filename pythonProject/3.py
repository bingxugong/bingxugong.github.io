
from dataclasses import dataclass, field

from enum import Enum
class Exchange(Enum):
    """
    Exchange.
    """
    # Chinese
    CFE = "CFE"             # CBOE Futures Exchange
    DME = "DME"             # Dubai Mercantile Exchange
    EUREX = "EUX"           # Eurex Exchange
    APEX = "APEX"           # Asia Pacific Exchange
    LME = "LME"             # London Metal Exchange

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
    exchange: Exchange  # 假设Exchange是一个枚举类型

    def __post_init__(self) -> None:
        self.vt_symbol: str = f"{self.symbol}.{self.exchange.value}"

# 创建ContractData对象
contract_obj = ContractData(gateway_name="example_gateway", symbol="BTCUSD", exchange=Exchange.CFE)

# 访问继承自BaseData的字段
print(contract_obj.gateway_name)  # 输出: example_gateway

# 访问子类特有的字段
print(contract_obj.symbol)  # 输出: BTCUSD
print(contract_obj.exchange.value)  # 输出: Exchange.CFE

# 访问在__post_init__中生成的字段
print(contract_obj.vt_symbol)  # 输出: BTCUSD.Exchange.CFE
