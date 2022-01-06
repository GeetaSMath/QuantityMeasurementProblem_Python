from quantity_measurement_exception import QuantityMeasurementException

class QuantityMeasurementProblem:
    def __init__(self, length):
        """
         init method to pass length arguments
        :param length: length
        """
        self.length = length

    def __eq__(self, other):
        """
         method find quality length for none
        :param other: other
        :return: others and inches and raise the exception
        """
        if other.length is None:
            raise QuantityMeasurementException('none')
        if other.length != self.length:
            raise QuantityMeasurementException('References are not Equal')
        if type(other.length) != (self.length):
            raise QuantityMeasurementException('Type Not Equal')
        if other.length > 0:
            return other.length * 12
        else:
            raise QuantityMeasurementException('Length is Invalid')