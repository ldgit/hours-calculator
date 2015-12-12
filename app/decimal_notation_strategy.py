class DecimalNotationStrategy:
    def calculate_minutes(self, decimal_notation_string):
        decimal_hour = float(decimal_notation_string)

        return int(decimal_hour * 60)
