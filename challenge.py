"""
AI Internship Take-Home Challenge — Plain Python Version

Complete the following pipeline:
1. Load each image from /data/
2. Extract all visible Finnish text
3. Translate to English
4. Draw the translated text back onto the image
5. Save the result to /output/
"""

# You may use any open-source library that runs offline
# Examples: PIL, pytesseract, transformers, etc.


def extract_text(image_path):
    # TODO: Perform OCR on the image (e.g. pytesseract)
    raise NotImplementedError


def translate_text(text):
    # TODO: Translate Finnish to English using a local model (e.g. Helsinki-NLP/opus-mt-fi-en)
    raise NotImplementedError


def render_translated_text(image_path, translated_blocks):
    # TODO: Reinsert translated text into the image and save result
    raise NotImplementedError


def main():
    # TODO: Loop through images in /data/, call extract -> translate -> render for each
    # Save output to /output/image_xx_en.png
    pass


if __name__ == "__main__":
    main()
