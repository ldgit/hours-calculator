import sublime, sublime_plugin

try:
    # ST 3
    from .app.sublime_command import SublimeCommand
except ValueError:
    # ST 2
    from app.sublime_command import SublimeCommand


class CalculateHoursCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        command = SublimeCommand()
        command.calculate_hours(edit, self.view)
