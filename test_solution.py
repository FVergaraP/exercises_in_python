import unittest
import solution


class TestSolution(unittest.TestCase):

    def test_ex953_normal_text(self):
        """Test with a normal string"""
        text = "This is a test text"
        hash_character = solution.ex953(text)
        expect = {
            't': 'text',
            'h': 'this',
            'i': 'this',
            's': 'test',
            'a': 'a',
            'e': 'text',
            'x': 'text'
        }
        self.assertEqual(hash_character, expect)

    def test_ex953_empty_text(self):
        """Test with empty string"""
        self.assertEqual(solution.ex953(""), {})


if __name__ == '__main__':
    unittest.main()
