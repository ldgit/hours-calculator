from __future__ import division
import re

class HoursCalculator():
    def add(self, *args):
        """
        :param list[str] args:
        :return: str
        """
        total_minutes = 0;

        for hour in args:
            hour = hour.strip()
            if hour == '':
                continue
            if not self.is_valid_format(hour):
                return 'NaN'
            total_minutes += self.calculate_total_minutes_from_string(hour.replace('.', ':'))

        total_hours = int(total_minutes / 60)
        remaining_minutes = abs(total_minutes) % 60

        if total_minutes < 0 <= total_hours:
            return str.format('-{0:02d}:{1:02d}', total_hours, abs(remaining_minutes))

        return str.format('{0:02d}:{1:02d}', total_hours, abs(remaining_minutes))

    def calculate_total_minutes_from_string(self, time_string):
        change_sign = False
        if time_string.startswith('-'):
            time_string = time_string[1:]
            change_sign = True

        time_list = time_string.split(':')
        hours = int(time_list[0])
        try:
            minutes = int(time_list[1])
        except IndexError:
            minutes = 0

        total_minutes = minutes + hours * 60

        return -total_minutes if change_sign else total_minutes

    def is_valid_format(self, hour):
        pattern = re.compile('^\s*-{0,1}\d+[.:]\d+\s*$')

        return pattern.search(hour) is not None
