
import math
from enums.class_interval_type import ClassIntervalType


class ClassIntervalHelper:

    @staticmethod
    def get_width_of_class_interval(smallest_value, largest_value, number_of_class_intervals):
        """Gets the Width of Class interval (smallest_value, largest_value, number_of_class_intervals)"""
        interval = (largest_value + 1 - smallest_value) / number_of_class_intervals
        return math.ceil(interval)

    @staticmethod
    def get_class_intervals(smallest_value, largest_value, class_width, class_interval_type):
        """Gets class intervals"""
        class_intervals = []
        lower_range = smallest_value
        upper_range = 0
        while upper_range < largest_value:
            upper_range = lower_range + class_width
            class_intervals.append((lower_range, upper_range))

            lower_range = upper_range
            if class_interval_type == ClassIntervalType.Discrete:
                lower_range += 1

        return class_intervals
