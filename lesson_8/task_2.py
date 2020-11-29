class Division:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def divide(dividend, divider):
        try:
            return dividend / divider
        except ZeroDivisionError:
            return f"На ноль делить нельзя!"


print(Division.divide(10, 0))
print(round(Division.divide(100, 2.3), 2))
