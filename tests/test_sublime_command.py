import unittest
from app.sublime_command import SublimeCommand
from tests.view_spy import ViewSpy
from tests.region_stub import EmptyRegionStub, RegionStub


class TestSublimeCommand(unittest.TestCase):
    def setUp(self):
        # SUT
        self.command = SublimeCommand()

        # Command inputs
        self.view = ViewSpy()
        self.edit = 'just some edit placeholder'

    def test_empty_region_selected(self):
        self.view.sel_return = [EmptyRegionStub()]

        self.command.calculate_hours(self.edit, self.view)

        self.assertEqual(self.edit, self.view.first_insert_parameter)
        self.assertEqual('dummy region end', self.view.second_insert_parameter)
        self.assertEqual('\n00:00', self.view.third_insert_parameter)

    def test_multiple_empty_regions_selected(self):
        final_region = EmptyRegionStub()
        final_region.dummy_region_end = 'final_region_end'
        self.view.sel_return = [EmptyRegionStub(), EmptyRegionStub(), final_region]

        self.command.calculate_hours(self.edit, self.view)

        self.assertEqual(self.edit, self.view.first_insert_parameter)
        self.assertEqual('final_region_end', self.view.second_insert_parameter)
        self.assertEqual('\n00:00', self.view.third_insert_parameter)

    def test_single_text_selection(self):
        single_region = RegionStub()
        self.view.sel_return = [single_region]
        self.view.substr_return_value = """
        3:12
        1:20
        -22:10
        -18:38
"""

        self.command.calculate_hours(self.edit, self.view)

        self.assertEqual(single_region, self.view.substr_parameter)
        self.assertEqual("\n-36:16", self.view.third_insert_parameter)

    def test_multi_line_selection(self):
        self.skipTest('todo')
