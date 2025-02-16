# 📝 Resume Screener

Resume Screener is a **Python-based web application** that utilizes **NLP (Natural Language Processing)** to extract and analyze key details from resumes. It evaluates candidates based on **skills, experience, and projects**, ranking them intelligently to streamline the hiring process. Designed for efficiency, it helps **recruiters quickly identify the most suitable candidates.**

---

### 🔗 Live Demo  
🔗 [Resume Screener](https://resume-screener-eta.vercel.app/)

## 🏗 Tech Stack  
- **Backend:** Python (Flask, NLP with NLTK)  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **PDF Processing:** PyMuPDF (fitz)  

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

## 📌 Future Enhancements  
✅ Support for more resume formats (DOCX, TXT)  
✅ ML-based Ranking for better scoring  
✅ Resume Parsing Optimization  