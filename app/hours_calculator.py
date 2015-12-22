from __future__ import division
import re
from .hour_notation_strategy import HourNotationStrategy
from .decimal_notation_strategy import DecimalNotationStrategy


class HoursCalculator:
    def add(self, *args):
        """
        :param list[str] args:
        :return: str
        """
        total_minutes = 0

        for hour in args:
            hour = hour.strip()
            if not self._is_valid_format(hour) or hour == '':
                continue
            total_minutes += self._get_calculation_strategy(hour).calculate_minutes(hour)

        total_hours = int(total_minutes / 60)
        remaining_minutes = abs(total_minutes) % 60

        if total_minutes < 0 <= total_hours:
            return '-{0:02d}:{1:02d}'.format(total_hours, remaining_minutes)

        return '{0:02d}:{1:02d}'.format(total_hours, remaining_minutes)

    def _get_calculation_strategy(self, time_string):
        if ':' in time_string:
            return HourNotationStrategy()
        else:
            return DecimalNotationStrategy()

    def _is_valid_format(self, hour):
        pattern = re.compile('^\s*[+-]?\d+[.:]\d+\s*$')

        return pattern.search(hour) is not None


if __name__ == '__main__':
    import sys

    print(HoursCalculator().add(*sys.argv[1:]))
