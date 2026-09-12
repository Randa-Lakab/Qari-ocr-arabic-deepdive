# Arabic OCR — Qari-OCR Deep Dive

A practical deep dive into Arabic Optical Character Recognition (OCR) using **Qari-OCR**, with experiments covering printed Arabic text, complex layouts, historical handwritten Arabic, Arabic text normalization, OCR evaluation, instruction prompting, and generation parameters.

## Project Overview

This project explores the capabilities and limitations of Qari-OCR for Arabic text recognition.

The main goal is to understand how well the model performs on different types of Arabic documents and how preprocessing, instructions, and generation parameters affect OCR results.

The project focuses particularly on challenging Arabic OCR cases, including historical handwritten Arabic documents.

## Model

The OCR model used in this project is:

**NAMAA-Space/Qari-OCR-0.2.2.1-VL-2B-Instruct**

The model is loaded using the Hugging Face Transformers pipeline for image-to-text OCR inference.

## Experiments

The notebook contains the following experiments:

### 1. Environment Setup

- GPU availability check
- Required Python packages
- Model and utility imports
- Project folder setup

### 2. Qari-OCR Loading

The Qari-OCR model is loaded and configured for Arabic OCR inference.

### 3. OCR Smoke Test

A simple OCR test is performed to verify that the model is correctly loaded and able to recognize Arabic text from an image.

### 4. Printed Arabic Benchmark

Printed Arabic text is generated and used to test the OCR model.

The benchmark examines the model's ability to recognize clean Arabic text.

### 5. Complex Arabic Layout

The project also tests OCR on more complex document layouts, including multi-column Arabic text.

### 6. Historical Handwritten Arabic

The project uses the **Muharaf** dataset to investigate OCR performance on historical handwritten Arabic.

This experiment is particularly important because historical Arabic documents present challenges that are different from clean modern printed text.

### 7. Arabic Text Normalization

Arabic OCR predictions are normalized before evaluation.

The preprocessing includes operations such as:

- Removing Arabic diacritics
- Normalizing Arabic Alef forms
- Preparing text for normalized comparison

Both strict and normalized evaluation are considered.

### 8. OCR Evaluation

The project uses **Character Error Rate (CER)** to evaluate OCR predictions.

Two types of comparison are considered:

- Strict CER
- Normalized CER

This allows the effect of Arabic text normalization on OCR evaluation to be examined.

### 9. OCR Instruction Experiments

Different instructions/prompts are tested to investigate whether the model's OCR output changes depending on how the task is described.

The experiments include instruction variants such as:

- Bare OCR instruction
- Detailed OCR instruction
- Layout-preserving instruction

### 10. Generation Parameter Experiments

The project also investigates generation settings such as:

- `do_sample`
- `temperature`
- `max_new_tokens`

The purpose is to understand how generation configuration affects OCR output.

## Project Structure

```text
Arabic-OCR-Qari/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks/
│   └── Arabic_OCR_Qari_DeepDive.ipynb
│
├── src/
│   ├── __init__.py
│   ├── ocr.py
│   ├── preprocessing.py
│   ├── dataset.py
│   ├── evaluation.py
│   └── visualization.py
│
├── data/
│   └── README.md
│
└── experiments/
    └── README.md