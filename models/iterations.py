import datetime
from config import MONITOR_RANGE


class Iteration:
    """
    Iteration object
    to store a record of fetched data with currency percentage changes
    of the BASIC PRICE

    delta: the percentage change in price by one minute

    absolute_value: absolute value that is calculated since
    start of script to spot the largest change

    largest_difference: each iteration will store information about the
    largest difference between last 60 iteration values
    """

    def __init__(self, delta: float = 0,
                 absolute_value: float = 0,
                 largest_difference: float = 0):
        self.delta = delta
        self.absolute_value: float = absolute_value
        self.largest_difference: float = largest_difference
        self.creation_time = datetime.datetime.now()


class Iterations:
    """
    List of iterations that form chronology of BASIC PRICE chane
    the size of storage declared in MONITOR_RANGE variable

        current_largest_delta:
    the largest difference in the scope of Iterations list

        add_iteration(self, iteration: Iteration):
    appending an Iteration into the Iterations list,
    keeping its size less than monitor_range minutes
    also updating the current_largest_delta variable

        calc_largest_difference(self):
    calculating largest difference to store it inside
    each Iteration and update in on the Iterations
    list

    """
    current_largest_difference: float

    def __init__(self, monitor_range: int):
        self.iterations = []
        self.monitor_range = monitor_range

    def add_iteration(self, delta: float):
        iteration = Iteration(delta)
        iteration.absolute_value = self.calculate_absolute_value(iteration.delta)

        if len(self.iterations) > MONITOR_RANGE:
            self.iterations.pop(0)
        self.iterations.append(iteration)

        self.current_largest_difference = self.calc_largest_difference()
        self.iterations[-1].largest_difference = self.current_largest_difference

    def calc_largest_difference(self):
        return self.find_max_absolute().absolute_value - self.find_min_absolute().absolute_value

    def find_max_absolute(self):
        return max(self.iterations, key=lambda x: x.absolute_value)

    def find_min_absolute(self):
        return min(self.iterations, key=lambda x: x.absolute_value)

    def calculate_absolute_value(self, delta: float):
        if self.iterations:
            return self.iterations[-1].absolute_value + delta
        else:
            return delta
