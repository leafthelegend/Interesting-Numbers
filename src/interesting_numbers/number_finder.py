from interesting_numbers.interests import *
class NumberFinder:
    def __init__(self, checks, base_dependent_checks, base_range = range(2,38)):
        self.checks = checks
        self.base_dependent_checks = base_dependent_checks
        self.base_range = base_range
    def findnext(self,number):
        for n in range(number+1, number+1000):
            result = self.find(n)
            if result:
                return result
        return None
    def find(self, number):
        for check in self.checks:
            result = check(number)
            if result:
                return result
        for base in self.base_range:
            for check in self.base_dependent_checks:
                result = check(number, base)
                if result:
                    return result
        return None
    
# example finder:
# finder = NumberFinder([is_square, is_cube, is_triangular, is_fibonacci, is_power_of_two], [is_repdigit, is_consecutive, is_palindrome])