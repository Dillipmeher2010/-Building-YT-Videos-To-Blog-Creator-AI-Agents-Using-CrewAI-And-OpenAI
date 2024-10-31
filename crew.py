# crew.py
from crewai import Crew, Process
from agents import researcher, writer
from task import research_task, write_task

# Forming the tech-focused crew with caching enabled
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# This function will be called in the Streamlit app
def kickoff_crew(topic):
    return crew.kickoff(inputs={'topic': topic})
