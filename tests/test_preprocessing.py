
import unittest

from Src.preprocessing import normalize_arabic


class TestArabicPreprocessing(unittest.TestCase):

    def test_remove_diacritics(self):
        self.assertEqual(
            normalize_arabic("مُحَمَّد"),
            "محمد"
        )

    def test_normalize_alef_variants(self):
        self.assertEqual(
            normalize_arabic("إسلام أمل آمنة ٱ"),
            "اسلام امل امنة ا"
        )

    def test_none_input(self):
        self.assertEqual(normalize_arabic(None), "")

    def test_empty_input(self):
        self.assertEqual(normalize_arabic(""), "")

    def test_preserve_diacritics(self):
        self.assertEqual(
            normalize_arabic("مُحَمَّد", strip_diacritics=False),
            "مُحَمَّد"
        )

    def test_disable_alef_normalization(self):
        self.assertEqual(
            normalize_arabic("إسلام", normalize_alef=False),
            "إسلام"
        )

    def test_strip_whitespace(self):
        self.assertEqual(
            normalize_arabic("  مرحبا  "),
            "مرحبا"
        )


if __name__ == "__main__":
    unittest.main()
