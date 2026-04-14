import streamlit as st

from analysis import analyze_resume

st.set_page_config(page_title='Resume Analyzer', page_icon='📄')
st.title('Resume Analyzer using AI ')
st.header(' :blue[AI powered Resume analyser with given job desciption using AI 🤖ིྀ]')
st.subheader(''' This page helps you to compare the resume and the givne job description and provide the ATS score, probability score, goodness of fit score, skills match score, missing keywords and SWOT analysis of the resume for the given job description.''')

pdf_doc = st.sidebar.file_uploader('Upload your resume (PDF only)', type = ['pdf'])

st.sidebar.markdown('Designed by Nandhini ✨')
st.sidebar.markdown('Git hub : https://github.com/nandhiniabds20092004-cloud/-resume_analyser.git')

job_des = st.text_area('copy and paste the job description here✍', max_chars=10000)

submit = st.button('Get Results🎯')

if submit:
    with st.spinner('Loading......⏳'):
                    analyze_resume(pdf_doc, job_des)