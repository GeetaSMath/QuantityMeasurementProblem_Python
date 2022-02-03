from quantity_measurement_exception import QuantityMeasurementException


class QuantityMeasurement:
    def __init__(self, length, unit):
        """

        :param length: passing length
        :param unit: passing unit
        """
        self.length = length
        self.unit = unit

    @staticmethod
    def feat_fun():
        """
         feat_fun to assign feat
        :return:
        """
        FEET = 3
        return FEET

    @staticmethod
    def yard_fun():
        """
        yard function to find
        :return:
        """
        YARD = 1
        return YARD

    def __eq__(self, other):
        """

        :param other: passing param
        :return: checking for quantity length unit
        """
        yard = QuantityMeasurement.yard_fun()
        feat = QuantityMeasurement.feat_fun()
        if other.length is None:
            raise QuantityMeasurementException('Null')
        if self.unit == other.unit or other.length == self.length:
            print("Values Not Equal")
            return True
        if type(self.length) != type(other.length):
            raise QuantityMeasurementException('Type Not Equal')
        if self.length != other.length:
            raise QuantityMeasurementException('References are not Equal')
        if other.length > 0:
            return other.length / 3
        else:
            raise QuantityMeasurementException("Invalid")