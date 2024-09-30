import unittest

def elementCounter(word):
    result = {}
    if not isinstance(word, str):
        raise TypeError("Input must be a string")

    word = word.replace(" ", "")  # Remove spaces
    for char in word:
        result[char] = result.get(char, 0) + 1
    return result



class TestElementCounter(unittest.TestCase):
    

    '''
    A set of unit tests for this function.
    
    1. string
    2. string with repeated characters
    3. string with spaces
    4. string with case sensitive
    5. empty/None
    4. Non string

    '''
    def test_character(self):
        """Test when the input is string only  """
        self.assertEqual(elementCounter('abc'), {'a': 1,'b':1,'c':1})
    
    def test_repeated_characters(self):
        """Test when the input contains repeated characters."""
        self.assertEqual(elementCounter('aaa'), {'a': 3})
    
    def test_input_with_spaces(self):
        """Test when the input contains spaces."""
        self.assertEqual(elementCounter('a b c'), {'a': 1, 'b': 1, 'c': 1})
     
    def test_case_sensitive(self):
        """Test that the input contains case-sensitive."""
        self.assertEqual(elementCounter('AaAa'), {'A': 2, 'a': 2})

    def test_empty_string(self):
        """Test when the input is an empty string."""
        self.assertEqual(elementCounter(''), {})
    
    def test_non_string_input(self):
        """Test that a TypeError is raised for non-string input."""
        with self.assertRaises(TypeError):
            elementCounter(123)
    

if __name__ == "__main__":
    unittest.main()
