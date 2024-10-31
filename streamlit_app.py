# streamlit_app.py
import streamlit as st
from dotenv import load_dotenv
from crew import crew

# Load environment variables
load_dotenv()

# Streamlit app UI
st.title("Crew AI: YouTube Video to Blog Post Creator")

# Input for the topic
topic = st.text_input("Enter the topic for the video content:", value="AI vs ML vs DL vs Data Science")

if st.button("Generate Blog Post"):
    # Kick off task execution and display results
    with st.spinner("Generating blog post..."):
        result = crew.kickoff(inputs={'topic': topic})
        st.success("Blog post generated successfully!")
        st.write(result)
        # Optionally, display result as markdown if it's saved to `new-blog-post.md`
        with open('new-blog-post.md', 'r') as file:
            st.markdown(file.read())
