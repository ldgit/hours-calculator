import unittest
from app.hours_calculator import HoursCalculator


class TestHoursCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = HoursCalculator()

    def test_add_with_no_parameters_returns_zero(self):
        self.assertEqual("00:00", self.calculator.add())

    def test_add_with_one_parameter_returns_that_parameter(self):
        self.assertEqual("02:53", self.calculator.add("2:53"))

    def test_add_ignore_leading_zero(self):
        self.assertEqual("02:53", self.calculator.add("02:53"))
        self.assertEqual("02:03", self.calculator.add("2:03"))

    def test_ignore_leading_plus_sign(self):
        self.assertEqual('01:00', self.calculator.add("+1:00"))

    def test_add_one_hour_and_sixty_minutes_equals_two_hours(self):
        self.assertEqual("02:00", self.calculator.add("1:60"))

    def test_add_1_hour_and_120_minutes_equals_3_hours(self):
        self.assertEqual("03:00", self.calculator.add("1:120"))

    def test_add_1_hour_and_75_minutes_equals_2_hours_and_15_minutes(self):
        self.assertEqual("02:15", self.calculator.add("1:75"))

    def test_add_zero(self):
        self.assertEqual("00:00", self.calculator.add("0:00"))
        self.assertEqual("01:00", self.calculator.add("1:00", "0:00"))

    def test_add_two_time_values(self):
        self.assertEqual("00:00", self.calculator.add("0:0", "0:0"))
        self.assertEqual("01:15", self.calculator.add("1:15", "0:00"))
        self.assertEqual("02:15", self.calculator.add("1:15", "1:00"))
        self.assertEqual("03:15", self.calculator.add("1:15", "1:60"))
        self.assertEqual("04:15", self.calculator.add("1:75", "01:60"))

    def test_add_multiple_time_values(self):
        self.assertEqual("07:10", self.calculator.add("1:50", "2:35", "2:45"))
        self.assertEqual("07:00", self.calculator.add("1:10", "1:10", "01:10", "01:10", "01:10", "01:10"))

    def test_add_single_negative_hour(self):
        self.assertEqual("-1:00", self.calculator.add("-1:00"))
        self.assertEqual("-15:10", self.calculator.add("-15:10"))
        self.assertEqual("-00:10", self.calculator.add("-0:10"))
        self.assertEqual("00:00", self.calculator.add("0:0"))

    def test_add_positive_with_negative_hours(self):
        self.assertEqual("00:10", self.calculator.add("1:10", "-1:00"))
        self.assertEqual("00:00", self.calculator.add("1:10", "-1:10"))
        self.assertEqual("-00:05", self.calculator.add("1:10", "-1:15"))
        self.assertEqual("00:05", self.calculator.add("2:10", "-1:65"), 'Negative hour with 65 minutes')

    def test_add_multiple_negative_hours(self):
        self.assertEqual("-2:10", self.calculator.add("-1:10", "-1:00"))
        self.assertEqual("-3:40", self.calculator.add("-1:10", "-1:00", "-1:30"))

    def test_large_hours_and_minutes(self):
        self.assertEqual("113:35", self.calculator.add("111:155"))

    def test_skip_empty_strings(self):
        self.assertEqual("01:00", self.calculator.add("1:00", ""))
        self.assertEqual("02:00", self.calculator.add("1:00", "", "1:00"))
        self.assertEqual("02:00", self.calculator.add("1:00", "   ", "1:00"))

    def test_ignore_blank_spaces_arround_hour_strings(self):
        self.assertEqual("-2:10", self.calculator.add("   -1:10", "-1:00   "))

    def test_input_hours_as_array(self):
        self.assertEqual("-1:20", self.calculator.add(*[u'1:00', u'-2:20']))

    def test_decimal_inputs(self):
        self.assertEqual("01:30", self.calculator.add("1.5"))
        self.assertEqual("01:12", self.calculator.add("1.2"))
        self.assertEqual("04:42", self.calculator.add("4.7"))
        self.assertEqual("02:42", self.calculator.add("1.2", "1.5"))
    
    def test_negative_decimal_inputs(self):
        self.assertEqual("-4:42", self.calculator.add("-4.7"))
        self.assertEqual("-00:18", self.calculator.add("1.2", "-1.5"))
    
    def test_round_down_decimal_inputs(self):
        self.assertEqual("00:58", self.calculator.add("0.97"))
        self.assertEqual("00:13", self.calculator.add("0.23"))

    def test_integration(self):
        self.assertEqual("05:02", self.calculator.add("1:65", "-1.00", '4.70', '-0.75'))

    def test_skip_invalid_inputs(self):
        self.assertEqual("00:00", self.calculator.add("1:1:65"))
        self.assertEqual("01:00", self.calculator.add("aaa", '1:00'))
        self.assertEqual("01:00", self.calculator.add("1:00", 'a:0b'))
