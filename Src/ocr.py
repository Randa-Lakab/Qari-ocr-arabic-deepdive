QARI_MODEL = "NAMAA-Space/Qari-OCR-0.2.2.1-VL-2B-Instruct"


def load_qari_ocr():
    """
    Load the Qari-OCR model using the Hugging Face pipeline.
    """
    from transformers import pipeline

    return pipeline(
        "image-text-to-text",
        model=QARI_MODEL,
    )


def extract_ocr_text(result):
    """
    Extract recognized text from common Hugging Face pipeline outputs.
    """

    if isinstance(result, str):
        return result.strip()

    if isinstance(result, list):
        if not result:
            return ""

        return extract_ocr_text(result[0])

    if isinstance(result, dict):
        if "generated_text" in result:
            generated_text = result["generated_text"]

            if isinstance(generated_text, str):
                return generated_text.strip()

            if isinstance(generated_text, list):
                for item in reversed(generated_text):
                    if isinstance(item, dict) and item.get("role") == "assistant":
                        content = item.get("content", "")
                        if isinstance(content, str):
                            return content.strip()

            return ""

        if "text" in result:
            return str(result["text"]).strip()

    raise ValueError("Unexpected OCR pipeline output format.")


def run_qari_ocr(
    ocr_pipe,
    image,
    instruction=None,
    max_new_tokens=512,
    do_sample=False,
    temperature=None,
):
    """
    Run Qari-OCR on an image and return the recognized text.
    """

    if instruction is None:
        instruction = (
            "Perform OCR on the image and return the Arabic text."
        )

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "url": image,
                },
                {
                    "type": "text",
                    "text": instruction,
                },
            ],
        }
    ]

    generation_kwargs = {
        "max_new_tokens": max_new_tokens,
        "do_sample": do_sample,
    }

    if temperature is not None and do_sample:
        generation_kwargs["temperature"] = temperature

    result = ocr_pipe(
        text=messages,
        **generation_kwargs,
    )

    return extract_ocr_text(result)
