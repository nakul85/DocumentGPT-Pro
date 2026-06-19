from utils.summarizer import generate_document_summary
from utils.question_generator import generate_suggested_questions


def analyze_document(document_text: str):

    print("STEP 1")

    summary = generate_document_summary(document_text)

    print("STEP 2")

    questions = generate_suggested_questions(document_text)

    print("STEP 3")

    return {
        "summary": summary,
        "questions": questions
    }