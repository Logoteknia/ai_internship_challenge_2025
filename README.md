# AI Internship Take-Home Challenge (Offline-Capable Models Only)

This challenge is part of the application process for the AI Engineering Internship – Summer 2025.

Your task is to translate Finnish-language images into English by extracting, translating, and re-embedding the text — all using models and tools that are fully accessible and modifiable.

---

## Your Objective

1. Extract all Finnish text from the provided image(s).
2. Translate the text into English using an offline-capable model.
3. Render the English translation back into the image, preserving layout.
4. Submit your code final images, and a short explanation of your process.

---

## Requirements

-   You may **only use models and libraries that can be downloaded and run or fine-tuned locally**, even if your code pulls them live (e.g. from Hugging Face).
-   **Proprietary cloud APIs are not allowed.** This includes services like Google Translate, OpenAI, DeepL, Azure, or similar. While tools like GitHub Copilot are allowed during development, your final solution must run **entirely offline**, using only installable packages (via `pip`, `apt`, etc.).
-   You are free to use tools like `pytesseract`, `easyocr`, `TrOCR`, and open Hugging Face models (e.g. `Helsinki-NLP/opus-mt-fi-en`).
-   Your solution **must not require API keys, authentication tokens, or paid subscriptions** to function.

> The goal is reproducibility and offline compatibility. We should be able to evaluate your submission without creating accounts or setting up secrets.

---

## Included

-   `data/` – Sample images of varying difficulty for OCR + translation
-   `expected/evaluation_data.json` – Ground truth Finnish strings (can be used for OCR and translation evaluation)
-   `output/` – Final translated images with text rendered back in layout
-   `challenge.py` – Starter plain Python solution (can include other files if needed)
-   `challenge.ipynb` – Starter notebook solution (can include other files if needed)
-   `EXPLANATION.md` – Short write-up of your approach and process

The starter files are only examples, you can use the provided structure or organize the code and change imports in the way you wish, following the requirements above.

---

## Included

-   data/ : Test case images of varying difficulty
-   expected/evaluation_data.json : OCR ground truth results, can be used also for translation ground truth (via model)
-   output/ : Final translated images
-   challenge.py : your solution, can include other files if desired.
-   EXPLANATION.md : Description of your solution and process

## Deliverables

-   Your code in a script or notebook
-   Final translated image files (matching original filenames)
-   `EXPLANATION.md` — write briefly what you did and why
-   Installation instructions, requirements.txt for venv etc.
-   We must be able to run your code in Kaggle/Colab or VM so
    include dependencies and installation instructions.

---

## Examples of allowed tools and libraries

| Purpose       | Library / Model Examples                        |
| ------------- | ----------------------------------------------- |
| OCR           | `pytesseract`, `easyocr`, `TrOCR`               |
| Translation   | `Helsinki-NLP/opus-mt-fi-en` via `transformers` |
| Image Editing | `Pillow`, `OpenCV`, `matplotlib`                |
| Fine-tuning   | `transformers`, `datasets`, `PEFT`, `LoRA`      |

---

## Bonus

-   Add a correction prompt/interface where the user can modify translations and regenerate output
-   Fine-tune the translation model on synthetic or manually aligned examples
-   Add a metric to assess the correctness of translations
-   Attempt to match the translation font, color, background etc. to the original image.

---

## Important Note

We don’t expect perfect results — this is a tough challenge, and in many cases, your solution will likely fail in amusing ways. That’s okay.
What we’re really interested in is how you approach the problem, what tradeoffs you make, and how clearly you explain your reasoning.

Show us your process. Tell us what worked, what didn’t, and what you'd improve with more time or data.

---

## Questions?

If anything is unclear, explain your reasoning in the explanation file — we value engineering judgment and creativity more than perfection.

## Disclaimer

By submitting your solution to this challenge, you agree to the following:

You confirm that the submitted code and materials are your own original work or based on openly licensed components (e.g. MIT, Apache 2.0, CC0).

You grant Logoteknia Oy a non-exclusive, royalty-free, worldwide license to evaluate, review, and test your submission for recruitment purposes.

You understand that similar ideas or implementations may be developed independently by others or already exist in our codebase.

Submission does not grant Logoteknia Oy ownership or commercial rights unless separately agreed in writing.
