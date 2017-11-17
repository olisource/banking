import os
import sys

import xmlrunner
import unittest

from util.calculator import Calculator

class CalculatorTestCase(unittest.TestCase)
    def setUp(self):
        self.calculator1 = Calculator()

    def tearDown(self):
        pass

    def test_addition_success(self):
        self.assertEqual(self.calculator1.addition(1, 3), 4)
