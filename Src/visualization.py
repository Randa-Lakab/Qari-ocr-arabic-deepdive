import os
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display


def find_arabic_font():
    candidates = [
        "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf",
        "/usr/share/fonts/truetype/kacst/KacstOne.ttf",
    ]

    for c in candidates:
        if os.path.exists(c):
            return c

    return None


def render_arabic_line(
    text,
    font_path,
    font_size=40,
    pad=20,
    image_size=None
):
    reshaped = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped)

    font = ImageFont.truetype(font_path, font_size)

    if image_size:
        img = Image.new("RGB", image_size, "white")
    else:
        dummy = Image.new("RGB", (10, 10))
        d = ImageDraw.Draw(dummy)

        bbox = d.textbbox(
            (0, 0),
            bidi_text,
            font=font
        )

        w = bbox[2] - bbox[0] + 2 * pad
        h = bbox[3] - bbox[1] + 2 * pad

        img = Image.new("RGB", (w, h), "white")

    d = ImageDraw.Draw(img)

    d.text(
        (pad, pad),
        bidi_text,
        font=font,
        fill="black"
    )

    return img


def render_two_column(
    left_lines,
    right_lines,
    font_path,
    font_size=32,
    pad=20,
    col_gap=60
):
    line_h = font_size + 14
    n_lines = max(len(left_lines), len(right_lines))
    col_w = 420

    img = Image.new(
        "RGB",
        (
            col_w * 2 + col_gap + 2 * pad,
            n_lines * line_h + 2 * pad
        ),
        "white"
    )

    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)

    def draw_column(lines, x0):
        for i, line in enumerate(lines):
            reshaped = arabic_reshaper.reshape(line)
            bidi_text = get_display(reshaped)

            bbox = d.textbbox(
                (0, 0),
                bidi_text,
                font=font
            )

            w = bbox[2] - bbox[0]

            x = x0 + (col_w - w)
            y = pad + i * line_h

            d.text(
                (x, y),
                bidi_text,
                font=font,
                fill="black"
            )

    draw_column(left_lines, pad)
    draw_column(
        right_lines,
        pad + col_w + col_gap
    )

    return img