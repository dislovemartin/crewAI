from crewai import Agent, Task, Crew
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define your agents
researcher = Agent(
    role='Researcher',
    goal='Research and gather information',
    backstory='Expert at gathering and analyzing information',
    verbose=True
)

writer = Agent(
    role='Writer',
    goal='Write clear and engaging content',
    backstory='Experienced content writer with expertise in technical writing',
    verbose=True
)

# Define your tasks
research_task = Task(
    description='Research the latest developments in AI',
    agent=researcher,
    expected_output='A comprehensive summary of recent AI developments and breakthroughs'
)

writing_task = Task(
    description='Write a summary of the research findings',
    agent=writer,
    expected_output='A well-written article summarizing the AI developments'
)

# Create your crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=True
)

# Start the crew
result = crew.kickoff()

print("Final Result:", result) 