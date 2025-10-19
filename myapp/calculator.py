def add(a, b):
    """
    两数相加，只接受数字类型
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("参数必须是数字类型")
    return a + b


def subtract(a, b):
    """
    两数相减
    Args:
        a: 被减数
        b: 减数
    Returns:
        两数之差
    """
    return a - b
