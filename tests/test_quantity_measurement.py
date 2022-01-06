import pytest
from quantity_measurement_problem import QuantityMeasurementProblem
from quantity_measurement_exception import QuantityMeasurementException


class TestQuantityMeasurementProblem:
    @pytest.fixture()
    def test_quantity_measurement(self):
        self.length = QuantityMeasurementProblem()

    @staticmethod
    def test_null_check():
        with pytest.raises(QuantityMeasurementException) as exe:
            length1 = QuantityMeasurementProblem(0)
            length2 = QuantityMeasurementProblem(None)
            length1 == length2
        assert exe.value.message == 'Null'
