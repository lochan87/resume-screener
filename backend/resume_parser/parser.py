from resume_parser.text_extraction import extract_text_from_pdf
from resume_parser.name_extraction import extract_name
from resume_parser.skill_extraction import extract_skills
from resume_parser.experience_extraction import extract_experience
from resume_parser.project_extraction import extract_projects
from resume_parser.scoring import calculate_final_score

def parse_resume(pdf_file):
    """Parses resume and calculates score."""
    text = extract_text_from_pdf(pdf_file)
    name = extract_name(text)
    skills = extract_skills(text)
    experience = extract_experience(text)
    projects = extract_projects(text)
    final_score = calculate_final_score(skills, experience, projects)

    return {
        'name': name,
        'skills': skills,
        'experience': experience,
        'projects': projects,
        'score': final_score
    }
