import pytest
from quantity_measurement_problem import QuantityMeasurement
from quantity_measurement_exception import QuantityMeasurementException


class TestQuantityMeasurementProblem:
        """
         test cases to check values for zero and type and reference check
         by its lenth and unit
        """

        @pytest.mark.parametrize("length1,unit1,length2,unit2",[(0,"feet",0,"feet")])
        def test_zero_value_check(self, length1, unit1, length2, unit2):
            """

            :param length1: length contains 1 and equals to 12 inches
            :param unit1: unit is to check for reference
            :param length2: param for check
            :param unit2:  reference check
            :return: pass quantity when we compare
            """
            print(length1)
            quantity1 = QuantityMeasurement(length1, unit1)
            quantity2 = QuantityMeasurement(length2, unit2)
            assert quantity1 == quantity2

        @pytest.mark.parametrize('length1, unit1, length2, unit2', [(None, "feet", None, "feet")])
        def test_null_reference_check(self, length1, unit1, length2, unit2):
            """

            :param length1: length1 for none
            :param unit1: unit to find feet
            :param length2: length2 for none
            :param unit2:unit to find feet
            :return: pass the test case when it true
            """
            quantity1 = QuantityMeasurement(length1, unit1)
            quantity2 = QuantityMeasurement(length2, unit2)
            with pytest.raises(QuantityMeasurementException) as exe:
                quantity1 == quantity2
            assert exe.value.message == 'Null'

        @pytest.mark.parametrize('length1, unit1, length2, unit2', [(0, "feet", 2, "inch")])
        def test_reference_check(self, length1, unit1, length2, unit2):
            """
            test case for reference check
            :param length1:length1 is for 0
            :param unit1: unit is for feet
            :param length2: length2 is for 2
            :param unit2: inch unit
            :return: pass the test cases
            """
            quantity1 = QuantityMeasurement(length1, unit1)
            quantity2 = QuantityMeasurement(length2, unit2)
            with pytest.raises(QuantityMeasurementException) as exe:
                quantity1 == quantity2
            assert exe.value.message == 'References are not Equal'

        @pytest.mark.parametrize('length1, unit1 , length2, unit2', [(0, "feet", "hello", "inch")])
        def test_type_check(self, length1, unit1, length2, unit2):
            """
            test case for type check
            :param length1: length1 is for zero
            :param unit1: unit for feet
            :param length2: length2 is for str to pass
            :param unit2: inch for unit
            :return: pass the test case when its true
            """
            quantity1 = QuantityMeasurement(length1, unit1)
            quantity2 = QuantityMeasurement(length2, unit2)
            with pytest.raises(QuantityMeasurementException) as exe:
                quantity1 == quantity2
            assert exe.value.message == 'Type Not Equal'

        @pytest.mark.parametrize('length1, unit1 , length2, unit2', [(0, "feet", "hello", "inch")])
        def test_type_check(self, length1, unit1, length2, unit2):
            """
             test case fot type check is equal
            :param length1: for zero
            :param unit1: for feet
            :param length2: to pass string
            :param unit2: inch to find unit
            :return: pass the test case when its true
            """
            quantity1 = QuantityMeasurement(length1, unit1)
            quantity2 = QuantityMeasurement(length2, unit2)
            with pytest.raises(QuantityMeasurementException) as exe:
                quantity1 == quantity2
            assert exe.value.message == 'Type Not Equal'

