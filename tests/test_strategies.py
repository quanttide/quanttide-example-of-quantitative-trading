from src.strategies import calculate_ma

def test_calculate_ma_with_full_window():
    prices = [100, 102, 101, 105, 107]
    window = 5
    expected = [100.0, 101.0, 101.0, 102.0, 103.0]  # 手动计算验证
    result = calculate_ma(prices, window)
    assert result == expected

def test_calculate_ma_with_window_larger_than_data():
    prices = [100, 102]
    window = 5
    expected = [100.0, 101.0]  # 每个点都基于已有数据计算
    result = calculate_ma(prices, window)
    assert result == expected

def test_calculate_ma_with_empty_prices():
    prices = []
    window = 5
    expected = []
    result = calculate_ma(prices, window)
    assert result == expected

def test_calculate_ma_with_single_price():
    prices = [100]
    window = 5
    expected = [100.0]
    result = calculate_ma(prices, window)
    assert result == expected