import re

# Predefined technical skills
PREDEFINED_SKILLS = {
    "python", "java", "c++", "c", "machine learning", "deep learning", "nlp", "data science",
    "html", "css", "javascript", "react", "angular", "node.js", "flask", "django",
    "sql", "mongodb", "postgresql", "cloud computing", "aws", "azure", "docker", "kubernetes",
    "tensorflow", "pytorch", "git", "linux", "bash", "api", "rest api", "microservices", "agile",
    "scrum", "kanban", "jira", "confluence", "gitlab", "github", "bitbucket", "data analysis",
    "data visualization", "tableau", "power bi", "excel", "pandas", "numpy", "scikit-learn",
    "matplotlib", "seaborn", "opencv", "computer vision", "image processing", "object detection",
    "natural language processing", "nltk", "spacy", "gensim", "word2vec", "bag of words",
    "tf-idf", "n-grams", "sentiment analysis", "text classification", "sequence tagging",
    "named entity recognition", "question answering", "text summarization", "topic modeling",
    "machine translation", "speech recognition", "ocr", "chatbot", "data engineering",
    "etl", "data warehousing", "data modeling", "data integration", "data governance",
    "cryptography", "web application security", "network security", "penetration testing",
    "app development", "web development", "mobile development", "full stack", "frontend",
    "backend", "ui/ux", "progressive web apps", "single page applications","graphql",
    "websockets", "push notifications", "authentication", "latex", "markdown", "agile",
    "power bi", "tableau", "excel", "data mining", "data wrangling", "data preprocessing"
}

def extract_skills(text):
    text = text.lower()  # Convert to lowercase
    words = text.split()  # Tokenize by splitting on spaces
    extracted_skills = set()

    # Check for multi-word skills first
    for skill in PREDEFINED_SKILLS:
        if skill in text:
            extracted_skills.add(skill)

    # Check for single-word skills
    for word in words:
        if word in PREDEFINED_SKILLS:
            extracted_skills.add(word)

    return list(extracted_skills)  # Return unique skills
