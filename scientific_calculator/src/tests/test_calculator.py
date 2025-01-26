import sys
import unittest
import os
import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Non è possibile dividere per zero.")
        return a / b

    def power(self, a, b):
        return a ** b

    def logarithm(self, a, base):
        if a <= 0:
            raise ValueError("Il logaritmo è definito solo per numeri maggiori di zero.")
        return math.log(a, base)

    def sine(self, angle):
        return math.sin(angle)

    def cosine(self, angle):
        return math.cos(angle)

    def tangent(self, angle):
        return math.tan(angle)

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

    def test_power(self):
        self.assertEqual(self.calculator.power(2, 3), 8)

    def test_logarithm(self):
        self.assertEqual(self.calculator.logarithm(8, 2), 3)
        with self.assertRaises(ValueError):
            self.calculator.logarithm(-1)

    def test_sine(self):
        self.assertAlmostEqual(self.calculator.sine(0), 0)

    def test_cosine(self):
        self.assertAlmostEqual(self.calculator.cosine(0), 1)

    def test_tangent(self):
        self.assertAlmostEqual(self.calculator.tangent(0), 0)

if __name__ == '__main__':
    unittest.main()