import streamlit as st
from crewai import Crew  # Ensure this works after fixing imports

def main():
    st.title("YouTube Video to Blog Creator")
    st.write("This app converts YouTube videos into formatted blog posts.")
    
    video_url = st.text_input("Enter YouTube Video URL:")
    video_title = st.text_input("Enter Video Title:")
    video_description = st.text_area("Enter Video Description:")
    
    if st.button("Generate Blog Post"):
        if video_url and video_title and video_description:
            # Placeholder for actual functionality
            blog_post = f"**Title:** {video_title}\n\n**Description:** {video_description}\n\n**Video Link:** {video_url}"
            st.markdown(blog_post)
        else:
            st.error("Please fill in all fields.")

if __name__ == "__main__":
    main()
