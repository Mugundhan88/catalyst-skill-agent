# Architecture: AI-Powered Skill Assessment Agent

## 1. Data Flow
- **Ingestion**: User uploads PDF resume and pastes JD text.
- **Parsing**: `PyPDF2` extracts text from PDF.
- **Extraction**: LLM (GPT-4o) identifies and categorizes skills from both sources.
- **Analysis**:
    - **Skill Matching**: Calculates overlap and semantic similarity.
    - **Proficiency Scoring**: Infers proficiency (1-10) based on context in the resume.
    - **Gap Detection**: Highlights JD requirements not met by the resume.
- **Recommendation**:
    - **Adjacent Skill Mapping**: Recommends skills that are natural extensions of current strengths.
    - **Resource Curation**: Fetches/Generates specific learning paths with links.
- **Presentation**: Streamlit UI displays a dashboard.
