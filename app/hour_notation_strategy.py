class HourNotationStrategy:
    def calculate_minutes(self, hour_notation_string):
        change_sign = False
        if hour_notation_string.startswith('-'):
            hour_notation_string = hour_notation_string[1:]
            change_sign = True

        time_list = hour_notation_string.split(':')
        hours = int(time_list[0])
        minutes = int(time_list[1])

        total_minutes = minutes + hours * 60

        return -total_minutes if change_sign else total_minutes
