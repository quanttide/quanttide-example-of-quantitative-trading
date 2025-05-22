import sys
sys.path.append('..')  # 添加父目录到模块搜索路径，以便导入 strategies 模块

from src.intro.strategies import simulated_prices, trade_log, cash

def test_strategy_logic():
    """
    测试双均线交易策略的逻辑是否正确。
    """
    # 验证交易记录
    expected_trades = [
        "Day 6: 买入 90股 @ 110",
        "Day 11: 卖出 @ 116",
        "Day 13: 买入 85股 @ 118",
        "Day 15: 卖出 @ 125"
    ]
    assert trade_log == expected_trades, f"交易记录不匹配，预期: {expected_trades}, 实际: {trade_log}"

    # 验证最终资产
    expected_cash = 10625.00
    assert abs(cash - expected_cash) < 0.01, f"最终资产不匹配，预期: {expected_cash}, 实际: {cash}"

"""
交易记录:
Day 6: 买入 90股 @ 110
Day 11: 卖出 @ 116
Day 13: 买入 85股 @ 118
Day 15: 卖出 @ 125

最终资产: 10625.00元
总收益率: 6.25%
"""

