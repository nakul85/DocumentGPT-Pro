import os

from pypdf import PdfReader
from docx import Document


def load_document(file_path):
    """
    Load text from PDF, DOCX or TXT.
    """

    extension = os.path.splitext(file_path)[1].lower()

    text = ""

    if extension == ".pdf":

        reader = PdfReader(file_path)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    elif extension == ".docx":

        doc = Document(file_path)

        for para in doc.paragraphs:

            text += para.text + "\n"

    elif extension == ".txt":

        with open(file_path, "r", encoding="utf-8") as f:

            text = f.read()

    else:

        raise ValueError("Unsupported File Type")

    return text