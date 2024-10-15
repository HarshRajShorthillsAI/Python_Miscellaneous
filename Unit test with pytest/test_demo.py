import pytest
from demoCode import DemoClass

class TestDemo:
    def setup_method(self):
        self.arithmetic = DemoClass()

    @pytest.mark.number
    def test_add(self):
        assert self.arithmetic.add(3, 2) == 5
        assert self.arithmetic.add(-3,2) == -1
        assert self.arithmetic.add(3,-2) == 1
        assert self.arithmetic.add(-3,-2) == -5

    @pytest.mark.number
    def test_subtract(self):
        assert self.arithmetic.subtract(3,2) == 1
        assert self.arithmetic.subtract(3,-2) == 5
        assert self.arithmetic.subtract(-3,2) == -5
        assert self.arithmetic.subtract(-3,-2) == -1

    @pytest.mark.number
    def test_multiply(self):
        assert self.arithmetic.multiply(3,2) == 6
        assert self.arithmetic.multiply(3,-2) == -6
        assert self.arithmetic.multiply(-3,2) == -6
        assert self.arithmetic.multiply(-3,-2) == 6

    @pytest.mark.number
    def test_divide(self):
        assert self.arithmetic.divide(3,2) == 1.5
        assert self.arithmetic.divide(3,-2) == -1.5
        assert self.arithmetic.divide(-3,2) == -1.5
        assert self.arithmetic.divide(-3,-2) == 1.5
        assert self.arithmetic.divide(4,2) == 2

    @pytest.mark.alphabet
    def test_consonents(self):
        for i in range(65, 91):
            t = chr(i)
            assert self.arithmetic.consonents(t) == (t not in ['A', 'E', 'I', 'O', 'U'])

        for i in range(97, 123):
            t = chr(i)
            assert self.arithmetic.consonents(t) == (t not in ['a', 'e', 'i', 'o', 'u'])

    @pytest.mark.alphabet
    def test_vowels(self):
        for i in range(65, 91):
            t = chr(i)
            assert self.arithmetic.vowel(t) == (t in ['A', 'E', 'I', 'O', 'U'])

        for i in range(97, 123):
            t = chr(i)
            assert self.arithmetic.vowel(t) == (t in ['a', 'e', 'i', 'o', 'u'])

    # def test_divide_by_zero(self):
    #     assert self.arithmetic.divide(1/0)