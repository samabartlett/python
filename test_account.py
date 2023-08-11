import pytest
from account import Account

class TestAccount:
    def test_init(self):
        acc = Account('John')
        assert acc.get_name() == 'John'
        assert acc.get_balance() == pytest.approx(0)

    def test_deposit(self):
        acc = Account('Sam')
        assert acc.deposit(-2) is False
        assert acc.get_balance() == pytest.approx(0)
        assert acc.deposit(100) is True
        assert acc.get_balance() == pytest.approx(100)

    def test_withdraw(self):
        acc = Account('Jack')
        acc.deposit(200)
        assert acc.withdraw(-50) is False
        assert acc.get_balance() == pytest.approx(200)
        assert acc.withdraw(0) is False
        assert acc.get_balance() == pytest.approx(200)
        assert acc.withdraw(250) is False
        assert acc.get_balance() == pytest.approx(200)
        assert acc.withdraw(150) is True
        assert acc.get_balance() == pytest.approx(50)
