import unittest
from unittest.mock import patch
from data_processor import input_integers, input_floats, input_string


class TestInputIntegers(unittest.TestCase):

    @patch("builtins.input", return_value="1 2 3 4 5")
    def test_valid_positive(self, _):
        self.assertEqual(input_integers(), [1, 2, 3, 4, 5])

    @patch("builtins.input", return_value="-1 -2 -3")
    def test_valid_negative(self, _):
        self.assertEqual(input_integers(), [-1, -2, -3])

    @patch("builtins.input", return_value="42")
    def test_single_value(self, _):
        self.assertEqual(input_integers(), [42])

    @patch("builtins.input", return_value="0 0 0")
    def test_zeros(self, _):
        self.assertEqual(input_integers(), [0, 0, 0])

    @patch("builtins.input", return_value="abc")
    def test_invalid_raises_value_error(self, _):
        with self.assertRaises(ValueError):
            input_integers()

    @patch("builtins.input", return_value="1 2.5 3")
    def test_float_in_int_input_raises(self, _):
        with self.assertRaises(ValueError):
            input_integers()

    @patch("builtins.input", return_value="")
    def test_empty_input_returns_empty_list(self, _):
        self.assertEqual(input_integers(), [])

    @patch("builtins.input", return_value="100 200 300")
    def test_custom_prompt(self, mock_input):
        result = input_integers("Введите: ")
        mock_input.assert_called_once_with("Введите: ")
        self.assertEqual(result, [100, 200, 300])


class TestInputFloats(unittest.TestCase):

    @patch("builtins.input", return_value="1.1 2.2 3.3")
    def test_valid_floats(self, _):
        result = input_floats()
        self.assertAlmostEqual(result[0], 1.1)
        self.assertAlmostEqual(result[1], 2.2)
        self.assertAlmostEqual(result[2], 3.3)

    @patch("builtins.input", return_value="-1.5 0.0 3.14")
    def test_mixed_floats(self, _):
        result = input_floats()
        self.assertEqual(len(result), 3)
        self.assertAlmostEqual(result[2], 3.14)

    @patch("builtins.input", return_value="1 2 3")
    def test_integers_accepted_as_floats(self, _):
        result = input_floats()
        self.assertEqual(result, [1.0, 2.0, 3.0])

    @patch("builtins.input", return_value="3.14")
    def test_single_float(self, _):
        self.assertEqual(input_floats(), [3.14])

    @patch("builtins.input", return_value="abc")
    def test_invalid_raises_value_error(self, _):
        with self.assertRaises(ValueError):
            input_floats()

    @patch("builtins.input", return_value="")
    def test_empty_input_returns_empty_list(self, _):
        self.assertEqual(input_floats(), [])

    @patch("builtins.input", return_value="1.0 2.0")
    def test_custom_prompt(self, mock_input):
        result = input_floats("Введите: ")
        mock_input.assert_called_once_with("Введите: ")
        self.assertEqual(result, [1.0, 2.0])


class TestInputString(unittest.TestCase):

    @patch("builtins.input", return_value="hello world")
    def test_basic_string(self, _):
        self.assertEqual(input_string(), "hello world")

    @patch("builtins.input", return_value="")
    def test_empty_string(self, _):
        self.assertEqual(input_string(), "")

    @patch("builtins.input", return_value="  пробелы  ")
    def test_whitespace_preserved(self, _):
        self.assertEqual(input_string(), "  пробелы  ")

    @patch("builtins.input", return_value="racecar")
    def test_palindrome_string(self, _):
        self.assertEqual(input_string(), "racecar")

    @patch("builtins.input", return_value="12345")
    def test_numeric_string(self, _):
        self.assertEqual(input_string(), "12345")

    @patch("builtins.input", return_value="hello")
    def test_custom_prompt(self, mock_input):
        result = input_string("Введите: ")
        mock_input.assert_called_once_with("Введите: ")
        self.assertEqual(result, "hello")


if __name__ == "__main__":
    unittest.main()
