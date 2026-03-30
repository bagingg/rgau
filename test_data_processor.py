"""
Тесты для модуля data_processor.py
ПЗ 5 — Основы работы с Git
"""
import pytest
from data_processor import (
    sum_integers, average_integers, max_integer, min_integer,
    filter_even, filter_odd, sort_integers,
    sum_floats, average_floats, round_floats,
    reverse_string, count_words, to_upper, to_lower,
    is_palindrome, count_char, words_list,
)


# ── Целые числа ────────────────────────────────────────────────────

class TestSumIntegers:
    def test_positive(self):
        assert sum_integers([1, 2, 3, 4, 5]) == 15

    def test_negative(self):
        assert sum_integers([-1, -2, -3]) == -6

    def test_mixed(self):
        assert sum_integers([-5, 5]) == 0

    def test_single(self):
        assert sum_integers([42]) == 42

    def test_empty(self):
        assert sum_integers([]) == 0


class TestAverageIntegers:
    def test_basic(self):
        assert average_integers([1, 2, 3, 4, 5]) == 3.0

    def test_two_elements(self):
        assert average_integers([10, 20]) == 15.0

    def test_single(self):
        assert average_integers([7]) == 7.0

    def test_negative(self):
        assert average_integers([-4, -2]) == -3.0

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            average_integers([])


class TestMaxMinIntegers:
    def test_max(self):
        assert max_integer([3, 1, 4, 1, 5, 9]) == 9

    def test_min(self):
        assert min_integer([3, 1, 4, 1, 5, 9]) == 1

    def test_max_negative(self):
        assert max_integer([-10, -3, -7]) == -3

    def test_min_negative(self):
        assert min_integer([-10, -3, -7]) == -10

    def test_single(self):
        assert max_integer([0]) == 0
        assert min_integer([0]) == 0


class TestFilterEvenOdd:
    def test_filter_even(self):
        assert filter_even([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    def test_filter_odd(self):
        assert filter_odd([1, 2, 3, 4, 5, 6]) == [1, 3, 5]

    def test_all_even(self):
        assert filter_even([2, 4, 6]) == [2, 4, 6]

    def test_all_odd(self):
        assert filter_odd([1, 3, 5]) == [1, 3, 5]

    def test_empty(self):
        assert filter_even([]) == []
        assert filter_odd([]) == []

    def test_negative_even(self):
        assert filter_even([-2, -3, -4]) == [-2, -4]


class TestSortIntegers:
    def test_asc(self):
        assert sort_integers([3, 1, 2]) == [1, 2, 3]

    def test_desc(self):
        assert sort_integers([3, 1, 2], reverse=True) == [3, 2, 1]

    def test_already_sorted(self):
        assert sort_integers([1, 2, 3]) == [1, 2, 3]

    def test_single(self):
        assert sort_integers([5]) == [5]

    def test_empty(self):
        assert sort_integers([]) == []


# ── Вещественные числа ─────────────────────────────────────────────

class TestFloats:
    def test_sum(self):
        assert abs(sum_floats([1.1, 2.2, 3.3]) - 6.6) < 1e-9

    def test_average(self):
        assert abs(average_floats([1.0, 3.0]) - 2.0) < 1e-9

    def test_round(self):
        # Python использует банковское округление: 1.555 -> 1.55 (round half to even)
        assert round_floats([1.555, 2.444], 2) == [1.55, 2.44]

    def test_round_default(self):
        assert round_floats([3.14159]) == [3.14]

    def test_average_empty_raises(self):
        with pytest.raises(ValueError):
            average_floats([])


# ── Строки ─────────────────────────────────────────────────────────

class TestStrings:
    def test_reverse(self):
        assert reverse_string("hello") == "olleh"

    def test_reverse_empty(self):
        assert reverse_string("") == ""

    def test_count_words(self):
        assert count_words("hello world foo") == 3

    def test_count_words_single(self):
        assert count_words("word") == 1

    def test_to_upper(self):
        assert to_upper("hello") == "HELLO"

    def test_to_lower(self):
        assert to_lower("HELLO") == "hello"

    def test_is_palindrome_true(self):
        assert is_palindrome("racecar") is True

    def test_is_palindrome_with_spaces(self):
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_is_palindrome_false(self):
        assert is_palindrome("hello") is False

    def test_count_char(self):
        assert count_char("hello world", "l") == 3

    def test_count_char_not_found(self):
        assert count_char("hello", "z") == 0

    def test_words_list(self):
        assert words_list("one two three") == ["one", "two", "three"]
