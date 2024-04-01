class PositionHolding:
    def __init__(self, symbol, quantity):
        self.symbol = symbol
        self.quantity = quantity

# 创建一个字典，值是 PositionHolding 类的实例
holdings = {
    "AAPL": PositionHolding("AAPL", 100),
    "GOOGL": PositionHolding("GOOGL", 50)
}

# 访问字典中的值（类的实例）
print(holdings["AAPL"].symbol)  # 输出：AAPL
print(holdings["AAPL"].quantity)  # 输出：100
