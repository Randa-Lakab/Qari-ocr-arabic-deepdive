import unittest

from Src.ocr import extract_ocr_text, run_qari_ocr


class TestOCR(unittest.TestCase):

    def test_extract_text_from_string(self):
        arabic_text = "\u0645\u0631\u062D\u0628\u0627 \u0628\u0627\u0644\u0639\u0627\u0644\u0645"

        self.assertEqual(
            extract_ocr_text(arabic_text),
            arabic_text
        )

    def test_extract_generated_text(self):
        result = [{"generated_text": "Recognized text"}]

        self.assertEqual(
            extract_ocr_text(result),
            "Recognized text"
        )

    def test_extract_assistant_message(self):
        result = [
            {
                "generated_text": [
                    {"role": "user", "content": "Image"},
                    {"role": "assistant", "content": "OCR result"},
                ]
            }
        ]

        self.assertEqual(
            extract_ocr_text(result),
            "OCR result"
        )

    def test_empty_result(self):
        self.assertEqual(extract_ocr_text([]), "")

    def test_unexpected_output(self):
        with self.assertRaises(ValueError):
            extract_ocr_text(123)

    def test_run_qari_ocr(self):
        class MockPipeline:
            def __call__(self, **kwargs):
                return [{"generated_text": "Arabic OCR text"}]

        result = run_qari_ocr(
            MockPipeline(),
            "image.jpg",
        )

        self.assertEqual(result, "Arabic OCR text")


if __name__ == "__main__":
    unittest.main()