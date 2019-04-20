from helpers.class_interval_helper import ClassIntervalHelper
from enums.class_interval_type import ClassIntervalType

input_data = [
    66, 65, 96, 80, 71,
    93, 66, 96, 75, 61,
    69, 61, 51, 84, 58,
    73, 77, 89, 69, 92,
    57, 56, 55, 78, 96
]

smallest_value = min(input_data)
largest_value = max(input_data)

number_of_class_intervals = 6

width_of_class_interval = ClassIntervalHelper.get_width_of_class_interval(
    smallest_value,
    largest_value,
    number_of_class_intervals)

print(f'smallest_value: {smallest_value}')
print(f'largest_value: {largest_value}')
print(f'width: {width_of_class_interval} ')

class_intervals = ClassIntervalHelper.get_class_intervals(
    smallest_value,
    largest_value,
    width_of_class_interval,
    ClassIntervalType.Discrete)

print(class_intervals)
