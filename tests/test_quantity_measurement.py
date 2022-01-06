import pytest
from quantity_measurement_problem import QuantityMeasurementProblem
from quantity_measurement_exception import QuantityMeasurementException


class TestQuantityMeasurementProblem:
        @staticmethod
        def test_zero_feet():
            """
            testing for zero feet
            :return: expected and pass the case
            """
            expected = True
            actual = QuantityMeasurementProblem.quantity_measurement(0, 0)
            assert actual == expected
