# task.py
from crewai import Task
from tools import tool
from agents import researcher, writer

# Research task
research_task = Task(
    description=(
        "Identify the video {topic}."
        "Get detailed information about the video from the channel."
    ),
    expected_output='A comprehensive 3-paragraph report based on the {topic} of video content.',
    tools=[tool],
    agent=researcher,
)

# Writing task with asynchronous execution
write_task = Task(
    description="Get the info from the YouTube channel on the topic {topic}.",
    expected_output="Summarize the info from the YouTube channel video on the topic {topic}",
    tools=[tool],
    agent=writer,
    async_execution=True,  # Updated for asynchronous compatibility
    output_file='new-blog-post.md'
)
