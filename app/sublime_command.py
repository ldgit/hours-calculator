from .hours_calculator import HoursCalculator


class SublimeCommand:
    def calculate_hours(self, edit, view):
        calculator = HoursCalculator()
        lines = self._get_selected_lines(view)
        view.insert(edit, view.sel()[0].end(), '\n' + calculator.add(*lines))

    def _get_selected_lines(self, view):
        lines = []
        for region in view.sel():
            if not region.empty():
                string = view.substr(region)

                lines += string.split('\n')

        return lines
