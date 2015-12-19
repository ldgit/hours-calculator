from .hours_calculator import HoursCalculator


class SublimeCommand:
    def __init__(self, settings):
        self._settings = settings

    def calculate_hours(self, edit, view):
        calculator = HoursCalculator()
        lines = self._get_selected_lines(view)
        view.insert(edit, view.sel()[-1].end(), '\n{0}{1}'.format(self._get_separator(), calculator.add(*lines)))

    def _get_selected_lines(self, view):
        lines = []
        for region in view.sel():
            if not region.empty():
                string = view.substr(region)

                lines += string.split('\n')

        return lines

    def _get_separator(self):
        return self._settings.separator + '\n' if self._settings.separator else ''
