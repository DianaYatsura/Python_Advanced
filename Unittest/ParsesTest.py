import unittest
from unittest.mock import patch, mock_open


def file_parser(file_path, find_str, replace_str=None):
    with open(file_path, 'r') as f:
        data = f.read()

    count = data.count(find_str)

    if replace_str is None:
        return f"Found {count} strings"

    update_data = data.replace(find_str, replace_str)
    with open(file_path, 'w') as f:
        f.write(update_data)

    return f"Replaced {count} strings"



class ParserTest(unittest.TestCase):

    def test_file_parser_found(self):
        test_data = "split strip upper lower split"
        m = mock_open(read_data=test_data)
        with patch("builtins.open", m):
            result = file_parser("test.txt", "split")
            self.assertEqual(result, "Found 2 strings")

    def test_file_parser_replace(self):
        test_data = "isalnum lower isalpha isdecimal isdigit lower istitle"
        m = mock_open(read_data=test_data)
        with patch("builtins.open", m):
            result = file_parser("test.txt", "lower", "islower")
            self.assertEqual(result, "Replaced 2 strings")
            handle = m()
            handle.write.assert_called_with("isalnum islower isalpha isdecimal isdigit islower istitle")



try:
    file_parser('pars.txt', 'better')
except FileNotFoundError as e:
    print('File is not exist') #File is not exist