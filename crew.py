# crew.py
import streamlit as st
from crewai import Crew, Process
from agents import researcher, writer
from task import research_task, write_task

def main():
    st.title("YouTube Video to Blog Creator")

    # Starting the task execution process
    try:
        result = Crew(
            agents=[researcher, writer],
            tasks=[research_task, write_task],
            process=Process.sequential,
            memory=True,
            cache=True,
            max_rpm=100,
            share_crew=True
        ).kickoff(inputs={'topic': 'AI vs ML VS DL VS Data Science'})
        
        st.write(result)

    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
