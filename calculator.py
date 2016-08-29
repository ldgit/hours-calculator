import sublime, sublime_plugin

try:
    # ST 3
    from .app.sublime_command import SublimeCommand
    from .app.settings import Settings
except ValueError:
    # ST 2
    from app.sublime_command import SublimeCommand
    from app.settings import Settings


class CalculateHoursCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        SublimeCommand(Settings(sublime)).calculate_hours(edit, self.view)


class ConvertHoursToSecondsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        SublimeCommand(Settings(sublime)).convert_hours_to_seconds(edit, self.view)
