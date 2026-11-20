
import unittest

from Src.evaluation import (
    cer_strict,
    cer_normalized,
    wer_strict,
    wer_normalized,
    evaluate_prediction,
)


class TestArabicOCREvaluation(unittest.TestCase):

    def test_strict_cer_identical_text(self):
        self.assertEqual(cer_strict("hello world", "hello world"), 0.0)

    def test_normalized_cer(self):
        self.assertEqual(
            cer_normalized("إسلام أحمد", "اسلام احمد"),
            0.0
        )

    def test_strict_wer_identical_text(self):
        self.assertEqual(wer_strict("hello world", "hello world"), 0.0)

    def test_normalized_wer(self):
        self.assertEqual(
            wer_normalized("إسلام أحمد", "اسلام احمد"),
            0.0
        )

    def test_evaluate_prediction_returns_all_metrics(self):
        result = evaluate_prediction("hello world", "hello world")

        self.assertEqual(
            set(result.keys()),
            {
                "CER_strict",
                "CER_normalized",
                "WER_strict",
                "WER_normalized",
            }
        )

        self.assertTrue(all(value == 0.0 for value in result.values()))


if __name__ == "__main__":
    unittest.main()
