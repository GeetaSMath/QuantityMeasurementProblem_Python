from quantity_measurement_exception import QuantityMeasurementException

class QuantityMeasurementProblem:
    def __init__(self, length):
        self.length = length

    @staticmethod
    def length_equal(feat, inches):
        """
         compare with equal length
        :param feat: feat param is one inch and 12 inch is one equal
        :param inches: inches to compare with feet
        :return:
        """
        if feat == 1 and inches == 12:
            return True
        if feat == 0 and inches == 0:
            return True
        else:
            return False

    @staticmethod
    def quantity_measurement(feat, inches):
        equal = QuantityMeasurementProblem.length_equal(feat, inches)
        if equal:
            return True
        else:
            raise QuantityMeasurementException("Not Equal")


