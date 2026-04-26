import streamlit as st
import PyPDF2
import io
import json
from openai import OpenAI

# Configuration
client = OpenAI(
    api_key="sk-emergent-a3e0c2eBc108142Ea1",
    base_url="https://integrations.emergentagent.com/llm"
)

st.set_page_config(page_title="Skill Assessment Agent", layout="wide")

st.sidebar.title("Catalyst Skill Agent")
st.sidebar.info("AI-Powered Skill Assessment & Personalised Learning Plan")

st.title("🎯 AI Skill Assessment & Learning Plan")

col1, col2 = st.columns(2)

with col1:
    st.header("1. Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF Resume", type="pdf")
    resume_text = ""
    if uploaded_file:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            resume_text += page.extract_text()
        st.success("Resume parsed successfully!")

with col2:
    st.header("2. Job Description")
    jd_text = st.text_area("Paste the Job Description here", height=300)

if st.button("Generate Assessment"):
    if resume_text and jd_text:
        with st.spinner("Analyzing skills and generating your plan..."):
            prompt = f"""
            Analyze the following Resume and Job Description.
            
            Resume:
            {resume_text}
            
            Job Description:
            {jd_text}
            
            Provide a JSON response with:
            1. 'skills_analysis': A list of objects with 'skill', 'jd_requirement' (boolean), 'proficiency' (1-10), and 'evidence' (brief quote from resume).
            2. 'critical_gaps': A list of skills required by JD but missing or low in Resume.
            3. 'learning_plan': A list of objects with 'skill', 'resource_name', 'resource_link', 'time_estimate', and 'why_this_skill' (relation to current skills).
            4. 'overall_score': A score from 0-100.
            
            Format the response strictly as valid JSON.
            """
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                response_format={ "type": "json_object" }
            )
            
            result = json.loads(response.choices[0].message.content)
            
            st.divider()
            st.header("📊 Assessment Results")
            st.metric("Overall Match Score", f"{result['overall_score']}% ")
            
            st.subheader("Skill Proficiency")
            for skill in result['skills_analysis']:
                st.write(f"**{skill['skill']}**")
                st.progress(skill['proficiency'] / 10)
                st.caption(f"Evidence: {skill['evidence']}")
                
            st.subheader("⚠️ Critical Gaps")
            for gap in result['critical_gaps']:
                st.error(gap)
                
            st.subheader("📚 Personalized Learning Plan")
            for item in result['learning_plan']:
                with st.expander(f"Learn {item['skill']} (Est: {item['time_estimate']})"):
                    st.write(f"**Why:** {item['why_this_skill']}")
                    st.write(f"**Resource:** [{item['resource_name']}]({item['resource_link']})")
    else:
        st.warning("Please upload a resume and paste a job description.")
