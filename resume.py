from pathlib import Path
import streamlit as st
from PIL import Image
import requests

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jonathan Hofmann"
PAGE_ICON = ":wave:"
NAME = "Jon Hofmann"
DESCRIPTION = """
Recently, I have been exploring machine learning use cases & building practical applications.
"""
EMAIL = "JChofmann99@gmail.com"
SOCIAL_MEDIA = {
    "GitHub": "https://github.com/hofmannj0n",
    "LinkedIn": "https://www.linkedin.com/in/jonathan-hofmann-67200b1b2/",
    "YouTube": "https://www.youtube.com/channel/UCoE0MAtX0RaT9Dlf_uu01mg"
}
PROJECTS = {
    "🏆 Feather - Data management Python package designed for bars and restaurants": "https://www.featherdata.io/",
    "🏆 Biomedical research - Predicting post-operative complications & using Deep learning for CT segmentation": "https://github.com/hofmannj0n/biomedical-research",
    "🏆 Automated Machine Learning - Comparing ARIMA models on stock market data": "https://github.com/hofmannj0n/Introduction-to-Quantitative-Finance-in-Python",
    "🏆 Algorithmic Trading - Trading strategies to automate financial decision making": "https://github.com/hofmannj0n/Introduction-to-Quantitative-Finance-in-Python/blob/main/tutorials/intro_to_qf_with_python.ipynb",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


css_file = "assets/main.css"
profile_pic = "assets/profile.jpeg"
resume_file = "assets/Hofmann_Jonathan.cv.pdf"
video = "assets/golf.mov"
portfolio = "assets/portfolio.png"
running = "assets/runner.JPG"
surfing = "assets/sarf.JPG"

# Fetch CSS content from URL
# css_response = requests.get(css_file)
# if css_response.status_code == 200:
#     css_content = css_response.text
#     st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)
# else:
#     st.error("Failed to fetch CSS file.")

with st.sidebar:
    choice = st.radio('Select one:', [
        'Home', 
        "Portfolio",
        "Extracurriculars", 
    ])

if choice == "Home":
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.image(profile_pic)

    with col2:
        st.header(NAME, divider='rainbow')
        st.write(":wave: Hi! I'm Jon, a Data Scientist from San Diego, California.")
        st.write(DESCRIPTION)
        st.divider()
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)
        st.write("📱", "703-304-7468")

    st.header("Social Links:", divider='red')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

    video_url = "https://www.youtube.com/watch?v=D7awk7_vO0k" 
    st.video(video_url)

    st.write('\n')
    st.header("Projects & Accomplishments", divider='violet')
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")

    st.write('\n')
    st.header("Experience & Qualifications", divider="orange")
    st.write(
        """
        ✔️ More than 2 years of proven expertise in deriving actionable insights from data

        ✔️ Demonstrated proficiency and hands-on experience in both Python and Excel

        ✔️ Sound grasp of statistical principles as well as their practical application 

        ✔️ Organized, detail-oriented individual with strong ability to learn new skills
        """
    )

if choice == "Portfolio":
    portfolio = Image.open(portfolio)
    st.subheader("For a look at my full portfolio, click [here](https://www.jhofmann.me/)")
    st.image(portfolio)

if choice == "Extracurriculars":
    st.video(video)
    running = Image.open(running)
    surfing = Image.open(surfing)
    st.image(surfing)
    st.image(running)

