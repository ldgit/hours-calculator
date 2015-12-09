from __future__ import division
import re


class HoursCalculator:
    def add(self, *args):
        """
        :param list[str] args:
        :return: str
        """
        total_minutes = 0

        for hour in args:
            hour = hour.strip()
            if hour == '':
                continue
            if not self._is_valid_format(hour):
                return 'Invalid hour value: "{0}"'.format(hour)
            total_minutes += self._calculate_total_minutes_from_string(hour.replace('.', ':'))

        total_hours = int(total_minutes / 60)
        remaining_minutes = abs(total_minutes) % 60

        if total_minutes < 0 <= total_hours:
            return '-{0:02d}:{1:02d}'.format(total_hours, remaining_minutes)

        return '{0:02d}:{1:02d}'.format(total_hours, remaining_minutes)

    def _calculate_total_minutes_from_string(self, time_string):
        change_sign = False
        if time_string.startswith('-'):
            time_string = time_string[1:]
            change_sign = True

        time_list = time_string.split(':')
        hours = int(time_list[0])
        minutes = int(time_list[1])

        total_minutes = minutes + hours * 60

        return -total_minutes if change_sign else total_minutes

    def _is_valid_format(self, hour):
        pattern = re.compile('^\s*[+-]?\d+[.:]\d+\s*$')

        return pattern.search(hour) is not None


if __name__ == '__main__':
    import sys

    print(HoursCalculator().add(*sys.argv[1:]))
