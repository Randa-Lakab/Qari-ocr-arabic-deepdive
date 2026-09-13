import re


ARABIC_DIACRITICS = re.compile(
    r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]"
)


def normalize_arabic(
    text,
    strip_diacritics=True,
    normalize_alef=True,
):
    """
    Normalize Arabic text for OCR evaluation.
    """

    if text is None:
        return ""

    text = str(text).strip()

    if strip_diacritics:
        text = ARABIC_DIACRITICS.sub("", text)

    if normalize_alef:
        text = re.sub(
            r"[إأآٱ]",
            "ا",
            text,
        )

    return text