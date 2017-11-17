import unittest

from bank_account import BankAccount, MinimumBalanceAccount

class AccountBalanceTestCase(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount()

    def test_balance(self):
        self.assertEqual(self.account1.balance, 3000, msg="Invalid account balance")

    def test_deposit(self):
        self.account1.deposit(4000)
        self.assertEqual(self.account1.balance, 7000, msg="Inaccurate deposit method")

    def test_withdraw(self):
        self.account1.withdraw(500)
        self.assertEqual(self.account1.balance, 2500, msg="Inaccurate withdraw method")

    def test_invalid_transaction(self):
        self.assertEqual(self.account1.withdraw(6000), "Invalid transaction", msg="Invalid transaction")

    def test_sub_class(self):
        self.assertTrue(issubclass(MinimumBalanceAccount, BankAccount), msg="Not a subclass of BalanceAccount")
