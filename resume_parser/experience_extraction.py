import re

def extract_experience(text):
    """
    Extracts years of experience from the resume text.
    Uses patterns like 'X years of experience' and job titles.
    """

    # Common job-related keywords
    job_titles = [
        "intern", "internship", "developer", "engineer", "analyst", "consultant",
        "specialist", "manager", "lead", "architect", "scientist", "administrator",
        "executive", "officer", "coordinator", "technician"
    ]

    # Regular expression to find experience like "X years of experience"
    experience_patterns = [
        r"(\d{1,2})\s*(?:\+|-)?\s*(?:years?|yrs?)\s*(?:of)?\s*(?:experience|exp)?",
        r"experience\s*:\s*(\d{1,2})\s*(?:\+|-)?\s*(?:years?|yrs?)"
    ]

    years_experience = 0

    # Search for experience patterns in text
    for pattern in experience_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            years_experience = max(map(int, matches))  # Take the max experience found

    # Count occurrences of job titles (as an alternative metric)
    job_title_count = sum(1 for title in job_titles if title in text.lower())

    # Final experience score (higher of extracted years or job title count)
    return max(years_experience, job_title_count // 2)  # Assume 2 job titles ≈ 1 year exp.

