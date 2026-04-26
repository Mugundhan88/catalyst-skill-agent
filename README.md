# AI-Powered Skill Assessment & Personalised Learning Plan Agent

## 🚀 Overview
A resume tells you what someone claims to know — not how well they actually know it. This agent takes a Job Description and a candidate's resume, assesses real proficiency on each required skill using semantic analysis and contextual deduction, identifies critical gaps, and generates a personalised learning plan focused on 'Adjacent Skills'.

## 🛠 Tech Stack
- **Frontend**: Streamlit
- **LLM**: GPT-4o (via OpenAI-compatible endpoint)
- **PDF Parsing**: PyPDF2
- **Logic**: Python

## 🏗 Architecture
Detailed scoring logic is in [architecture.md](./architecture.md).

### Scoring Logic
1. **Semantic Matching**: Matches skills based on meaning (e.g., "MERN stack" matches "React" and "Node.js").
2. **Contextual Proficiency**: Scores proficiency (1-10) by analyzing experience duration, project roles, and tool complexity mentioned in the resume.
3. **Gap Detection**: Lists JD requirements missing or significantly under-represented.
4. **Adjacent Skill Mapping**: Recommends skills that build upon current strengths to bridge gaps efficiently.

## 📦 Setup Instructions
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## 📝 Sample Inputs
- Sample Resume: [samples/resume.txt](./samples/resume.txt)
- Sample JD: [samples/job_description.txt](./samples/job_description.txt)

## 👨‍💻 Author
Mugundhan R
