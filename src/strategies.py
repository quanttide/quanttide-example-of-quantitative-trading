"""
"""

# 模拟一个最简单的双均线交易策略（5日均线 & 20日均线）

# 生成模拟数据（假设每日收盘价）
simulated_prices = [
    100, 102, 101, 105, 107,  # 第1-5天
    110, 108, 112, 115, 113,  # 第6-10天
    116, 120, 118, 122, 125   # 第11-15天
]

# 计算移动平均线（模拟实现）
def calculate_ma(prices, window):
    ma = []
    for i in range(len(prices)):
        # 使用 min 来决定实际参与计算的数据窗口范围
        start_index = max(0, i - window + 1)  # 如果 i < window，start_index 会是 0
        window_prices = prices[start_index : i + 1]
        ma_value = sum(window_prices) / len(window_prices)  # 使用实际窗口长度来计算均值
        ma.append(round(ma_value, 2))  # 保留两位小数
    return ma

def main():
    # 计算5日和20日均线（注意：因为数据量小，20日均线窗口自动适配）
    short_ma = calculate_ma(simulated_prices, 5)  # 短期均线
    long_ma = calculate_ma(simulated_prices, 10)  # 长期均线（因数据只有15天）

    # 策略逻辑
    hold_stock = False  # 是否持有股票
    cash = 10000        # 初始资金
    shares = 0          # 持有股票数量
    trade_log = []      # 交易记录

    for day in range(1, len(simulated_prices)):
        # 获取当前价格和前一日均线值
        current_price = simulated_prices[day]
        prev_short = short_ma[day-1]
        prev_long = long_ma[day-1]
        
        # 生成交易信号（金叉：短期上穿长期）
        if prev_short > prev_long and not hold_stock:
            # 买入信号
            shares = cash // current_price
            cash -= shares * current_price
            hold_stock = True
            trade_log.append(f"Day {day+1}: 买入 {shares}股 @ {current_price}")
            
        # 生成交易信号（死叉：短期下穿长期）
        elif prev_short < prev_long and hold_stock:
            # 卖出信号
            cash += shares * current_price
            shares = 0
            hold_stock = False
            trade_log.append(f"Day {day+1}: 卖出 @ {current_price}")

    # 最终清算
    if hold_stock:
        cash += shares * simulated_prices[-1]

    # 打印结果
    print("模拟价格序列:", simulated_prices)
    print("\n交易记录:")
    for log in trade_log:
        print(log)
    print(f"\n最终资产: {cash:.2f}元")
    print(f"总收益率: {(cash/10000-1)*100:.2f}%")
