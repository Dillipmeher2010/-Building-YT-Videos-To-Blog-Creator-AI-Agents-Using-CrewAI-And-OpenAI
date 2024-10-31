# agents.py
from crewai import Agent
from tools import tool

# Researcher agent
researcher = Agent(
    role='Blogs Creator from Youtube Videos',
    goal='Provide relevant video suggestions for the topic {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, Machine Learning, and Gen AI and providing suggestions."
    ),
    tools=[tool],
    allow_delegation=True
)

# Writer agent
writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about the video {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, "
        "bringing new discoveries to light in an accessible manner."
    ),
    tools=[tool],
    allow_delegation=False
)
