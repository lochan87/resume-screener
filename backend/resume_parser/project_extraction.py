import re

def extract_projects(text):
    """Extracts project details from resume text."""
    project_keywords = ["project", "developed", "built", "created", "designed", "implemented", "worked", "deployed"]
    return [line.strip() for line in text.split("\n") if any(k in line.lower() for k in project_keywords)]

def score_projects(projects):
    """Scores projects based on technology relevance."""
    high_value_tech = {"machine learning", "deep learning", "ai", "nlp", "data science", 
                       "cloud computing", "aws", "docker", "kubernetes", "flask", "django"}

    score = sum(10 for project in projects if any(tech in project.lower() for tech in high_value_tech))
    return min(score, 30)  # Max project score is 30
