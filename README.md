# 📝 AI Resume Screener

AI Resume Screener is a **Python-based web application** that extracts and analyzes information from resumes using **NLP (Natural Language Processing)**. It ranks candidates based on their **skills, experience, and projects**.

---

## 🚀 Features

- 📂 **Upload & Analyze Resumes (PDF)**
- 🔍 **Extracts Key Information:**
  - **Candidate Name**
  - **Skills**
  - **Experience (years)**
  - **Projects**
- 📊 **Calculates a Resume Score**
- 🌐 **Simple & Responsive Web UI (HTML, CSS, JS, Bootstrap)**
- ⚡ **Fast & Lightweight Processing with NLP**

---

## 📊 **Resume Scoring Criteria**
The resume score is calculated based on **Skills, Experience, and Projects**, with the following weightage:

| **Criteria**      | **Weightage** |
|------------------|-------------|
| 📌 **Skills**    | **50%**      |
| 🏆 **Experience** | **30%**      |
| 💡 **Projects**  | **20%**      |

- **Skills (Max: 50 points)**  
  - Each relevant skill adds **5 points** (up to a max of 10 skills).
  
- **Experience (Max: 30 points)**  
  - 1 year = **5 points** (Max: **30 points** for **6+ years**).
  
- **Projects (Max: 20 points)**  
  - Each technical project adds **10 points** (Max: **2 projects**).

💡 **Final Score = (Skills Score) + (Experience Score) + (Projects Score)**
  
---
