import logging
import pytest


class TestCalculator:
    """Tests, related to calculator"""
    @staticmethod
    @pytest.mark.smoke
    def test_sum_2_integers(calculator):
        """
        Testing `addition` calculator function with 2 int parameters
        """
        logging.info("Verifying that `addition` function works correctly with 2 integers")
        res = calculator.addition(1, 1)
        assert res == 2, f"`Addition` function does not work correctly: expecting 2, but got {res}"
        logging.info("Successfully verified that `addition` works correctly")

    @staticmethod
    @pytest.mark.smoke
    def test_concatenate_2_strings(calculator):
        """
        Testing `addition` calculator function with 2 string parameters
        """
        logging.info("Verifying that `addition` function works correctly with 2 strings")
        res = calculator.addition('one', 'two')
        assert res == 'onetwo', f"`Addition` function does not work correctly: expecting `onetwo`, but got {res}"
        logging.info("Successfully verified that `addition` works correctly")

    @staticmethod
    @pytest.mark.xfail(reason="This test is failing due to <put your reason here>")
    @pytest.mark.regression
    def test_concatenate_int_and_string(calculator):
        """
        Testing `addition` calculator function with 1 integer and 1 string parameters
        """
        logging.info("Verifying that `addition` function works correctly with 1 integer and 1 string")
        res = calculator.addition(1, 'two')
        assert res == '1two', f"`Addition` function does not work correctly: expecting 2, but got {res}"
        logging.info("Successfully verified that `addition` works correctly")