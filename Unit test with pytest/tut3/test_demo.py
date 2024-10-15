from tut3.demoCode import DemoClass
import pytest

class TestClass:

    def setup_method(self):
        self.arithmetic = DemoClass()

    @pytest.mark.parametrize( 'num1, num2, result',
            [
                (7, 3, 10),
                ('Hello', ' World', 'Hello World'),
                (10.5, 25.5, 36)
            ]
    )
    def test_add(self, num1, num2, result):
        assert self.arithmetic.add(num1, num2) == result