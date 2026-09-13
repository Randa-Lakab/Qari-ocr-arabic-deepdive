from transformers import pipeline


QARI_MODEL = "NAMAA-Space/Qari-OCR-0.2.2.1-VL-2B-Instruct"


def load_qari_ocr():
    """
    Load the Qari-OCR model using the Hugging Face pipeline.
    """
    ocr_pipe = pipeline(
        "image-text-to-text",
        model=QARI_MODEL,
    )

    return ocr_pipe


def run_qari_ocr(
    ocr_pipe,
    image,
    instruction=None,
    max_new_tokens=512,
    do_sample=False,
    temperature=None,
):
    """
    Run Qari-OCR on an image.

    Parameters
    ----------
    ocr_pipe:
        Loaded Qari-OCR pipeline.

    image:
        Image path or image object.

    instruction:
        OCR instruction/prompt.

    max_new_tokens:
        Maximum number of generated tokens.

    do_sample:
        Whether sampling is enabled.

    temperature:
        Generation temperature when sampling is enabled.

    Returns
    -------
    str
        OCR prediction.
    """

    if instruction is None:
        instruction = (
            "Perform OCR on the image and return the Arabic text."
        )

    generation_kwargs = {
        "max_new_tokens": max_new_tokens,
        "do_sample": do_sample,
    }

    if temperature is not None:
        generation_kwargs["temperature"] = temperature

    # Keep the actual message/input structure from your notebook here.
    # This function should contain the inference code currently used
    # in Arabic_OCR_Qari_DeepDive.ipynb.

    result = ocr_pipe(
        image,
        prompt=instruction,
        **generation_kwargs,
    )

    return result