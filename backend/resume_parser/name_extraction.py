import re
import nltk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")

from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tree import Tree

def extract_name(text):
    """Extracts candidate name from resume using NLTK NER."""
    lines = text.strip().split("\n")

    # 1️⃣ **Check Top Lines for a Possible Name**
    for line in lines[:5]:
        words = line.split()
        if len(words) >= 2 and all(w[0].isupper() for w in words if w.isalpha()):
            return line.strip()

    # 2️⃣ **Use NLTK Named Entity Recognition (NER)**
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    named_entities = ne_chunk(tagged_words, binary=False)

    for subtree in named_entities:
        if isinstance(subtree, Tree) and subtree.label() == "PERSON":
            return " ".join([token for token, pos in subtree.leaves()])

    return "Unknown"
