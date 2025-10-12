def add(a, b):
    """
    两数相加，只接受数字类型
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("参数必须是数字类型")
    return a + b
