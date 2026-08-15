import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

from agent import root_agent


async def main():
    session_service = InMemorySessionService()

    session = await session_service.create_session(
        app_name="day_trip_agent",
        user_id="user1"
    )

    runner = Runner(
        agent=root_agent,
        app_name="day_trip_agent",
        session_service=session_service
    )

    message = Content(
        role="user",
        parts=[Part(text="Say hello in one sentence.")]
    )

    async for event in runner.run_async(
        user_id="user1",
        session_id=session.id,
        new_message=message
    ):
        if event.content and event.content.parts:
            print(event.content.parts[0].text)


asyncio.run(main())
