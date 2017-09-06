import unittest

import utils


class GuillimentsTestCase(unittest.TestCase):
    def run_test(self, test_input, expected_output):
        test_output = utils.replace_computer_quotation_marks_with_guillemets(test_input)
        self.assertEqual(test_output, expected_output)

    def test_quotes_in_the_middle(self):
        expected_output = 'qwe «asd» qwe'
        self.run_test("qwe 'asd' qwe", expected_output)
        self.run_test('qwe "asd" qwe', expected_output)

    def test_quotes_at_the_beginning(self):
        expected_output = '«asd» qwe'
        self.run_test("'asd' qwe", expected_output)
        self.run_test('"asd" qwe', expected_output)

    def test_quotes_at_the_end(self):
        expected_output = 'qwe «asd»'
        self.run_test("qwe 'asd'", expected_output)
        self.run_test('qwe "asd"', expected_output)

    def test_quotes_with_dot(self):
        expected_output = 'qwe «asd». qwe'
        self.run_test("qwe 'asd'. qwe", expected_output)
        self.run_test('qwe "asd". qwe', expected_output)

    def test_quotes_with_special_characters_in_between(self):
        expected_output = 'qwe «asd? asd!» qwe'
        self.run_test("qwe 'asd? asd!' qwe", expected_output)
        self.run_test('qwe "asd? asd!" qwe', expected_output)

    def test_quotes_between_html_tags(self):
        expected_output = '<html>«asd»</html>'
        self.run_test("<html>'asd'</html>", expected_output)
        self.run_test('<html>"asd"</html>', expected_output)


class EmDashTestCase(unittest.TestCase):
    def run_test(self, test_input, expected_output):
        test_output = utils.replace_hyphen_with_em_dash(test_input)
        self.assertEqual(test_output, expected_output)

    def test_em_dash_in_the_middle(self):
        self.run_test('qwe - asd - qwe', 'qwe — asd — qwe')

    def test_em_dash_at_the_beginning(self):
        self.run_test('- qwe asd.', '— qwe asd.')

    def test_em_dash_at_the_end(self):
        self.run_test('qwe asd -', 'qwe asd —')

    def test_hyphen_between_words(self):
        test_string = 'qwe-asd'
        self.run_test(test_input=test_string, expected_output=test_string)

    def test_hyphen_between_digits(self):
        test_string = '123-456'
        self.run_test(test_input=test_string, expected_output=test_string)


class EnDashTestCase(unittest.TestCase):
    def run_test(self, test_input, expected_output):
        test_output = utils.replace_hyphen_with_en_dash(test_input)
        self.assertEqual(test_output, expected_output)

    def test_en_dash_between_digits(self):
        self.run_test('123-456', '123–456')

    def test_hyphen_at_the_beginning_of_number(self):
        test_string = 'qwe -456 qwe'
        self.run_test(test_input=test_string, expected_output=test_string)

    def test_hyphen_at_the_end_of_number(self):
        test_string = 'qwe -456 qwe'
        self.run_test(test_input=test_string, expected_output=test_string)


class NumbersWithWordsTestCase(unittest.TestCase):
    def run_test(self, test_input, expected_output):
        test_output = utils.tie_numbers_with_words_by_non_breaking_space(test_input)
        self.assertEqual(test_output, expected_output)

    def test_number_with_word(self):
        self.run_test('123 qwe', '123 qwe')


class ShortWordsTestCase(unittest.TestCase):
    def run_test(self, test_input, expected_output):
        test_output = utils.tie_short_words_by_non_breaking_space(test_input)
        self.assertEqual(test_output, expected_output)

    def test_one_letter_word(self):
        self.run_test('qwe a qwe', 'qwe a qwe')

    def test_two_letter_word(self):
        self.run_test('qwe as qwe', 'qwe as qwe')

    def test_two_letter_word_at_the_beginning(self):
        self.run_test('as qwe', 'as qwe')

    def test_long_word(self):
        test_string = 'qwe asdas qwe'
        self.run_test(test_input=test_string, expected_output=test_string)


class RedundantWhitespace(unittest.TestCase):
    def run_test(self, test_input, expected_output):
        test_output = utils.remove_redundant_whitespace(test_input)
        self.assertEqual(test_output, expected_output)

    def test_redundant_spaces_in_the_middle(self):
        self.run_test('asd    asd', 'asd asd')

    def test_redundant_spaces_at_the_beginning(self):
        self.run_test('    asd', 'asd')

    def test_redundant_spaces_at_the_end(self):
        self.run_test('asd   ', 'asd')

    def test_redundant_newlines_in_middle(self):
        self.run_test('asd\n\n\nasd', 'asd\nasd')

    def test_redundant_newlines_at_the_beginning(self):
        self.run_test('\n\nasd', 'asd')

    def test_redundant_newlines_at_the_end(self):
        self.run_test('asd\n\n', 'asd')


if __name__ == '__main__':
    unittest.main()
