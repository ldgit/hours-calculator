import sublime, sublime_plugin

try:
    # ST 3
    from .app.hours_calculator import HoursCalculator
except ValueError:
    # ST 2
    from app.hours_calculator import HoursCalculator


class CalculateHoursCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        calculator = HoursCalculator()
        lines = self._get_selected_lines(self.view)
        self.view.insert(edit, self.view.sel()[0].end(), '\n' + calculator.add(*lines))

    def _get_selected_lines(self, view):
        lines = []
        for region in view.sel():
            if not region.empty():
                string = view.substr(region)

                lines += string.split('\n')

        return lines
