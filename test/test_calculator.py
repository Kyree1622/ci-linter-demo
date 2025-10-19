import pytest
from myapp.calculator import add, subtract


class TestCalculator:
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

    def test_subtract_positive_numbers(self):
        """测试正数相减"""
        assert subtract(5, 3) == 2
        assert subtract(10, 2) == 8

    def test_subtract_negative_numbers(self):
        """测试负数相减"""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8

    def test_subtract_zero(self):
        """测试零值边界情况"""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0

    def test_subtract_large_numbers(self):
        """测试大数相减"""
        assert subtract(1000000, 500000) == 500000
