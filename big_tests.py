import unittest

import utils


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

    def test_number_with_word_inside_tags(self):
        test_string = '<html value="123 asd"></123 html>'
        self.run_test(test_input=test_string, expected_output=test_string)

    def test_number_with_word_beside_tags(self):
        expected_output = '123 asd<html>123 asd</html> 123 asd'
        test_input = '123 asd<html>123 asd</html> 123 asd'
        self.run_test(test_input, expected_output)

    def test_short_word_inside_tags(self):
        test_string = '<html value="a asd"></a html>'
        self.run_test(test_input=test_string, expected_output=test_string)

    def test_short_word_beside_tags(self):
        expected_output = 'a asd<html>a asd</html>a asd'
        test_input = 'a asd<html>a asd</html>a asd'
        self.run_test(test_input, expected_output)


if __name__ == '__main__':
    unittest.main()
