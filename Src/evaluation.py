from jiwer import cer
from .preprocessing import normalize_arabic


def cer_strict(reference, prediction):
    return cer(reference, prediction)


def cer_normalized(reference, prediction):
    reference_normalized = normalize_arabic(reference)
    prediction_normalized = normalize_arabic(prediction)

    return cer(reference_normalized, prediction_normalized)


def evaluate_prediction(reference, prediction):
    return {
        "CER_strict": cer_strict(reference, prediction),
        "CER_normalized": cer_normalized(reference, prediction),
    }