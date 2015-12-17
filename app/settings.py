class Settings():
    PLUGIN_FOLDER = 'Calculator'

    def __init__(self, sublime):
        self._settings_file = self.PLUGIN_FOLDER + '.sublime-settings'
        self._sublime = sublime

    @property
    def separator(self):
        return self._get('separator')

    def _get(self, name):
        settings = self._sublime.load_settings(self._settings_file)

        return settings.get(name)
