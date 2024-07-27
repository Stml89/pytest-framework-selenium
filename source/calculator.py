"""
This module defines add(a,b), multiply(a, b) and divide(a, b).
"""
import logging


class Calculator:
    @staticmethod
    def addition(a, b):
        """
        Returns a plus b.

        Usage: calculator.addition(2, 2)
        4
        Usage: calculator.addition('b', 4)
        'b4'
        """
        logging.debug(f"Given A: {a}")
        logging.debug(f"Given B: {b}")
        return a + b

    @staticmethod
    def subtraction(a, b):
        """
        Returns b minus a.

        Usage: calculator.subtraction(2, 2)
        0
        """
        logging.debug(f"Given A: {a}")
        logging.debug(f"Given B: {b}")
        return b - a

    @staticmethod
    def multiply(a, b):
        """
        Returns a multiplied by b.

        Usage: calculator.multiply(3, 3)
        9
        Usage: calculator.multiply('b', 4)
        'bbbb'
        """
        logging.debug(f"Given A: {a}")
        logging.debug(f"Given B: {b}")
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Returns a divided by b.

        Usage: calculator.multiply(25, 5)
        5.0
        """
        logging.debug(f"Given A: {a}")
        logging.debug(f"Given B: {b}")
        return a / b
