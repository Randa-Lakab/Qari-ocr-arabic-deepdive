# Experiments

This file contains documentation related to the experiments conducted during the Qari-OCR deep dive.

The experiments focus on evaluating the Qari-OCR model on different types of Arabic text and testing how different prompting and generation settings affect OCR output.

## Experiments Performed

### 1. Printed Arabic Text

Qari-OCR was tested on printed Arabic text to establish a baseline for OCR performance.

### 2. Complex Two-Column Layout

The model was tested on Arabic documents containing a two-column layout to examine its ability to recognize text when the page structure is more complex.

### 3. Historical Handwritten Arabic

The model was evaluated on historical handwritten Arabic samples from the **Muharaf** dataset.

The experiment was used to explore the challenges of OCR on historical and handwritten Arabic text.

### 4. Printed vs. Historical Arabic

The OCR results from printed Arabic and historical handwritten Arabic were compared using:

* Strict Character Error Rate (CER)
* Normalized Character Error Rate (CER)

This comparison helps identify how OCR performance changes across different text domains.

### 5. Instruction Variants

Different OCR instructions were tested to observe their effect on the generated text.

The tested instruction variants included:

* `bare`
* `default_detailed`
* `preserve_layout`

### 6. Generation Parameter Tests

Different generation settings were also explored, including:

* `do_sample`
* `temperature`
* `max_new_tokens`

These experiments were used to examine how generation parameters can influence OCR output.

## Evaluation

The main evaluation metric used in the experiments is **Character Error Rate (CER)**.

Two versions were considered:

* **Strict CER:** calculated directly between the ground-truth text and the OCR prediction.
* **Normalized CER:** calculated after applying Arabic text normalization.

## Purpose

The experiments are exploratory and are intended to better understand the behavior and limitations of Qari-OCR on different Arabic OCR scenarios.

The results should be interpreted as experimental observations from the tested samples rather than as a general benchmark of the model.
