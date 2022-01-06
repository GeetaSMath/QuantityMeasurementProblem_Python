import pytest
from quantity_measurement_problem import QuantityMeasurementProblem
from quantity_measurement_exception import QuantityMeasurementException


class TestQuantityMeasurementProblem:
    @pytest.fixture()
    def test_quantity_measurement(self):
        self.length = QuantityMeasurementProblem()

    @staticmethod
    def test_null_check():
        """
        test case to find null check and comparing length1 and length
        :return: none
        """
        with pytest.raises(QuantityMeasurementException) as exe:
            length1 = QuantityMeasurementProblem(0)
            length2 = QuantityMeasurementProblem(None)
            length1 == length2
        assert exe.value.message == 'none'

    @staticmethod
    def test_reference_check():
        """
        test reference check none
        :return: reference not qual
        """
        with pytest.raises(QuantityMeasurementException) as exe:
            ref1 = QuantityMeasurementProblem(1)
            ref2 = QuantityMeasurementProblem(2)
            ref1 != ref2
        assert exe.value.message == 'References are not Equal'