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


class HTMLTagsTestCase(unittest.TestCase):
    def run_test(self, test_input, expected_output):
        test_output = utils.typograph_text(test_input)
        self.assertEqual(test_output, expected_output)

    def test_quotation_marks_inside_tags(self):
        test_string = '<html attr="qwe \'asd\' qwe"></ht"m"l>'
        self.run_test(test_input=test_string, expected_output=test_string)

    def test_quotation_marks_beside_tags(self):
        expected_output = '«asd» <html>«asd»</html> «asd» qwe'
        test_input = '"asd" <html>"asd"</html> \'asd\' qwe'
        self.run_test(test_input, expected_output)

    def test_em_dash_inside_tags(self):
        test_string = '<html value="q - a"></html>'
        self.run_test(test_input=test_string, expected_output=test_string)

    def test_em_dash_beside_tags(self):
        expected_output = '— <html>q — a</html> —'
        test_input = '- <html>q - a</html> -'
        self.run_test(test_input, expected_output)

    def test_en_dash_inside_tags(self):
        test_string = '<html value="0-1"></html>'
        self.run_test(test_input=test_string, expected_output=test_string)

    def test_en_dash_beside_tags(self):
        expected_output = '123–456 <html>123–456</html> 123–456'
        test_input = '123-456 <html>123-456</html> 123-456'
        self.run_test(test_input, expected_output)


if __name__ == '__main__':
    unittest.main()
