def score_skills(skills):
    """Assigns score based on number of skills (Max 40)."""
    return min(len(skills) * 2, 40)

def score_experience(experience):
    """Assigns score based on years of experience (Max 30)."""
    return min(experience * 5, 30)

def score_projects(projects):
    """Assigns score based on project quality (Max 30)."""
    high_value_tech = {"machine learning", "deep learning", "ai", "nlp", "data science",
                       "cloud computing", "aws", "docker", "kubernetes", "flask", "django"}
    
    score = sum(10 for project in projects if any(tech in project.lower() for tech in high_value_tech))
    return min(score, 30)

def calculate_final_score(skills, experience, projects):
    """Calculates the final score out of 100."""
    return score_skills(skills) + score_experience(experience) + score_projects(projects)
