import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
from pdf import extract_text
key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=key)

model = genai.GenerativeModel('gemini-2.5-flash-lite')

def analyze_resume(pdf_doc, job_des):

    if pdf_doc is not None:
        pdf_text = extract_text(pdf_doc)
        st.write(f'Text extracted successfully✔️')
                 
    else:
        st.warning(f'Error !! Drop the file in PDF format 📝')

    ats_score = model.generate_content(f'''Compare the given pdf {pdf_text}
                                       and given job description {job_des})
                                       and provide ATS score
                                       an scale of 0 to 100

                                       Generate the results in ballet points
                                       (maximum 5 points)''')
    
    probability = model.generate_content(f'''Compare the given pdf {pdf_text}
                                         and given job description {job_des}
                                         and provide the  probability to get 
                                         short lilsted for the given Job description
                                         on scale of 0 to 100
                                         
                                         Generate the results in bullet points
                                         (maximum 5 points)''')
    goodness_score = model.generate_content(f'''Compare the given pdf {pdf_text}
                                            and given job description {job_des})
                                            and say if the resume good or not
                                            for the given Job description. if it's 
                                            good give the details
                                            on scale of 0 to 100

                                            Generate the results in bullet points
                                            (maximum 5 points)''')
    swot_analysis = model.generate_content(f'''Compare the given pdf {pdf_text}
                                            and given job description {job_des})
                                            and perform the SWAT analysis

                                            Generate the results in bullet points
                                            (maximum 5 points)''')
    skill_match = model.generate_content(f'''Compare the given pdf {pdf_text}
                                            and given job description {job_des})
                                            and see if the given skills are enough 
                                            for the given Job description
                                            on scale of 0 to 100

                                            Generate the results in bullet points
                                            (maximum 5 points)''')

    return{st.write(ats_score.text),
           st.write(probability.text),
           st.write(goodness_score.text),
           st.write(swot_analysis.text),
           st.write(skill_match.text)}