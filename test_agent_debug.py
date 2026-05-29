import asyncio
import logging
from dotenv import load_dotenv
from claude_agent_sdk import query, ClaudeAgentOptions

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

async def main():
    """Test basic query with debug logging"""
    try:
        print("Testing query with debug logging...")
        async for message in query(
            prompt="Hello",
            options=ClaudeAgentOptions(allowed_tools=[])
        ):
            if hasattr(message, "result"):
                print(f"Result: {message.result}")
    except Exception as e:
        import traceback
        print(f"Error: {type(e).__name__}: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
