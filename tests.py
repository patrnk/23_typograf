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


if __name__ == '__main__':
    unittest.main()
