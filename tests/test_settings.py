import unittest
from app.settings import Settings


class TestSettings(unittest.TestCase):
    def setUp(self):
        self.sublime = SublimeSpy()
        self.settings = Settings(self.sublime)

    def test_folder_and_settings_file_name(self):
        self.settings.separator
        self.assertEqual('Calculator.sublime-settings', self.sublime.settings_file_to_load)

    def test_settings_file_actually_exists(self):
        from os import path
        settings_dir = path.dirname(path.dirname(path.abspath(__file__)))

        self.settings.separator

        file_to_find = path.join(settings_dir, self.sublime.settings_file_to_load)
        self.assertTrue(path.isfile(file_to_find),
                        'Could not find file "{0}" in path "{1}"'.format(
                            self.sublime.settings_file_to_load, file_to_find
                        ))


    def test_correct_settings_file_is_loaded(self):
        self.settings.separator
        self.assertThatCorrectSublimeSettingsFileIsLoaded(self.settings, self.sublime.settings_file_to_load)

    def test_get_separator(self):
        self.assertEqual(SublimeSettingsStub.SEPARATOR_SETTING, self.settings.separator)

    def assertThatCorrectSublimeSettingsFileIsLoaded(self, settings, sublime_settings_file):
        self.assertEqual(settings._settings_file, sublime_settings_file)


class SublimeSpy:
    def __init__(self):
        self.settings_file_to_load = None

    def load_settings(self, settings_file):
        self.settings_file_to_load = settings_file

        return SublimeSettingsStub()


class SublimeSettingsStub:
    SEPARATOR_SETTING = '===='

    def get(self, setting_name):
        if setting_name == 'separator':
            return self.SEPARATOR_SETTING

        return None
