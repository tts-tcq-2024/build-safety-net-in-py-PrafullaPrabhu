import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_simple_name(self):
        self.assertEqual(generate_soundex("Smith"), "S530")

    def test_name_with_vowels(self):
        self.assertEqual(generate_soundex("Aebersold"), "A162")

    def test_repeated_characters(self):
        self.assertEqual(generate_soundex("Ashcraft"), "A261")

    def test_name_with_same_sounds(self):
        self.assertEqual(generate_soundex("Pfister"), "P236")

    def test_name_with_no_mapped_characters(self):
        self.assertEqual(generate_soundex("Aeiou"), "A000")

    def test_name_exceeds_max_length(self):
        self.assertEqual(generate_soundex("Washington"), "W252")

    def test_name_with_mixed_case(self):
        self.assertEqual(generate_soundex("WaShInGtOn"), "W252")

    def test_name_with_non_alphabetic_characters(self):
        self.assertEqual(generate_soundex("H@ll3"), "H400")

    def test_name_with_only_non_mapped_characters(self):
        self.assertEqual(generate_soundex("123"), "1000")
        

if __name__ == '__main__':
    unittest.main()
