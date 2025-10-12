import pytest
import sys
import os

# 添加项目根目录到Python路径，以便导入calculator模块
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from calculator import add

class TestCalculator:
    """计算器测试类"""
    
    def test_add_positive_numbers(self):
        """测试正数相加"""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """测试负数相加"""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5
    
    def test_add_zero(self):
        """测试零值边界情况"""
        assert add(0, 0) == 0
        assert add(0, 5) == 5
        assert add(5, 0) == 5
    
    def test_add_large_numbers(self):
        """测试大数相加"""
        assert add(1000000, 2000000) == 3000000
    
    def test_add_float_numbers(self):
        """测试浮点数相加"""
        assert add(1.5, 2.5) == 4.0
        assert abs(add(0.1, 0.2) - 0.3) < 1e-10  # 处理浮点精度问题
    
    def test_add_invalid_input(self):
        """测试无效输入（字符串相加会报错，这是预期的）"""
        with pytest.raises(TypeError):
            add("hello", "world")