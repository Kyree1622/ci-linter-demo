import pytest
import sys
import os
from calculator import add  # 导入移到顶部

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestCalculator:  # 类定义前有2个空行
    """计算器测试类"""

    def test_add_positive_numbers(self):
        """测试正数相加"""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """测试负数相加"""
        assert add(-2, -3) == -5

    def test_add_zero(self):
        """测试零值边界情况"""
        assert add(0, 0) == 0

    def test_add_large_numbers(self):
        """测试大数相加"""
        assert add(1000000, 2000000) == 3000000

    def test_add_float_numbers(self):
        """测试浮点数相加"""
        assert add(1.5, 2.5) == 4.0

    def test_add_invalid_input(self):
        """测试无效输入"""
        with pytest.raises(TypeError):
            add("hello", "world")
