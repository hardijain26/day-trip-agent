from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.tools import google_search
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part


root_agent = Agent(
    name="day_trip_agent",
    model="gemini-3.6-flash",
    description="A simple day trip planning assistant.",
    instruction="Plan a practical and enjoyable day trip based on the user's request.",
    tools=[google_search],
)
