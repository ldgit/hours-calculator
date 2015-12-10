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

        self.assertViewInsertCalledWithEditAsFirstParameter()
        self.assertViewInsertCalledWithRegionEndAsSecondParameter('dummy region end')
        self.assertThirdInsertParameterIsCalculationResult('\n00:00')

    def test_multiple_empty_regions_selected(self):
        final_region = EmptyRegionStub()
        final_region.dummy_region_end = 'final_region_end'
        self.view.sel_return = [EmptyRegionStub(), EmptyRegionStub(), final_region]

        self.command.calculate_hours(self.edit, self.view)

        self.assertViewInsertCalledWithEditAsFirstParameter()
        self.assertViewInsertCalledWithRegionEndAsSecondParameter('final_region_end')
        self.assertThirdInsertParameterIsCalculationResult('\n00:00')

    def test_single_multiline_text_selection(self):
        single_region = RegionStub()
        self.view.sel_return = [single_region]
        self.view.substr_return_value = """
        3:12
        1:20
        -22:10
        -18:38
        """
        expected_lines = ["", "        3:12", "        1:20", "        -22:10", "        -18:38", "        "]

        self.command.calculate_hours(self.edit, self.view)

        self.assertEqual(expected_lines, self.command._get_selected_lines(self.view))
        self.assertThirdInsertParameterIsCalculationResult("\n-36:16")

    def test_several_single_line_text_selections(self):
        """
        Tests that the selection in sublime text is correctly converted to python list.
        """
        self.first_region = RegionStub()
        self.second_region = RegionStub()
        self.view.sel_return = [self.first_region, self.second_region]
        self.view.substr = self.substr_replacement
        expected_lines = ["12:00", "1:00"]

        self.command.calculate_hours(self.edit, self.view)

        self.assertEqual(expected_lines, self.command._get_selected_lines(self.view))
        self.assertThirdInsertParameterIsCalculationResult("\n13:00")

    def substr_replacement(self, region):
        """
        A stub method for sublime text view object substr method. It returns different values based on what region it
        receives.
        """
        if region is self.first_region:
            return "12:00"

        if region is self.second_region:
            return "1:00"

    def assertViewInsertCalledWithEditAsFirstParameter(self):
        self.assertEqual(self.edit, self.view.first_insert_parameter)

    def assertViewInsertCalledWithRegionEndAsSecondParameter(self, expected_region_end):
        self.assertEqual(expected_region_end, self.view.second_insert_parameter)

    def assertThirdInsertParameterIsCalculationResult(self, expected_calculation_result):
        self.assertEqual(expected_calculation_result, self.view.third_insert_parameter)

    def test_fail(self):
        self.fail('just a test')
