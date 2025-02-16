import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_name(text):
    """Extracts candidate name from resume."""
    lines = text.strip().split("\n")

    # Check top lines for a possible name
    for line in lines[:5]:
        words = line.split()
        if len(words) >= 2 and all(w[0].isupper() for w in words if w.isalpha()):
            return line.strip()

    # Fallback: Use Spacy NER
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON" and len(ent.text.split()) >= 2:
            return ent.text

    return "Unknown"
